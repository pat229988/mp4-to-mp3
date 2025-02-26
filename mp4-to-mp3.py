import os
import argparse
import subprocess

def convert_mp4_to_mp3(input_file, output_file=None):
    """
    Convert an MP4 video file to MP3 audio file using ffmpeg
    
    Args:
        input_file (str): Path to the input MP4 file
        output_file (str, optional): Path to the output MP3 file. 
                                    If not provided, uses the same name as input with .mp3 extension
    
    Returns:
        str: Path to the created MP3 file
    """
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Input file not found: {input_file}")
    
    # If output file not specified, use input filename with .mp3 extension
    if output_file is None:
        output_file = os.path.splitext(input_file)[0] + '.mp3'
    
    # Make sure output directory exists
    output_dir = os.path.dirname(output_file)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Run ffmpeg command to extract audio
    cmd = ['ffmpeg', '-i', input_file, '-q:a', '0', '-map', 'a', output_file]
    
    try:
        subprocess.run(cmd, check=True)
        return output_file
    except subprocess.CalledProcessError as e:
        raise Exception(f"FFmpeg conversion failed: {e}")

if __name__ == "__main__":
    # Set up command line argument parsing
    parser = argparse.ArgumentParser(description='Convert MP4 video files to MP3 audio')
    parser.add_argument('input', help='Input MP4 file path')
    parser.add_argument('-o', '--output', help='Output MP3 file path (optional)')
    
    args = parser.parse_args()
    
    # Perform the conversion
    try:
        output_path = convert_mp4_to_mp3(args.input, args.output)
        print(f"Conversion successful: {output_path}")
    except Exception as e:
        print(f"Error during conversion: {e}")