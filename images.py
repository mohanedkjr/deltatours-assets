import os
import json

def generate_json_for_images(main_folder):
    # Loop through each subfolder in the main folder
    for subfolder in os.listdir(main_folder):
        subfolder_path = os.path.join(main_folder, subfolder)
        
        # Ensure it's a directory
        if os.path.isdir(subfolder_path):
            # Get list of images (JPEG files only)
            image_files = sorted([
                file for file in os.listdir(subfolder_path) 
                if file.lower().endswith((".jpeg", ".jpg", ".png"))
            ])

            # JSON structure
            images_data = {"images": image_files}

            # Save JSON file inside the subfolder
            json_path = os.path.join(subfolder_path, "images.json")
            with open(json_path, "w", encoding="utf-8") as json_file:
                json.dump(images_data, json_file, indent=2)

            print(f"Created: {json_path}")

# Usage: Replace 'your_main_folder_path' with the actual path
main_folder = "C:/Users/mohan/Downloads/ImageAssistant_Batch_Image_Downloader/sites.google.com"
generate_json_for_images(main_folder)
