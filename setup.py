from setuptools import setup

# Read in dependencies from requirements.txt and make them requirements
# during package install
with open('requirements.txt') as f:
    dependencies = f.readlines()

setup(
    name='cube_robot',
    version='0.0.1',
    description='Hopefully solves a Rubix Cube with a robot.',
    long_description='Hopefully solves a Rubix Cube with a robot.',
    url='https://github.com/Wentworth-IEEE/IEEECubeRobot',
    author='IEEE Cube Robot Team',
    author_email='ieee@wit.edu',
    include_package_data=True,
    packages=['cube_robot'],
    install_requires=dependencies,
    entry_points={
        'console_scripts': ['cube_robot = cube_robot.__main__:main']
    }
)
