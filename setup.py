from setuptools import setup, find_packages

with open("README.md", "r") as r:
    desc = r.read()

setup(
    name="autotsk",            
    version="1.0.0",
    author="5f0",
    url="https://github.com/5f0ne/autotsk",
    description="Automatically creates mmls, fsstat and fls results for image files",
    classifiers=[
        "Operating System :: OS Independent ",
        "Programming Language :: Python :: 3 ",
        "License :: OSI Approved :: MIT License "
    ],
    license="MIT",
    long_description=desc,
    long_description_content_type="text/markdown",
    package_dir={"": "src"},
    packages=find_packages(where='src'),
    include_package_data=True,
    install_requires=[
   
    ],
     entry_points={
        "autotsk": [
            "autotsk = autotsk.__main__:main"
        ]
    }
)
