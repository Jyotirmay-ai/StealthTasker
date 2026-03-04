import pyautogui 
import random
import time
import keyboard
# --- CONFIGURATION: UPDATE THESE COORDINATES ---
# You can find the coordinates of your screen by using a tool or running a  simple Python script that prints pyautogui position()
POS_1 = (110, 260)  # Input field below "Select the two BEST images"
POS_UNSELECT = (1058, 245) # Update with the exact coordinate for unselect
POS_2 = (143, 345)  # Input field below "Select the two WORST Images"
POS_3 = (1829, 146) # "Submit" button at the top right

# Intermediate safe locations across the screen for "human-like" distraction movements
INTERMEDIATE_POSITIONS = [(132,250), (147,345), (1835, 143)]
# -----------------------------------------------

def human_like_move(x, y):
    """
    Moves the mouse to (x, y) with a randomized duration and tweening 
    to simulate human-like movement instead of instant snapping.
    """
    # Random duration between 0.5s and 1.2s to simulate human movement speed
    duration = random.uniform(0.5, 1.2)
    
    # Choose a random easing function to make the movement look less robotic and more organic
    tweens = [
        pyautogui.easeInQuad,
        pyautogui.easeOutQuad,
        pyautogui.easeInOutQuad
    ]
    selected_tween = random.choice(tweens)
    
    pyautogui.moveTo(x, y, duration=duration, tween=selected_tween)

def move_to_intermediate():
    """Moves to a random intermediate coordinate to mimic a human drifting the mouse."""
    pos = random.choice(INTERMEDIATE_POSITIONS)
    # Add some randomness to the chosen coordinate so it's never the exact same pixel
    rx = pos[0] + random.randint(-50, 50)
    ry = pos[1] + random.randint(-50, 50)
    human_like_move(rx, ry)
    time.sleep(random.uniform(0.2, 0.6))

def random_movement_delay(duration_seconds):
    """
    Moves the mouse pointer randomly around the screen for `duration_seconds`
    with varying speeds and random natural pauses.
    """
    start_time = time.time()
    
    # Get the screen size so we don't accidentally move out of bounds
    screen_width, screen_height = pyautogui.size()
    
    print(f"Beginning {duration_seconds}-second random movement phase...")
    while time.time() - start_time < duration_seconds:
        # Check kill switch during delay phase
        if keyboard.is_pressed('esc'):
            return
            
        # Optional: Occasionally don't move at all ('less than zero movement' pause)
        if random.random() < 0.2:  # 20% chance to just sit still
            time.sleep(random.uniform(0.5, 1.5))
            continue
            
        # Pick a completely random target somewhere on the screen
        target_x = random.randint(0, screen_width)
        target_y = random.randint(0, screen_height)
        
        # Pick a vastly random speed (0.1 is extremely fast twitch, 2.5 is very slow drag)
        move_duration = random.uniform(0.1, 2.5)
        
        # Move without clicking
        pyautogui.moveTo(target_x, target_y, duration=move_duration, tween=pyautogui.easeInOutQuad)
        
        # Tiny pause between random moves
        time.sleep(random.uniform(0.1, 0.5))

def main():
    print("Starting automation process in 3 seconds...")
    print("Please focus the target window or application!")
    print("==================================================")
    print("KILL SWITCH: Press and HOLD the 'ESC' key anytime to stop!")
    print("==================================================")
    time.sleep(3)

    for iteration in range(1, 51):
        if keyboard.is_pressed('esc'):
            print("\nKill switch activated! Stopping script gracefully.")
            break
            
        print(f"\n--- Starting Iteration {iteration} / 50 ---")
        # 1. Pick two unique random numbers between 1 and 8
        set_1 = random.sample(range(1, 9), 2)
        
        # 2. Pick two more unique random numbers between 1 and 8, excluding the ones from set_1
        remaining_numbers = list(set(range(1, 9)) - set(set_1))
        set_2 = random.sample(remaining_numbers, 2)
        
        print(f"Generated first set of numbers: {set_1}")
        print(f"Generated second set of numbers: {set_2}")

        # === STEP 1: POSITION 1 ===
        print(f"Moving to Position 1 {POS_1}...")
        human_like_move(POS_1[0], POS_1[1])
        pyautogui.click()
        time.sleep(random.uniform(0.2, 0.5))
        
        # "Add two random numbers"
        # Assuming this means typing the two numbers sequentially
        # "Add two random numbers" - type first, hit enter, type second, hit enter
        print(f"Typing numbers: {set_1[0]} then Enter, {set_1[1]} then Enter")
        pyautogui.write(str(set_1[0]))
        time.sleep(random.uniform(0.1, 0.3))
        pyautogui.press('enter')
        time.sleep(random.uniform(0.3, 0.6))
        pyautogui.write(str(set_1[1]))
        time.sleep(random.uniform(0.1, 0.3))
        pyautogui.press('enter')
        time.sleep(random.uniform(0.3, 0.7))

        # Intermediate human-like mouse drift
        print("Performing intermediate human drift...")
        move_to_intermediate()

        # === STEP 1.5: POS_UNSELECT ===
        print(f"Moving to POS_UNSELECT {POS_UNSELECT} for a normal click...")
        human_like_move(POS_UNSELECT[0], POS_UNSELECT[1])
        pyautogui.click()
        time.sleep(random.uniform(0.2, 0.5))

        # === STEP 2: POSITION 2 ===
        print(f"Moving to Position 2 {POS_2}...")
        human_like_move(POS_2[0], POS_2[1])
        pyautogui.click()
        time.sleep(random.uniform(0.2, 0.5))

        # "Add two random numbers (different from first position)" - type first, hit enter, type second, hit enter
        print(f"Typing numbers: {set_2[0]} then Enter, {set_2[1]} then Enter")
        pyautogui.write(str(set_2[0]))
        time.sleep(random.uniform(0.1, 0.3))
        pyautogui.press('enter')
        time.sleep(random.uniform(0.3, 0.6))
        pyautogui.write(str(set_2[1]))
        time.sleep(random.uniform(0.1, 0.3))
        pyautogui.press('enter')
        time.sleep(random.uniform(0.3, 0.7))

        # Intermediate human-like mouse drift
        print("Performing intermediate human drift...")
        move_to_intermediate()

        # === STEP 3: POSITION 3 ===
        print(f"Moving to final Position 3 {POS_3}...")
        human_like_move(POS_3[0], POS_3[1])
        time.sleep(random.uniform(0.2, 0.5))
        
        # "1 click one on a button"
        print("Clicking the final button...")
        pyautogui.click()
        
        # Pause briefly before the next iteration begins (gives the website time to load next task)
        # We now use our new random movement delay function!
        random_movement_delay(10)

    print("\nProcess finished.")

if __name__ == "__main__":
    main()
