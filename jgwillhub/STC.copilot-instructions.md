workspace /new python module called 'jgwillhub' wrapping the pull of prompts from 'langchainhub'.

example:

```python

from langchain import hub
tool_hub_tag="jgwill/cmpenghelperbeta"
prompt_template = hub.pull(tool_hub_tag)

```

capabilities:

* 'jhub', a cli with which you can get a list of prompts from user 'jgwill' in the 'langchainhub'
* support for a YAML setting file 'jgwill-hub.yml' in current directory or in homes defining the supported prompts with a description to expose their capabilities to agents (in various format such as a schema or markdown table with : prompt_tag, system_instruction, prompt_template, variables, prompt_goal, extra_info).  You make that data structure optimal for agents (it might means changing columns mentionned before.)
Here are few prompts tag and information for them to design this feature:

"jgwill/cmpenghelperbeta", Create a ChatMusician Musical Inference Request, variables: creation_name, seq_name, musical_notes

"jgwill/json2yaml", Simple Tool to convert input JSON into YAML.

"jgwill/sfcp", Shift focus from technical-aspect to creative practitionner perspective., variable:  content

"jgwill/stcgoalsfcp", Shift focus from technical-aspect to creative practitionner perspective with a structured user goal in the inputs., variable:  content, stcgoal
