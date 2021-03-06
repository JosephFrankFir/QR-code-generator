import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="qrgc",
    version="0.0.3",
    author=" JosephFrankFir ",
    author_email="josephfir@protonmail.com",
    description="Very basic library for QR code generator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JosephFrankFir/QR-code-generator",
    project_urls={
        "Bug Tracker": "https://github.com/JosephFrankFir/QR-code-generator/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    keywords='QR code',
)
