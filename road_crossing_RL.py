# Q-Learning + Pygame Simple RL Road Crossing

import pygame
import numpy as np
import random

# Game settings
WIDTH, HEIGHT = 600, 100
CELL_SIZE = 100
N_CELLS = WIDTH // CELL_SIZE

# Q-Learning settings
alpha = 0.1
gamma = 0.95
epsilon = 1.0
epsilon_decay = 0.995
min_epsilon = 0.01
episodes = 500

# Rewards
REWARD_GOAL = 10
REWARD_STEP = -0.1

# Initialize pygame
pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("RL Agent - Road Crossing")

# Q-table: (state, action) -> Q-value
q_table = np.zeros((N_CELLS, 2))  # 2 actions: left(0), right(1)

# Actions
ACTION_LEFT = 0
ACTION_RIGHT = 1
ACTIONS = [ACTION_LEFT, ACTION_RIGHT]

# Draw environment
def draw(state):
    win.fill((255, 255, 255))
    
    # Draw cells
    for i in range(N_CELLS):
        rect = pygame.Rect(i * CELL_SIZE, 0, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(win, (200, 200, 200), rect, 2)
    
    # Draw goal
    goal_rect = pygame.Rect((N_CELLS - 1) * CELL_SIZE, 0, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(win, (0, 255, 0), goal_rect)
    
    # Draw agent
    agent_rect = pygame.Rect(state * CELL_SIZE, 0, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(win, (0, 0, 255), agent_rect)
    
    pygame.display.update()

# Main training loop
for ep in range(episodes):
    state = 0  # Start at left-most cell
    done = False
    
    while not done:
        # Epsilon-greedy action selection
        if random.uniform(0, 1) < epsilon:
            action = random.choice(ACTIONS)
        else:
            action = np.argmax(q_table[state])
        
        # Take action
        next_state = state
        if action == ACTION_LEFT and state > 0:
            next_state -= 1
        elif action == ACTION_RIGHT and state < N_CELLS - 1:
            next_state += 1
        
        # Get reward
        if next_state == N_CELLS - 1:
            reward = REWARD_GOAL
            done = True
        else:
            reward = REWARD_STEP
        
        # Q-Learning update
        old_q = q_table[state, action]
        next_max_q = np.max(q_table[next_state])
        
        new_q = old_q + alpha * (reward + gamma * next_max_q - old_q)
        q_table[state, action] = new_q
        
        state = next_state
        
        # Draw current state
        draw(state)
        pygame.time.delay(50)
    
    # Decay epsilon
    if epsilon > min_epsilon:
        epsilon *= epsilon_decay
    
    # Print progress
    if (ep + 1) % 50 == 0:
        print(f"Episode {ep + 1}/{episodes}, epsilon={epsilon:.3f}")

# Done training
print("Training completed!")

# Wait before quitting
pygame.time.wait(2000)
pygame.quit()
