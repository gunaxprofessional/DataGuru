from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: OS Independent',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='DataGuru',
    version='0.0.1',
    description='The "DataGuru" library is a comprehensive Python toolkit designed to simplify common data analysis tasks for data science students and practitioners. With a focus on ease of use and efficiency, this library provides a range of functions to streamline your data analysis workflow.',
    long_description=open('README.txt').read() + '\n\n' +
    open('CHANGELOG.txt').read(),
    long_description_content_type='text/markdown',
    url='',
    author='Guna M',
    author_email='guna0professional@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords='data analysis',
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=['plotly', 'pandas', 'numpy', 'scipy']
)
