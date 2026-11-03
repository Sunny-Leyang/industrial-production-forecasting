"""Execute the report analysis with the Python environment running this command."""
from pathlib import Path
import json
import os
import sys
import tempfile

import nbformat
from nbclient import NotebookClient
from jupyter_client import KernelManager


def main():
    root = Path(__file__).resolve().parents[1]
    path = root / "notebooks/01_indpro_analysis.ipynb"
    notebook = nbformat.read(path, as_version=4)
    with tempfile.TemporaryDirectory(prefix="indpro-runtime-") as temporary:
        environment = os.environ.copy()
        environment["IPYTHONDIR"] = str(Path(temporary) / "ipython")
        environment["MPLCONFIGDIR"] = str(Path(temporary) / "matplotlib")
        environment["JUPYTER_RUNTIME_DIR"] = str(Path(temporary) / "jupyter")
        manager = KernelManager(kernel_name="python3")
        # Avoid silently executing a globally installed kernel from a different environment.
        manager.kernel_spec.argv = [sys.executable, "-m", "ipykernel_launcher", "-f", "{connection_file}"]
        try:
            NotebookClient(notebook, km=manager, timeout=300,
                           resources={"metadata": {"path": str(root)}}).execute(env=environment)
        finally:
            if manager.has_kernel:
                manager.shutdown_kernel(now=True)
        nbformat.validate(notebook)
        nbformat.write(notebook, path)
    validation = json.loads((root / "results/validation.json").read_text())
    if not validation["passed"]:
        raise RuntimeError("Reference validation failed.")
    print(json.dumps(validation, indent=2))
    print("Reproduced notebook, figures and results with:", sys.executable)


if __name__ == "__main__":
    main()
