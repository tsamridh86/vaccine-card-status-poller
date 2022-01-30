# Vaccine Card Status Poller

Simple program written in python to poll the nepal govt. website to check if your vaccine card has been generated.

**Important: Does not download your vaccine card for you!**

---

## How to use

1. Run:

    ```
    pip install -r requirements.txt 
    ```

2. Open `config.yaml` and add / remove people with thier name and registration number accordingly.

3. Change `duration` if required, set to a sensible default of 60 mins, any number > 0 is supported ( even decimals ). Must be written in minutes.

4. Run:
  
  ```
  python main.py
  ```

---

## To do:

1. Download and save the vaccine card.
2. Ignore people who already got the vaccine card.
