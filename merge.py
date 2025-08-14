import os
import shutil
base_dir = r"e:\customer_support"
data_file = os.path.join(base_dir, "customer_support_data.jsonl")
model_file = os.path.join(base_dir, "modelfile")
target_dir = os.path.join(base_dir, "local_customer_support_model")
os.makedirs(target_dir, exist_ok=True)
shutil.copy2(data_file, os.path.join(target_dir, "customer_support_data.jsonl"))
shutil.copy2(model_file, os.path.join(target_dir, "modelfile"))
print(f"Files merged into {target_dir}")