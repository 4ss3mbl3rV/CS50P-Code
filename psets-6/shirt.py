import sys
from os.path import splitext
from PIL import Image, ImageOps

def main():
  check_cmd_arg()
  # open image
  try:
    imagefile =Image.open(sys.argv[1])
  except FileNotFoundError:
    sys.exit('Input does no exist')
  # open shirt
  shirtfile = Image.open('shirt.png')
  # display size of shirt 
  size = shirtfile.size
  # resize to fit the picture
  muppets = ImageOps.fit(imagefile, size)
  # paste the shirt to muppets photo
  muppets.paste(shirtfile, shirtfile)
  # save file
  muppets.save(sys.argv[2])

def check_cmd_arg():
  if len(sys.argv) < 3:
    sys.exit('Too few command-line arguments')
  elif len(sys.argv) > 3:
    sys.exit('Too many command-line arguments')
  else:
    file1 = splitext(sys.argv[1])
    file2 = splitext(sys.argv[2])
    chck_ext_file(file1[1], file2[1])

def chck_ext_file(file1, file2):
  if not file1 in ['.jpg', '.jpeg', '.png']:
    sys.exit('Invalid input')
  if not file2 in ['.jpg', '.jpeg', '.png']:
    sys.exit('Invalid output')
  if not file1.lower() == file2.lower():
    sys.exit('Input and output have different extensions')
  return



if __name__ == '__main__':
  main()