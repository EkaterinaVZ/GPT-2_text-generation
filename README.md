# GPT-2_text-generation
<a hreaf=text_generation>released at this page</a>
 https://huggingface.co/gpt2
Pretrained model on English language using a causal language modeling (CLM) objective. It was introduced in this paper and first released at this page.

Disclaimer: The team releasing GPT-2 also wrote a model card for their model. Content from this model card has been written by the Hugging Face team to complete the information they provided and give specific examples of bias.

<h2>Model description</h2>
GPT-2 is a transformers model pretrained on a very large corpus of English data in a self-supervised fashion. This means it was pretrained on the raw texts only, with no humans labelling them in any way (which is why it can use lots of publicly available data) with an automatic process to generate inputs and labels from those texts. More precisely, it was trained to guess the next word in sentences.

More precisely, inputs are sequences of continuous text of a certain length and the targets are the same sequence, shifted one token (word or piece of word) to the right. The model uses internally a mask-mechanism to make sure the predictions for the token i only uses the inputs from 1 to i but not the future tokens.

This way, the model learns an inner representation of the English language that can then be used to extract features useful for downstream tasks. The model is best at what it was pretrained for however, which is generating texts from a prompt.

<h2>Intended uses & limitations</h2>
You can use the raw model for text generation or fine-tune it to a downstream task. See the model hub to look for fine-tuned versions on a task that interests you.
