# ML-project
ML, Devops, MLops Project
this is for learning purpose

NOTES
Note on Frontend Testing Issue in GitHub Actions
I am currently facing an issue with testing the frontend part of my application using Selenium on GitHub Actions. The frontend tests work perfectly on my local machine (Windows OS), where I use Chrome and Chromedriver to automate the browser interactions. However, my attempts to replicate this setup in the GitHub Actions environment (Ubuntu) have not been successful.

Attempts to Solve the Issue:
Installing Chrome and Chromedriver:

I tried installing Chrome and Chromedriver in the GitHub Actions workflow using wget to download the .deb package for Chrome and the corresponding Chromedriver version.
Despite resolving dependencies with sudo apt-get -f install, the installation process fails intermittently, causing the workflow to exit with an error (exit code 8).
Dynamic Chromedriver Version Matching:

I ensured that the version of Chromedriver matches the installed version of Chrome by dynamically fetching the version using google-chrome --version. This works locally but doesn't resolve the issue in the GitHub Actions environment.
Headless Mode:

I configured Selenium to run Chrome in headless mode to avoid GUI-related issues. This works locally but doesn't seem to help in the GitHub Actions setup.
Dependency Fixes:

I added commands like sudo apt-get update and sudo apt-get -f install to resolve any broken dependencies during the Chrome installation process. However, the issue persists.
Current Status:
The frontend tests work flawlessly on my local Windows machine.
On GitHub Actions, the Chrome installation step fails, preventing the tests from running.
I am exploring alternative approaches, such as using a pre-installed browser in the GitHub Actions environment or switching to a different browser (e.g., Firefox with Geckodriver) to bypass the Chrome installation issues.

# Future Steps:
1. Investigate the specific error messages from the GitHub Actions logs to identify the root cause of the Chrome installation failure.
2. Consider using a Docker container with a pre-configured environment that includes Chrome and Chromedriver to ensure consistency across local and CI environments.
3. Explore using a different browser or testing framework that may have better support in the GitHub Actions environment.
# ML Project
