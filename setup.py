from setuptools import setup, find_packages

requirements = [
    'torch',
    'numpy',
    'opencv-python',
    'scipy',
    'numba',
    'librosa==0.8.1',
    'tqdm'
]

setup(
    name='wav2lip',
    version='1.0',

    description="Python package for Wav2Lip implementation (https://github.com/Rudrabha/Wav2Lip)",

    url='https://github.com/ReneLutz/Wav2Lip',
    author='Rene Lutz',

    packages=find_packages(),

    python_requires='>=3',
    install_requires=requirements,

    classifiers=[
        'Intended Audience :: Developers',

        'Programming Language :: Python',
        'Programming Language :: Python :: 3.8',
    ]
)