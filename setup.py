import setuptools

# description
with open("README.md", "r") as f:
  long_description = f.read()

setuptools.setup(
    
    name="pyperties",
    version="0.0.1",
    author="larry.zzn",
    author_email="larry.zzn@gmail.com",
    description="a simple .properties file parser",
    long_description=long_description,
    long_description_content_type="text/markdown",
    
    
    url="https://github.com/larryonline/pyperties",
    
    py_modules=['pyperties'],

    packages=setuptools.find_packages(),
    
    classifiers=[
      "Development Status :: 1 - Planning"
      "Programming Language :: Python :: 3",
      "Operating System :: OS Independent",
    ],

    exclude_package_data= {
      
    }
)