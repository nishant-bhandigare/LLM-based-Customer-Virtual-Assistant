from transformers import GPT2LMHeadModel, GPT2Tokenizer, Trainer, TrainingArguments
from datasets import load_dataset

# Load the custom dataset
ds = load_dataset("argilla/customer_assistant")

# Check the structure of the dataset
print(ds)

# Define the tokenizer and tokenize function
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

def tokenize_function(examples):
    return tokenizer(examples["user-message"], truncation=True, max_length=512)

# Tokenize the dataset using the GPT-2 tokenizer
tokenized_ds = ds.map(tokenize_function)

# Define the GPT-2 model and training arguments
model = GPT2LMHeadModel.from_pretrained("gpt2")
training_args = TrainingArguments(
    output_dir="./gpt2-finetuned",
    overwrite_output_dir=True,
    num_train_epochs=3,
    per_device_train_batch_size=4,
    save_steps=10_000,
    save_total_limit=2,
    logging_dir="./logs",
)

# Define a Trainer object and fine-tune the model
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_ds["train"],
)

trainer.train()
