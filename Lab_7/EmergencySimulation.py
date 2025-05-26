import simpy
import random
import statistics
import pandas as pd
import matplotlib.pyplot as plt

# Constants
SIM_DURATION = 12 * 60  # minutes
INTERARRIVAL_MEAN = 5  # minutes
NURSE_MEAN = 6  # service time mean
DOCTOR_MEAN = 8
COST_DOCTOR = 50  # $/hour
COST_NURSE = 30
BUDGET = 4800  # $/day


def patient(env, name, nurses, doctors, wait_times):
    arrival = env.now
    # Nurse stage
    with nurses.request() as req_n:
        yield req_n
        wait_nurse = env.now - arrival
        # service
        yield env.timeout(random.expovariate(1.0 / NURSE_MEAN))

    # Doctor stage
    with doctors.request() as req_d:
        yield req_d
        wait_doctor = env.now - (arrival + wait_nurse)
        yield env.timeout(random.expovariate(1.0 / DOCTOR_MEAN))

    total_wait = wait_nurse + wait_doctor
    wait_times.append(total_wait)


def run_one(env, num_nurses, num_doctors):
    nurses = simpy.Resource(env, capacity=num_nurses)
    doctors = simpy.Resource(env, capacity=num_doctors)
    wait_times = []

    def arrival_process():
        i = 0
        while True:
            yield env.timeout(random.expovariate(1.0 / INTERARRIVAL_MEAN))
            i += 1
            env.process(patient(env, f"Patient_{i}", nurses, doctors, wait_times))

    env.process(arrival_process())
    env.run(until=SIM_DURATION)
    return statistics.mean(wait_times), sum(wait_times)


def optimize():
    results = []
    for n in range(1, 6):
        for d in range(1, 6):
            cost = (n * COST_NURSE + d * COST_DOCTOR) * 12
            if cost <= BUDGET:
                env = simpy.Environment()
                avg_wait, total_wait = run_one(env, n, d)
                results.append({
                    'nurses': n,
                    'doctors': d,
                    'cost': cost,
                    'avg_wait': avg_wait
                })
    return pd.DataFrame(results)


def sensitivity(base_config, var, levels):
    sens = []
    for pct in levels:
        globals()[var] = globals()[var] * (1 + pct)
        env = simpy.Environment()
        avg_wait, _ = run_one(env, base_config['nurses'], base_config['doctors'])
        sens.append({'change': pct, 'avg_wait': avg_wait})
        # reset
        globals()[var] = globals()[var] / (1 + pct)
    return pd.DataFrame(sens)


if __name__ == '__main__':
    # Optimization
    df = optimize()
    print(df)
    best = df.loc[df['avg_wait'].idxmin()]

    # Sensitivity on INTERARRIVAL_MEAN ±10,20,30%
    levels = [-0.3, -0.2, -0.1, 0.1, 0.2, 0.3]
    sens_df = sensitivity(best, 'INTERARRIVAL_MEAN', levels)

    # Plot sensitivity
    plt.figure()
    plt.plot(sens_df['change'], sens_df['avg_wait'], marker='o')
    plt.xlabel('Change in arrival rate')
    plt.ylabel('Average wait (min)')
    plt.title('Sensitivity Analysis')
    plt.show()

    # Save results
    df.to_csv('optimization_results.csv', index=False)
    sens_df.to_csv('sensitivity_results.csv', index=False)
