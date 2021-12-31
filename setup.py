from setuptools import setup

setup(
    name='autograde-viz',
    version='0.0.1',    
    description='D3 Autograding Utilities',
    url='https://github.com/matthewdhull/autograde-viz',
    author='Matthew Hull',
    author_email='matthewdhull@gmail.com',
    license='BSD 2-clause',
    packages=['autograde-viz'],
    install_requires=['pandas',
                      'numpy',
                      'selenium',                     
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 3.7',
    ],
)