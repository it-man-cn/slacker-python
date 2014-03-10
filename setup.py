
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

long_desc=open('README.rst','r').read()

setup(name="slacker-python",
      version="0.1.3",
      author="Sun Ning",
      author_email="sunng@about.me",
      description="python client of slacker RPC",
      long_description=long_desc,
      url="http://github.com/sunng87/slacker-python",
      license='mit',
      packages=['slacker'],
      install_requires=['gevent==1.0', 'pyclj==0.2.1'],
      classifiers=['Development Status :: 3 - Alpha',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Topic :: Software Development',
            'Programming Language :: Python',
            'Operating System :: OS Independent']
    )

