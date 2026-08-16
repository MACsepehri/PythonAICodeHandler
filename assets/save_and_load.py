import json
import os

def load(name="main", cur_list=None):
    if cur_list is None:
        cur_list = []
    
    path = f"data/{name}.json"
    
    if not os.path.exists(path):
        print(f"File {path} not found. Starting with empty list.")
        return cur_list
    
    try:
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)
            
            if not isinstance(data, dict) or "list" not in data:
                print(f"Invalid structure in {path}. Expected {{'list': [...]}}")
                return cur_list
            
            existing_set = set(cur_list)
            added_count = 0
            
            for item in data["list"]:
                if item not in existing_set:
                    cur_list.append(item)
                    existing_set.add(item)
                    added_count += 1
            
            if added_count > 0:
                print(f"Loaded {added_count} new items from {path}")
            else:
                print(f"No new items to load from {path}")

            return cur_list
            
    except json.JSONDecodeError as e:
        print(f"Error: json file is empyty; path: {path}: {e}")
        return cur_list
    except Exception as e:
        print(f"Error loading {path} file: {e}")
        return cur_list