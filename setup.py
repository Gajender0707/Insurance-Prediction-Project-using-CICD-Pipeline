from setuptools import setup,mypackages


def Requirements():
    with open("requirements.txt","r") as f:
        r=f.readlines()
        r=[ i.replace("\n","") for i in r ]
        return r


setup(
    name="iris",
    author="Gajender",
    version="0.1",
    description="This is Test Project",
    packages=mypackages(),
    install_requires=Requirements()
)

