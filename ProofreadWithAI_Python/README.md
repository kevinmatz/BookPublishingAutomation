# Log of steps to run this program

* TODO: "python -m pip install openai" fails on Windows (both inside a conda environment and outside, and in both cmd and PowerShell, with and without Admin privileges) due to a "yarl" build error and there's no clear answer; the general advice seems to be "don't use Windows", sigh

* `C:\GitRepos\BookPublishingAutomation> conda create --name BookPublishingAutomationEnv python=3.9`
  * set Python version to 3.9 as a forum post implied that the "yarl"/"wheel" build issue was due to an incompatibility with Python 3.11/3.12 (3.12.0 is what's currently installed as the main Python version on my Windows machine)

* `C:\GitRepos\BookPublishingAutomation> conda activate BookPublishingAutomationEnv`

* In VSCode, using Python button in left side panel, selected "BookPublishingAutomationEnv" as the workspace environment, and opened a terminal within VSCode

* `python -m pip install -r requirements.txt` to install prerequisite packages

* I got a `ModuleNotFoundError: No module named 'pkg_resources'` error when running the program; according to https://stackoverflow.com/questions/7446187/no-module-named-pkg-resources it may be due to a broken `setuptools` install
  * Problem was resolved by running (in the conda environment): `pip install --upgrade setuptools`
  
* Run (in ProofreadWithAI folder):
  * `python ProofreadWithAI.py TestDataInputs/CorporateCultureTermPaper.docx output.docx`

