# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

import versioneer

with open('README.rst', 'rb') as f:
    readme = str(f.read())

with open('license.txt', 'rb') as f:
    license = str(f.read())


pkgs = find_packages('src', exclude=['data'])
print('found these packages:', pkgs)

schema_dir = 'data'

setup_args = {
    'name': 'pynwb',
    'version': versioneer.get_version(),
    'cmdclass': versioneer.get_cmdclass(),
    'description': 'Package for working with Neurodata stored in the NWB format',
    'long_description': readme,
    'author': 'Andrew Tritt',
    'author_email': 'ajtritt@lbl.gov',
    'url': 'https://github.com/NeurodataWithoutBorders/pynwb',
    'license': license,
    'install_requires':
    [
        'numpy',
        'h5py',
        'ruamel.yaml',
        'python-dateutil',
        'six',
        'requests'
    ],
    'packages': pkgs,
    'package_dir': {'': 'src'},
    'package_data': {'pynwb': ["%s/*.yaml" % schema_dir, "%s/*.json" % schema_dir]},
    'classifiers': [
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: BSD License",
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",
        "Operating System :: Unix",
        "Topic :: Scientific/Engineering :: Medical Science Apps."
    ],
    'keywords': 'Neuroscience '
                'python '
                'HDF '
                'HDF5 '
                'cross-platform '
                'open-data '
                'data-format '
                'open-source '
                'open-science '
                'reproducible-research '
                'PyNWB '
                'NWB '
                'NWB:N '
                'NeurodataWithoutBorders',
}

if __name__ == '__main__':
    setup(**setup_args)
