Works with any OpenAI or Anthropic model. It also works with any model from this site: https://deepinfra.com/
- Anthropic models have been buggy when being target models (still working on fixing this). The other sources work as targets

There are some of my initial results in the pre_attack_result and attack_result folders

My notes from my first tests just seeing if the creds and the system worked
- It works with Openai-4o and in my one test produced a violative answer
- Claude 3.5 Sonnet refuses to generate an attack plan
- WizardLM-2-8x22B is pretty slow, especially when coming up with the attack plan but it produced good (violative) content

Also something we should look at, it seems the judge.py is hardcoded to produce scores based on OpenAI's policy. So maybe we change them to align with how we are going to benchmark (or maybe we don't and we jusdge all models against OAI policy).