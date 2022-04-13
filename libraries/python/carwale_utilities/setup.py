import setuptools

if __name__ == "__main__":
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()

    setuptools.setup(
        name='carwale_utilities',
        version='0.0.1',
        author='CarWale',
        author_email='',
        description='Python utilities for CarWale',
        long_description=long_description,
        long_description_content_type="text/markdown",
        url='',
        license='MIT',
        packages=['utilities'],
        install_requires=['boto3>=1.21.39', 'PyYAML>=6.0', 'consulate>=0.6.0'],
    )
