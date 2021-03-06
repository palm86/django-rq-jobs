import os

from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-rq-jobs',
    version='0.1.5',
    author='Ilan Steemers',
    author_email='koed00@gmail.com',
    packages=['django_rq_jobs'],
    url='https://github.com/koed00/django-rq-jobs',
    license='MIT',
    description='Provides scheduled jobs from the Django Admin using Django-RQ',
    long_description=README,
    include_package_data=True,
    install_requires=['django>=1.7', 'django-rq>=0.8.0', 'arrow>=0.5.4'],
    test_suite='django_rq_jobs.tests.runtests.runtests',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)