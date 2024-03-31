#!/usr/bin/env python
# coding: utf-8

# In[1]:


from setuptools import setup, find_packages

setup(
    name='HW09',
    version='0.1',
    packages=find_packages(),
    description='A brief description of your package',
    long_description='A longer description of your package',
    author='Emmanuel Leonce',
    author_email='deoleojr016@gmail.com',
    url='https://github.com/deoleojr/HW09.git',
    install_requires=[
        # Add your package dependencies here, e.g.,
        # 'numpy>=1.18.1',
        # 'pandas>=1.0.3',
    ],
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.org/classifiers/
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)


# In[ ]:




