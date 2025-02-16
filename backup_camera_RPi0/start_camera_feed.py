import sys
import tty
import termios
import threading
import subprocess

def start_camera_preview():
    try:
        print("Starting camera preview...")
        subprocess.run(["libcamera-hello", "--hflip", "--vflip"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error starting camera: {e}")

def keypress():
    """ Wait for a keypress to exit the program. """
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        key = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return key

if __name__ == "__main__":
    camera_thread = threading.Thread(target=start_camera_preview)
    camera_thread.start()

    print("Press any key to exit.")
    keypress()

    print("Stopping camera preview...")
    camera_thread.join()
