from setuptools import setup,find_packages


def Requirements():
    with open("requirements.txt","r") as f:
        r=f.readlines()
        r=[ i.replace("\n","") for i in r ]
        if "-e ." in r:
            r.remove("-e .")
            
        return r


setup(
    name="iris",
    author="Gajender",
    version="0.1",
    description="This is Test Project",
    packages=find_packages(),
    install_requires=Requirements()
)
