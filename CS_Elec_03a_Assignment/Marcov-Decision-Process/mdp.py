import random

states = ["A", "B", "C"]
actions = ["left", "right"]

# Rewards
rewards = {
    ("A", "right"): 1,
    ("B", "right"): 2,
    ("C", "right"): 5
}

# Transition function
def next_state(state, action):
    if action == "right":
        if state == "A":
            return "B"
        elif state == "B":
            return "C"
    return state  # stay if left

# Simulation
current_state = "A"
total_reward = 0

for step in range(5):
    action = random.choice(actions)
    new_state = next_state(current_state, action)

    reward = rewards.get((current_state, action), 0)
    total_reward += reward

    print(f"State: {current_state}, Action: {action}, Reward: {reward}")

    current_state = new_state

print("Total reward:", total_reward)