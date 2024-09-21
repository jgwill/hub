import langchainhub

def get_prompt_list():
    # Use langchainhub module to pull prompts from 'langchainhub' for user 'jgwill'
    prompts = langchainhub.get_prompts(user='jgwill')
    return prompts

def jhub():
    # CLI tool implementation to get a list of prompts from 'langchainhub' for user 'jgwill'
    prompts = get_prompt_list()
    for prompt in prompts:
        print(prompt)

if __name__ == "__main__":
    jhub()