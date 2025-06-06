from setuptools import setup, find_packages

setup(
    name='text_in_pattern',
    version='1.0.0',  
    author='Adarsh Kumar',
    author_email='ethycaladarsh@example.com',
    description='It is a simple Python library that transforms user input text into a stylized pattern using a user-defined symbol.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ethicaladarsh/text_in_pattern', 
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[],
    include_package_data=True,
)
