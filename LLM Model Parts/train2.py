from transformers import GPT2LMHeadModel, GPT2Tokenizer, Trainer, TrainingArguments
from datasets import load_dataset

# Load the Hugging Face LLM dataset
dataset = load_dataset("DR-DRR/Medical_Customer_care")

# Load the pre-trained GPT-2 model and tokenizer
model_name = "gpt2"  # You can use different pre-trained models like "gpt2-medium", "gpt2-large", etc.
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# # Define training arguments
# training_args = TrainingArguments(
#     output_dir="./output",
#     overwrite_output_dir=True,
#     num_train_epochs=3,  # Adjust the number of training epochs as needed
#     per_device_train_batch_size=4,
#     save_steps=1000,
#     save_total_limit=2,
# )

# # Define Trainer object
# trainer = Trainer(
#     model=model,
#     tokenizer=tokenizer,
#     args=training_args,
#     train_dataset=dataset["train"],  # Assuming you have a split for training in your dataset
# )

# # Fine-tune the model
# trainer.train()

print(f"Train dataset size: {len(dataset['train'])}")
# print(f"Test dataset size: {len(dataset['test'])}")
