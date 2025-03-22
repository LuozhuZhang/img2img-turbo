import os
import subprocess
from pathlib import Path

def ensure_output_dir(output_dir):
    """Ensure output directory exists"""
    Path(output_dir).mkdir(parents=True, exist_ok=True)

def process_images(input_dir, output_dir):
    """Process all images in input_dir and save to output_dir"""
    # Create output directory if not exists
    ensure_output_dir(output_dir)
    
    # Get all image files
    image_extensions = ('.png', '.jpg', '.jpeg', '.PNG', '.JPG', '.JPEG')
    image_files = [f for f in os.listdir(input_dir) if f.endswith(image_extensions)]
    
    # Process each image
    for img_file in image_files:
        input_path = os.path.join(input_dir, img_file)
        print(f"Processing: {input_path}")
        
        # Run inference command
        cmd = [
            "python", 
            "src/inference_unpaired.py",
            "--model_name", "day_to_night",
            "--input_image", input_path,
            "--output_dir", output_dir
        ]
        
        try:
            subprocess.run(cmd, check=True)
            print(f"Successfully processed: {img_file}")
        except subprocess.CalledProcessError as e:
            print(f"Error processing {img_file}: {e}")

def main():
    # Define paths
    hk_input_dir = "lz/hk/images"
    sg_input_dir = "lz/singapore/images"
    hk_output_dir = "outputs/hk"
    sg_output_dir = "outputs/sg"
    
    # Process Hong Kong images
    print("\nProcessing Hong Kong images...")
    process_images(hk_input_dir, hk_output_dir)
    
    # Process Singapore images
    print("\nProcessing Singapore images...")
    process_images(sg_input_dir, sg_output_dir)

if __name__ == "__main__":
    main() 