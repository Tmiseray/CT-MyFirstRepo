exercise_data = {}

def log_exercise(exercise, duration):
    exercise_data[exercise] = exercise_data.get(exercise, 0) + duration

def get_total_exercise_time():
    return sum(exercise_data.values())
