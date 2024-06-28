# GPT Powered Enterprise Knowledge Search

This section contains code for various demos useful for many enterprise applications using Azure OpenAI service. The idea is to enable industries to plug each piece together and build GPT-powered applications for their needs.

## Projects

1. [Assistant Demo](./assistant-demo/README.md)
1. [Vision Demo](./vision-demo/README.md)

## SetUp

### Azure SetUp

An Azure subscription does not come by default with Azure Open AI enabled, you must request this for your organization and after the request was approved you can access Azure Open AI

1. Head over to azure portal and type in search bar `Azure Open AI`
2. Hit the `Create` button and fill out the form
   ```
   Resource Group: rg-<project name>-oai-dev
   Region: East US
   Name: oai-<project name>-dev
   Pricing Tier: Standard S0
   ```
3. Once resource was created, head over to resource and start by creating a deployment. Depending to the project a different model must be used, select any model for this step deployment name: `depl-<project name>-dev`
4. Head over to assistant playground and start chatting, your all set

## Environment SetUp

Due to frequent updates from Azure OpenAI, we'll use Pipenv to enforce specific software versions for stability and reproducibility in our projects. Ensure you follow the setup steps closely.

### Python Version

It's crucial to have Python 3.11 installed for compatibility with LangChain and OpenAI. You can check your current Python version with:

```bash
python --version
```

If you need to upgrade, on macOS, use Homebrew:

```bash
brew install python@3.11
```

Alternatively, download it directly from Python's official site if you're using a Mac.

#### Important Note on macOS Python Installation:

The default Python installed on macOS should not be altered as it is used by the operating system itself. If your system's default Python version is 2.6.1, you likely have Snow Leopard. Installing Python 3.11 won't interfere with the system's default Python if you use a versioned installation approach. After installing, you can use Python 3.11 by invoking python3.11 from the terminal. This setup leaves the original Python version intact and avoids any system issues.

### Pipenv Installation and Configuration

1. Set Up Directory:

   Create a directory for your project: `01-gpt-code-gen`.

1. Install Pipenv:

   In your terminal, execute the command `pip install pipenv` or `pip3 install pipenv`, depending on your setup.

1. Create Pipfile:

   In your `01-gpt-code-gen` directory, create a file named `Pipfile`.

1. Pipfile Configuration:

   Paste the following configuration into your new Pipfile:

   ```python
   [[source]]
   url = "https://pypi.org/simple"
   verify_ssl = true
   name = "pypi"

   [packages]
   langchain = "==0.0.352"
   openai = "==0.27.8"
   python-dotenv = "==1.0.0"

   [dev-packages]

   [requires]
   python_version = "3.11"
   ```

1. Install Dependencies:

   Run `pipenv install` within the `01-gpt-code-gen` directory to install the dependencies specified in the Pipfile.

1. Activate Environment:

   Enter the new environment by running `pipenv shell`. Your terminal will now operate within this Pipenv-managed environment.

1. Running Python Commands:

   Within the Pipenv shell, you can execute Python scripts like `python main.py`.

1. Re-enter Environment:

   If you update environment variables or keys, exit and re-enter the shell with `pipenv shell` to refresh these changes.

#### Note for Anaconda Users:

If you're using Anaconda and experience conflicts, deactivate your conda environment before proceeding with Pipenv.

#### Ignore Deprecation Warnings:

Disregard any deprecation warnings about Langchain 0.1.0 and 0.2.0, as these versions are not utilized.

#### Alternative - Requirements.txt:

If you prefer not using Pipenv, a `requirements.txt` file is available based on the Pipenv environment for traditional dependency management.

### VSCode Configuration

After activating the Pipenv environment, you might notice that VSCode Pylance is still not fully configured and throws errors for LangChain, for instance:

```bash
Import 'langchain' could not be resolved
```

To fix this, in the active environment, try to get the path to one of the installed packages, for example, LangChain:

```bash
$ python
>>> import langchain
>>> print(langchain.__file__)
/Users/<User Name>/.local/share/virtualenvs/01-gpt-code-gen-fRYM0PSj/lib/python3.11/site-packages/langchain/__init__.py

exit()
```

Copy the path up until `/site-packages/`.

Head over to VSCode settings, type "Pylance" under the extensions section.

Find the "Extra Paths" config item. Use "add item" to add a path to the parent folder of the module. It will not do any recursive tree searching.

And you should be good to go! Now imports and autocomplete should work fine.
