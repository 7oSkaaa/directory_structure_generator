from setuptools import setup, find_packages


setup(
    name="directory_structure_generator",
    version="1.0.2",
    author="Ahmed Hossam",
    author_email="ahmed.7oskaa@gmail.com",
    description="This script is used to generate a list of the project structure in a markdown format. It is useful for README.md files.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/7oSkaaa/directory_structure_generator",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": ["directory_structure_generator=directory_structure_generator.__main__:main"]
    },
    python_requires=">=3.6",
    install_requires=["argparse"],
    include_package_data=True,
    zip_safe=False,
)
