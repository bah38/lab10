import os
import runpy
import shutil
from pathlib import Path
from tempfile import TemporaryDirectory


def deploy():
    source = Path(__file__).with_name("app.py")
    jenkins_home = Path(os.environ.get("JENKINS_HOME", Path.home()))
    build = os.environ.get("BUILD_NUMBER", "manual")
    destination = jenkins_home / "lab10-deployments" / "Python-CI-CD" / build
    destination.mkdir(parents=True, exist_ok=True)

    with TemporaryDirectory(dir=destination) as staging_directory:
        staged_app = Path(staging_directory) / source.name
        shutil.copyfile(source, staged_app)
        print("Running deployment smoke test:")
        runpy.run_path(str(staged_app), run_name="__main__")
        deployed_app = destination / source.name
        staged_app.replace(deployed_app)

    print(f"Deployed application to {deployed_app}")


if __name__ == "__main__":
    deploy()
