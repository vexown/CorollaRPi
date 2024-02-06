import picamera
import sys
import tty
import termios
import threading

def start_camera_preview():
	with picamera.PiCamera() as camera:
		camera.rotation = 270
		camera.hflip = True
		camera.start_preview()
		camera.preview.fullscreen = True
		camera.preview.alpha = 255
		
		print("Press any key to close camera preview.")
		sys.stdin.read(1)

def keypress():
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
	
	camera_thread.join()


