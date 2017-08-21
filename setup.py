from setuptools import setup


setup(
    name='Flask-RedisSession',
    version='0.1',
    url='https://github.com/bingtel/flask_redissession',
    license='BSD',
    author='bingtel',
    author_email='bingtelwang@163.com',
    description='server-side session support to your Flask application',
    long_description=__doc__,
    packages=['flask_redissession'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask>=0.8'
    ],
    test_suite='test_session',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)