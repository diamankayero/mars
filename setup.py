from setuptools import setup, find_packages

setup(
        name="mars",
        version="0.0.1",
        author="Yéro",
        author_email="diamanka.tck@gmail.com",
        url="",
        description="Un package pour créer des réseaux de neurones denses",
        packages=find_packages(),
        readme = "README.md",
        install_requires = ["numpy >= 2.2.2"],
        python_requires=">=3.12",
        classifiers=[
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        ],
)