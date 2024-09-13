import setuptools

setuptools.setup(
    name='Resonnance',
    version='001',
    description='Ai Project',
    author='team Out of the Box',
    packages=setuptools.find_packages(),
    setup_requires=['nltk', 'joblib','click','regex','sqlparse','setuptools'],
)