## Run experiments

```bash
nohup python main.py --config config/halfcheetah/halfcheetah-expert-v2.yaml --seed 0 --max_timesteps 100000 > nohup/average-threshold-over-states/01.out 2>&1 &
```

```bash
nohup python main.py --config config/antmaze/antmaze-medium-play-v2.yaml --seed 0 --max_timesteps 100000 > nohup/average-threshold-over-states/02.out 2>&1 &
```

```bash
nohup python main.py --config config/hopper/hopper-medium-replay-v2.yaml --seed 0 --max_timesteps 100000 > nohup/average-threshold-over-states/03.out 2>&1 &
```

```bash
nohup python main.py --config config/walker2d/walker2d-expert-v2.yaml --seed 0 --max_timesteps 100000 > nohup/average-threshold-over-states/04.out 2>&1 &
```