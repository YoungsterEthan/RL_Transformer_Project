import gym
import torch

env = gym.make('CartPole-v1')
obs = env.reset()

print("initial observation", obs)
print("torch version: ", torch.__version__)