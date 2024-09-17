# How to use zprocess to run RPC

The Notebooks in this repo show how to run a remote process and communicate with it using zprocess.


## For nix users

### For the first time
To create a quick ad-hoc environment for these tests use the commands:
```bash
nix-shell
virtualenv . 
source ./bin/activate
pip install -r requirements.txt
jupyter lab
```
### For the next times

The envoronment is created therefore you can simply run:
```bash
nix-shell 
source ./bin/activate
jupyter lab
```

