# coding: utf-8
from setuptools import setup, find_packages
from usergroup_segment import __version__


REQUIREMENTS = [
    'aldryn-segmentation',
    'django-cms'
]

CLASSIFIERS = [
    'Development Status :: 2 - Pre-Alpha',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
]

setup(
    name='aldryn-country-segment',
    version=__version__,
    description='Django CMS and aldryn-segmentation segment by user group plugin',
    author='ELCODO',
    author_email='info@elcodo.pl',
    url='https://github.com/elcodo/djangocms-usergroup-segment',
    packages=find_packages(),
    package_data={
        "usergroup_segment": [
            "locale/*/LC_MESSAGES/*",
        ],
    },
    license='LICENSE.txt',
    platforms=['OS Independent'],
    install_requires=REQUIREMENTS,
    classifiers=CLASSIFIERS,
    include_package_data=True,
    zip_safe=False
)
