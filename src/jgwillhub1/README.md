# jgwillhub

This project is a Python module that wraps the functionality of pulling prompts from the 'langchainhub' module for the user 'jgwill'.

## Installation

To install the `jgwillhub` module, you can use pip:

```shell
pip install jgwillhub
```

## Usage

### CLI Tool: jhub

The `jhub` command-line tool allows you to get a list of prompts from the 'langchainhub' for the user 'jgwill'.

To use the `jhub` tool, simply run the following command:

```shell
jhub
```

This will display a list of prompts from the 'langchainhub' for the user 'jgwill'.

### Module: jgwillhub

The `jgwillhub` module provides a function `get_prompt_list` that allows you to retrieve prompts from the 'langchainhub' for the user 'jgwill'.

Here is an example of how to use the `get_prompt_list` function:

```python
from jgwillhub import get_prompt_list

prompt_list = get_prompt_list()
print(prompt_list)
```

This will print a list of prompts retrieved from the 'langchainhub' for the user 'jgwill'.

## Configuration

The `jgwill-hub.yml` file can be used to configure the supported prompts with their descriptions and capabilities to expose to agents. Please refer to the YAML file for more information.

## Testing

To run the unit tests for the `jgwillhub` module, you can use the following command:

```shell
python -m unittest discover tests
```

## Dependencies

The project requires the following dependencies, which can be installed using the `requirements.txt` file:

```
langchainhub
```

Please make sure to install these dependencies before using the `jgwillhub` module.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
```

Please let me know if you need help with anything else.