from pathlib import Path
import yaml
import subprocess as sp
import shutil

aux_content = yaml.safe_load(open(Path(__file__).parent / "aux_content.yml"))

for repo in aux_content:
    repo_name = Path(repo).name
    repo_dir: Path = Path("build") / repo_name
    repo_dir.mkdir(parents=True, exist_ok=True)
    sp.run(["git", "clone", f"https://github.com/{repo}", str(repo_dir)], check=True)

    sp.run(["pixi", "run", "build"], check=True, cwd=repo_dir)
    teaching_dir = Path("src/teaching")
    teaching_dir.mkdir(parents=True, exist_ok=True)
    shutil.copytree(
        repo_dir / "build/html", teaching_dir / repo_name, dirs_exist_ok=True
    )
