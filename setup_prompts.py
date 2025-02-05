import yaml


def load_prompts(filename="./prompts.yml"):
    with open(filename) as f:
        prompts = yaml.safe_load(f)

    for k, v in prompts.items():
        temp = v.split("\n")
        prompts[k] = ''.join(temp)

    return prompts


if __name__ == "__main__":
    prompt_dict = load_prompts()
    print(prompt_dict)