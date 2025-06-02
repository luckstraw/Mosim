import random
# Constants
SIMULATION_TIME = 480 # minutes (8 hours)
PATIENTS = 1000
AVG_CONSULT_TIME = 8 # minutes
AVG_VACCINE_TIME = 5 # minutes

def simulate(doctors, nurses):
    time = 0
    patients_served = 0

    waiting_time = []
    doctor_queue = []
    nurse_queue = []
    # Generate random arrival times for patients
    arrival_times = sorted([random.randint(0, SIMULATION_TIME - 1) for _ in range(PATIENTS)])
    # Keep track of doctors and nurses' availability
    doctor_available = [0] * doctors
    nurse_available = [0] * nurses

    for arrival in arrival_times:
        # Assign to the first available doctor
        soonest_doc = min(doctor_available)
        if soonest_doc <= arrival:
            start_consult = arrival
        else:
            start_consult = soonest_doc

        consult_end = start_consult + AVG_CONSULT_TIME
        doc_index = doctor_available.index(soonest_doc)
        doctor_available[doc_index] = consult_end

        # After consultation, wait for nurse
        soonest_nurse = min(nurse_available)
        if soonest_nurse <= consult_end:
            start_vaccine = consult_end
        else:
            start_vaccine = soonest_nurse

        vaccine_end = start_vaccine + AVG_VACCINE_TIME
        nurse_index = nurse_available.index(soonest_nurse)
        nurse_available[nurse_index] = vaccine_end
        total_wait = (start_consult - arrival) + (start_vaccine - consult_end)
        waiting_time.append(total_wait)

        if vaccine_end <= SIMULATION_TIME:
            patients_served += 1

    avg_wait = sum(waiting_time) / len(waiting_time)
    return patients_served, avg_wait

# Try different allocations
print("Doctors | Nurses | Patients Served | Avg. Wait Time (mins)")

for d in range(1, 4):
    for n in range(1, 4):
        served, avg_wait = simulate(d, n)
        print(f"{d:^7} | {n:^6} | {served:^15} | {avg_wait:^21.2f}")