## Troubleshooting

Requires Python 3.8.5

1. Anaconda Installation [(Install instructions)](https://www.anaconda.com/docs/getting-started/anaconda/install)

2. Download the MuJoCo version 2.1 binaries for Linux

```bash
wget https://mujoco.org/download/mujoco210-linux-x86_64.tar.gz

tar -xvzf mujoco210-linux-x86_64.tar.gz

mkdir ~/.mujoco/

mv mujoco210/ ~/.mujoco/

echo 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$HOME/.mujoco/mujoco210/bin' >> ~/.bashrc

source ~/.bashrc
```

3. Create Anaconda environment

```bash
conda create -n scq python=3.8.5 pip

conda activate scq
```

4. To install `mujoco-py` on Ubuntu, make sure you have the following libraries installed

```bash
sudo apt install libosmesa6-dev libgl1 libglx-mesa0 libglfw3 build-essential patchelf
```

5. Link the lib file into the conda environment [(Question Link - Ask Ubuntu)](https://askubuntu.com/questions/1418016/glibcxx-3-4-30-not-found-in-conda-environment)

```bash
ln -sf /usr/lib/x86_64-linux-gnu/libstdc++.so.6 ${CONDA_PREFIX}/lib/libstdc++.so.6
```

6. Install `gym==0.18.3`

```bash
git clone https://github.com/openai/gym

cd gym

git checkout 0.18.3
```

Fix `setup.py`, use `opencv-python>=3.0.0` in extras. Install dependencies using pip.

```bash
pip install -e .
```

7. Install the remaining dependencies.

```bash
pip install -r requirements.txt
```

8. See if `mujoco-py` is installed.

```bash
python mujoco-py-test.py
```
