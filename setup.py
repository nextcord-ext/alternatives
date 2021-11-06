import re
import setuptools


classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: Apache Software License",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3 :: Only",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: Implementation :: CPython",
    "Topic :: Software Development",
    "Topic :: Software Development :: Libraries",
    "Topic :: Software Development :: Libraries :: Python Modules",
]

with open("requirements.txt") as stream:
    install_requires = stream.read().splitlines()

packages = [
    "nextcord.ext.alternatives",
]

project_urls = {
    "Issue Tracker": "https://github.com/nextcord-ext/alternatives/issues",
    "Source": "https://github.com/nextcord-ext/alternatives",
}

_version_regex = r"^version = ('|\")((?:[0-9]+\.)*[0-9]+(?:\.?([a-z]+)(?:\.?[0-9])?)?)\1$"

with open("nextcord/ext/alternatives/__init__.py") as stream:
    match = re.search(_version_regex, stream.read(), re.MULTILINE)

version = match.group(2)

if match.group(3) is not None:
    try:
        import subprocess

        process = subprocess.Popen(["git", "rev-list", "--count", "HEAD"], stdout=subprocess.PIPE)
        out, _ = process.communicate()
        if out:
            version += out.decode("utf-8").strip()

        process = subprocess.Popen(["git", "rev-parse", "--short", "HEAD"], stdout=subprocess.PIPE)
        out, _ = process.communicate()
        if out:
            version += "+g" + out.decode("utf-8").strip()
    except (Exception) as e:
        pass

setuptools.setup(
    author="nextcord-ext",
    classifiers=classifiers,
    description="A nextcord extension with additional and alternative features, Forked from discord-ext-alternatives",
    install_requires=install_requires,
    license="Apache Software License",
    name="nextcord-ext-alternatives",
    packages=packages,
    project_urls=project_urls,
    url="https://github.com/nextcord/alternatives",
    version=version,
)
