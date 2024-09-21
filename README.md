# hub
JGWill's Hub

----
generated doc to help plan

# jgwillhub Documentation

## Overview

The `jgwillhub` module provides a convenient way to pull prompt templates from the LangSmith Hub, specifically from the user [`jgwill`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fjgi%2FDropbox%2Fg%2Fpractice_orpheuspy%2Fsrc%2Fjghfmanager%2FREADME.md%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A38%2C%22character%22%3A94%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fjgi%2FDropbox%2Fg%2Fpractice_orpheuspy%2Fsrc%2Fjghfmanager%2F.hch%2Fissue_add__2409210710.md%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A2%2C%22character%22%3A30%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fjgi%2FDropbox%2Fg%2Fpractice_orpheuspy%2Fsrc%2Fjghfmanager%2Fjghfmanager%2Fcminferencer.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A69%2C%22character%22%3A40%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fjgi%2FDropbox%2Fg%2Fpractice_orpheuspy%2Fsrc%2Fjghfmanager%2Fsetup.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A7%2C%22character%22%3A28%7D%7D%5D%2C%22a69b3260-2643-4c48-9fac-b79e1c1a3aed%22%5D "Go to definition"). This module wraps the functionality of [`langchainhub`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fjgi%2FDropbox%2Fg%2Fpractice_orpheuspy%2Fsrc%2Fjghfmanager%2FREADME.md%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A54%2C%22character%22%3A15%7D%7D%5D%2C%22a69b3260-2643-4c48-9fac-b79e1c1a3aed%22%5D "Go to definition") and offers additional capabilities through a CLI tool and YAML configuration.

## Installation

To install the `jgwillhub` module, run:

```sh
pip install -U jgwillhub
```

## Usage

### Python Example

You can pull a prompt template using the following code:

```python
from jgwillhub import hub

tool_hub_tag = "jgwill/cmpenghelperbeta"
prompt_template = hub.pull(tool_hub_tag)
```

### CLI Tool

The `jgwillhub` module includes a CLI tool named `jhub` that allows you to list and manage prompts from the user [`jgwill`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fjgi%2FDropbox%2Fg%2Fpractice_orpheuspy%2Fsrc%2Fjghfmanager%2FREADME.md%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A38%2C%22character%22%3A94%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fjgi%2FDropbox%2Fg%2Fpractice_orpheuspy%2Fsrc%2Fjghfmanager%2F.hch%2Fissue_add__2409210710.md%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A2%2C%22character%22%3A30%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fjgi%2FDropbox%2Fg%2Fpractice_orpheuspy%2Fsrc%2Fjghfmanager%2Fjghfmanager%2Fcminferencer.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A69%2C%22character%22%3A40%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fjgi%2FDropbox%2Fg%2Fpractice_orpheuspy%2Fsrc%2Fjghfmanager%2Fsetup.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A7%2C%22character%22%3A28%7D%7D%5D%2C%22a69b3260-2643-4c48-9fac-b79e1c1a3aed%22%5D "Go to definition") in the LangSmith Hub.

#### List Prompts

To list all available prompts from the user [`jgwill`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fjgi%2FDropbox%2Fg%2Fpractice_orpheuspy%2Fsrc%2Fjghfmanager%2FREADME.md%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A38%2C%22character%22%3A94%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fjgi%2FDropbox%2Fg%2Fpractice_orpheuspy%2Fsrc%2Fjghfmanager%2F.hch%2Fissue_add__2409210710.md%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A2%2C%22character%22%3A30%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fjgi%2FDropbox%2Fg%2Fpractice_orpheuspy%2Fsrc%2Fjghfmanager%2Fjghfmanager%2Fcminferencer.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A69%2C%22character%22%3A40%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fjgi%2FDropbox%2Fg%2Fpractice_orpheuspy%2Fsrc%2Fjghfmanager%2Fsetup.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A7%2C%22character%22%3A28%7D%7D%5D%2C%22a69b3260-2643-4c48-9fac-b79e1c1a3aed%22%5D "Go to definition"), run:

```sh
jhub list
```

## Configuration

The `jgwillhub` module supports a YAML configuration file named `jgwill-hub.yml`. This file can be placed in the current directory or in the home directory. The configuration file defines the supported prompts and their descriptions, which can be exposed to agents in various formats such as a schema or a markdown table.

### Example Configuration

```yaml
prompts:
  - tag: "jgwill/cmpenghelperbeta"
    description: "Create a ChatMusician Musical Inference Request"
    variables:
      - creation_name
      - seq_name
      - musical_notes
  - tag: "jgwill/json2yaml"
    description: "Simple Tool to convert input JSON into YAML"
  - tag: "jgwill/sfcp"
    description: "Shift focus from technical-aspect to creative practitionner perspective"
    variables:
      - content
  - tag: "jgwill/stcgoalsfcp"
    description: "Shift focus from technical-aspect to creative practitionner perspective with a structured user goal in the inputs"
    variables:
      - content
      - stcgoal
```

### Configuration Fields

- `tag`: The unique identifier for the prompt.
- [`description`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fjgi%2FDropbox%2Fg%2Fpractice_orpheuspy%2Fsrc%2Fjghfmanager%2Fsetup.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A6%2C%22character%22%3A4%7D%7D%5D%2C%22a69b3260-2643-4c48-9fac-b79e1c1a3aed%22%5D "Go to definition"): A brief description of the prompt's purpose.
- `variables`: A list of variables required by the prompt.

## Capabilities

- **Prompt Management**: Easily pull prompt templates from the LangSmith Hub.
- **CLI Tool**: Use the `jhub` CLI to list and manage prompts.
- **YAML Configuration**: Define supported prompts and their descriptions in a YAML file for easy integration with agents.

## Supported Prompts

Here are a few example prompts and their information:

| Prompt Tag                     | Description                                                        | Variables                        |
|--------------------------------|--------------------------------------------------------------------|----------------------------------|
| jgwill/cmpenghelperbeta        | Create a ChatMusician Musical Inference Request                    | creation_name, seq_name, musical_notes |
| jgwill/json2yaml               | Simple Tool to convert input JSON into YAML                        | None                             |
| jgwill/sfcp                    | Shift focus from technical-aspect to creative practitionner perspective | content                          |
| jgwill/stcgoalsfcp             | Shift focus from technical-aspect to creative practitionner perspective with a structured user goal in the inputs | content, stcgoal                 |

## Conclusion

The `jgwillhub` module simplifies the process of managing and using prompt templates from the LangSmith Hub. With its CLI tool and YAML configuration support, it provides a flexible and powerful way to integrate prompts into your applications.

