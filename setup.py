from setuptools import setup, find_packages

setup(
    name="notetaker",
    version="0.3_a",
    packages=find_packages(),
    install_requires=[
        "PyQt5>=5.15.11",
        "pyyaml",
    ],
    entry_points={
        'console_scripts': [
            'notetaker=main:main',
        ],
    },
    author="citizen",
    author_email="communotron@protonmail.com",
    description="Simple note taking utility.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/communotron/notetaker",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License version 3"
        "Operating System :: POSIX :: Linux",
    ],
    python_requires=">=3.6",
    include_package_data=True,
)
