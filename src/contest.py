import gymnasium as gym
import numpy as np
import pickle


def check_submission(submission_bytes):
    env = gym.make("CartPole-v1", render_mode=None)

    pos_space = np.linspace(-2.4, 2.4, 10)
    vel_space = np.linspace(-4, 4, 10)
    ang_space = np.linspace(-0.2095, 0.2095, 10)
    ang_vel_space = np.linspace(-4, 4, 10)

    q = pickle.loads(submission_bytes)

    rewards_per_episode = []

    episodes = 100

    for _ in range(episodes):

        state = env.reset()[0]
        state_p = np.digitize(state[0], pos_space)
        state_v = np.digitize(state[1], vel_space)
        state_a = np.digitize(state[2], ang_space)
        state_av = np.digitize(state[3], ang_vel_space)

        terminated = False

        rewards = 0

        while not terminated:

            action = np.argmax(q[state_p, state_v, state_a, state_av, :])

            new_state, reward, terminated, _, _ = env.step(action)
            new_state_p = np.digitize(new_state[0], pos_space)
            new_state_v = np.digitize(new_state[1], vel_space)
            new_state_a = np.digitize(new_state[2], ang_space)
            new_state_av = np.digitize(new_state[3], ang_vel_space)

            state = new_state
            state_p = new_state_p
            state_v = new_state_v
            state_a = new_state_a
            state_av = new_state_av

            rewards += reward

        rewards_per_episode.append(rewards)

    mean_rewards = np.mean(rewards_per_episode)

    env.close()

    return mean_rewards
