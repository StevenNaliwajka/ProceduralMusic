
import sys
import select

def user_input_stop_flag_check(stop_flag):
    while not stop_flag.is_set():
        try:
            user_input = input("Type 'stop' to stop playback: ").strip().lower()
            if user_input == "stop":
                stop_flag.set()
                print("Playback stopped.")
                break
        except KeyboardInterrupt:
            print("\nMonitoring interrupted by user.")
            stop_flag.set()
            break
        except Exception as e:
            print(f"An error occurred: {e}")