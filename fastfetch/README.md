# fastfetch

[fastfetch](https://github.com/fastfetch-cli/fastfetch) is a simple terminal tool that let's you display a bunch of system information inside the terminal. I primarily use it to show key information every time I start up a new terminal window.

## Installation

- Linux/Fedora — `sudo dnf install fastfetch`
- macOS — `brew install fastfetch` using [Homebrew](https://formulae.brew.sh/).

## Custom Config
I would suggest running the `fastfetch -c all.jsonc` command to see all the options available to you. Furthermore you should also check out the [official config template](https://github.com/fastfetch-cli/fastfetch/blob/dev/presets/all.jsonc). To change the default config just place `config.jsonc` and `myascii.txt` inside `~/.config/fastfetch`.

> Apparently you can also use the `fastfetch --gen-config` command to generate a custom template file. After that you just edit this file and you are good to go.

### Auto run on new terminals:
1. `nano ~/.bashrc`
2. add `fastfetch` at the bottom of the file
3. save and exit
4. reload with `source ~/.bashrc`

> If you use a Macbook you should put this into `~/.zshrc` instead of `~/.bashrc`.
