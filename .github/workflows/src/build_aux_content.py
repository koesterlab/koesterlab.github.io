from pathlib import Path
import yaml
import subprocess as sp
from git import Repo
import shutil

aux_content = yaml.safe_load(open(Path(__file__) / "aux_content.yml"))

for repo in aux_content:
    repo_name = Path(repo).basename()
    repo_dir: Path = Path("build") / repo_name
    repo_dir.mkdir(parents=True, exist_ok=True)
    Repo.clone_from(f"https://github.com/{repo}", repo_dir)

    sp.call(["pixi", "run", "build"], check=True, cwd=repo_dir)
    shutil.copytree(
        repo_dir / "build/html", Path("src/teaching") / repo_name, dirs_exist_ok=True
    )
