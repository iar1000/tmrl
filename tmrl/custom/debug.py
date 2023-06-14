import subprocess
from PIL import Image
import io


result = subprocess.run(['xdotool', 'search', '--name', 'tmrl-pius'],
                                        capture_output=True)
# window_ids = result.stdout.strip().split('\n')

result = subprocess.run(['import', '-window', str(39845898), '-silent', '-resize', '1920x1080', 'png:-'],
                                        capture_output=True, check=True)
print(len(result.stdout))
image = Image.open(io.BytesIO(result.stdout))
image.show()  

result = subprocess.run(['import', '-window', str(39845898), '-silent', '-resize', '64x164', 'png:-'],
                                        capture_output=True, check=True)
print(len(result.stdout))
image = Image.open(io.BytesIO(result.stdout))
image.show() 