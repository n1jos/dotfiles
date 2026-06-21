# gitconfig

Per-host Git identity using `includeIf` directives. This keeps GitHub and Gitea commits attributed to different email addresses without having to set anything per-repo manually.

## Structure

- `.gitconfig` — main config, symlinked to `~/.gitconfig`
- `.gitconfig-github` — identity for repos under `~/Documents/github/`
- `.gitconfig-gitea` — identity for repos under `~/Documents/gitea/`
- `.gitignore_global` — patterns Git ignores in every repo

The `-github` and `-gitea` files are templates with placeholder values. Fill in your real name and email after symlinking.

## How it works

Git's `includeIf "gitdir:..."` applies a config file conditionally based on where the repo lives. Keeping GitHub and Gitea repos in separate folders is all that's needed for the right identity to be picked up automatically.

## Global gitignore

`.gitconfig` points `core.excludesfile` at `~/.gitignore_global`, so its patterns are ignored across every repo without touching each project's own `.gitignore`. It's the place for machine- or OS-specific clutter you never want committed anywhere — currently just `.DS_Store`. Add your own editor/tooling junk (e.g. `*.swp`, `.idea/`) here as needed.

## Tip: privacy email for GitHub

To keep your real address out of public commit metadata, you can set `.gitconfig-github`'s email to GitHub's no-reply alias (`12345678+username@users.noreply.github.com`), found under GitHub → Settings → Emails. This is optional — use any email you like.
