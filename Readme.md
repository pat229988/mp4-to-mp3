# MP4 to MP3 Converter

A simple command-line tool to convert MP4 video files to MP3 audio files using FFmpeg.

## Requirements

- Python 3.6 or higher
- FFmpeg (see installation instructions below)

## FFmpeg Installation

### Windows

1. Download FFmpeg from the official website: https://ffmpeg.org/download.html#build-windows
   - Alternatively, use the direct link to a Windows build: https://github.com/BtbN/FFmpeg-Builds/releases
2. Extract the ZIP file to a location on your computer (e.g., `C:\ffmpeg`)
3. Add FFmpeg to your PATH:
   - Right-click on "This PC" or "My Computer" and select "Properties"
   - Click on "Advanced system settings"
   - Click on "Environment Variables"
   - Under "System variables", find the "Path" variable, select it and click "Edit"
   - Click "New" and add the path to the `bin` folder (e.g., `C:\ffmpeg\bin`)
   - Click "OK" on all dialogs to save the changes
4. Verify the installation by opening Command Prompt and typing:
   ```
   ffmpeg -version
   ```

### macOS

Using Homebrew (recommended):
1. Install Homebrew if not already installed:
   ```
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
2. Install FFmpeg:
   ```
   brew install ffmpeg
   ```
3. Verify the installation:
   ```
   ffmpeg -version
   ```

### Ubuntu/Debian

1. Update your package list:
   ```
   sudo apt update
   ```
2. Install FFmpeg:
   ```
   sudo apt install ffmpeg
   ```
3. Verify the installation:
   ```
   ffmpeg -version
   ```

## Usage

### Basic Usage

To convert an MP4 file to MP3 with the same base filename:

```
python mp4-to-mp3.py input_video.mp4
```

This will create `input_video.mp3` in the same directory.

### Specify Output Filename

To specify a custom output filename:

```
python mp4-to-mp3.py input_video.mp4 -o custom_output.mp3
```

### Batch Processing

To convert multiple MP4 files, you can use a simple loop in your shell:

#### Windows (CMD):
```
for %f in (*.mp4) do python mp4-to-mp3.py "%f"
```

#### Windows (PowerShell):
```
foreach ($file in Get-ChildItem -Filter *.mp4) { python mp4-to-mp3.py $file.FullName }
```

#### macOS/Linux:
```
for f in *.mp4; do python mp4-to-mp3.py "$f"; done
```

## Options

- `input`: Path to the input MP4 file (required)
- `-o, --output`: Path to the output MP3 file (optional)

## Notes

- The script uses FFmpeg's default audio encoding settings with high quality (`-q:a 0`)
- If you encounter permission errors, make sure you have write access to the output directory
- For files with multiple audio tracks, only the first track will be extracted
