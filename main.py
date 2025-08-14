import os
import json
model_dir = r"e:\customer_support\local_customer_support_model"
data_path = os.path.join(model_dir, r"E:\customer_support\local_customer_support_model\customer_support_data.jsonl")
modelfile_path = os.path.join(model_dir, "modelfile")
default_reply = "I'm here to help with customer support only. Please ask about your order or account."
with open(modelfile_path, "r", encoding="utf-8") as f:
    for line in f:
        if default_reply in line:
            break
with open(data_path, "r", encoding="utf-8") as f:
    dataset = [json.loads(line) for line in f if line.strip()]
def get_response(user_input):
    for entry in dataset:
        if user_input.lower() in entry["prompt"].lower():
            return entry["response"]
    return default_reply
if __name__ == "__main__":
    print("Customer Support Assistant")
    print("Ask a question or type 'exit' to quit.")
    while True:
        user_input = input("> ")
        if user_input.lower() == "exit":
            break
        print(get_response(user_input))