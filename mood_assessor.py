from pathlib import Path
import datetime

def get_mood():
    valid_moods = ["happy", "relaxed", "apathetic", "sad", "angry"]
    mood_to_value = {
        "happy": 2,
        "relaxed": 1,
        "apathetic": 0,
        "sad": -1,
        "angry": -2
    }
    
    while True:
        mood = input("Please enter your current mood (happy, relaxed, apathetic, sad, angry): ").lower()
        if mood in valid_moods:
            return mood_to_value[mood]
        else:
            print("Invalid mood. Please try again.")

def log_mood(mood_value):
    directory = Path("data")
    file_path = directory / "mood_diary.txt"
    if not directory.exists():
        directory.mkdir(parents=True, exist_ok=True)

 
    with file_path.open("a") as file:
        file.write(f"{get_date_today()}: {mood_value}\n")

def get_date_today():
    return str(datetime.date.today())

def has_already_logged_today():
    date = get_date_today()
    file_path = Path('data/mood_diary.txt')

    if file_path.exists():
        with file_path.open('r') as file:
            lines = file.readlines()
            for line in lines:
                if date in line:
                    return True
    return False

def diagnose_disorder():
    file_path = Path('data/mood_diary.txt')
    
    if file_path.exists():
        with file_path.open('r') as file:
            lines = file.readlines()
            if len(lines) < 7:
                return "There is not enough data to diagnose."

            full_log = lines[-7:]
            mood_values = [int(line.split(":")[1]) for line in full_log]
            average_mood = round(sum(mood_values) / len(mood_values))
            if mood_values.count(2) >= 5:
                diagnosis = "manic"
            elif mood_values.count(-1) >= 4:
                diagnosis = "depressive"
            elif mood_values.count(0) >= 6:
                diagnosis = "schizoid"
            else:
                diagnosis = average_mood_to_string(average_mood)

            return f"Your diagnosis: {diagnosis}!"


def average_mood_to_string(average_mood):
    if average_mood == 2:
        return "happy"
    elif average_mood == 1:
        return "relaxed"
    elif average_mood == 0:
        return "apathetic"
    elif average_mood == -1:
        return "sad"
    elif average_mood == -2:
        return "angry"

def assess_mood():
    if has_already_logged_today():
        print("Sorry, you have already entered your mood today.")
        return
    
    mood_value = get_mood()
    log_mood(mood_value)
    print("Your mood has been logged successfully.")
    
    diagnosis = diagnose_disorder()
    if diagnosis:
        print(diagnosis)
