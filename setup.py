from setuptools import setup, find_packages

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setup(
    name='bot-assistant',
    version='0.2.9',
    description = "Bot Assistant for Python to avoid getting Blocked for Web Automation",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    license='MIT',
    author="Soukarja Dutta",
    author_email='soukarjadutta@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/soukarja/botAssistant_Python',
    keywords='example project',
    python_requires = ">=3.6",
    install_requires=[
          'selenium'
      ]

)