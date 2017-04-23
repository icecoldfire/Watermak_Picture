from distutils.core import setup


def readme():
    with open('README.rst') as f:
        return f.read()

setup(
    name='watermark_picture',
    version='1.0.0',
    packages=['watermark_picture'],
    url='',
    license='MIT License',
    author='Stijn Goethals',
    author_email='stijn.goethals@outlook.be',
    description='Places an watermark on the bottom right side of an picture',
    long_description=readme(),
    install_requires=[
        'tqdm', 'pillow',
      ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Topic :: Multimedia :: Graphics :: Editors',
    ],
    keywords=["PILLOW", "Watermark", "Image", "PIL"],
    include_package_data=True,
    zip_safe=True,
)