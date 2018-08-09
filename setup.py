import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	name="autoscaling_lifecycle",
	version="0.0.1",
	author="Jan Schumann",
	author_email="js@schumann-it.com",
	description="A library to handle aws autoscaling lifecycle events",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/7NXT/infrstructure",
	packages=setuptools.find_packages(),
	classifiers=(
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	),
)