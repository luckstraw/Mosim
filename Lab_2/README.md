# Laboratory Activity # 2: System Dynamics & Discrete-Event Simulation in Python

Simulation Modeling Using Python

## Running the program

Follow these steps to execute the program:

1. **Make the code executable then run the program**:
```bash
chmod +x run.sh
```
```bash
./run.sh
```

## Output:

After running the `./run.sh` you will see the output of 4 files

- *`part_1.py*
    ```bash
    Year 1: Population = 101000
    Year 2: Population = 102010
    Year 3: Population = 103030
    Year 4: Population = 104060
    Year 5: Population = 105101
    Year 6: Population = 106152
    Year 7: Population = 107213
    Year 8: Population = 108285
    Year 9: Population = 109368
    Year 10: Population = 110462
    ```

- *`part_2.py*
    ```bash
    Turning ON air conditioner | Current Temperature: 24°C
    Turning ON air conditioner | Current Temperature: 23°C
    Temperature stable | Current Temperature: 22°C
    Temperature stable | Current Temperature: 22°C
    ```

- *`part_3.py*
    ```bash
    Customer Arrival at 11:06:09 PM
    Order Taken at 11:06:10 PM
    Food Preparation Complete at 11:06:12 PM
    Customer Departure at 11:06:17 PM
    ```
- *`part_4.py*
    ```bash
    Passenger 1 is being served...
    Passenger 1 finished check-in.

    Passenger 2 is being served...
    Passenger 2 finished check-in.

    Passenger 3 is being served...
    Passenger 3 finished check-in.

    Passenger 4 is being served...
    Passenger 4 finished check-in.

    Passenger 5 is being served...
    Passenger 5 finished check-in.
    ```

## Reflection Question: 
- **Question**: “What are the advantages and disadvantages of continuous vs discrete simulation in real-world systems?”

- **Answer**: 

    Continuous Simulation - Best for gradual processes (e.g., climate change, physics). More precise but computationally heavy. Hard to track stepwise interactions.

    Discrete Simulation - Best for event-driven systems (e.g., queues, inventory). Efficient and easier to analyze. Less precision for gradual changes.

    Which to use?

    Continuous → Smooth, evolving systems.
    Discrete → Stepwise, event-driven systems.