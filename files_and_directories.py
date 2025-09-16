from pathlib import Path
# path=Path("myPackage")
# print(path.exists()) chacking if exist

# path=Path("email")
# print(path.exists())

# print(path.mkdir()) #Creates folder

# print(path.rmdir())#Removes folder

path=Path()
# for file in path.glob('*.py'):
for file in path.glob('*'):
 print(file)