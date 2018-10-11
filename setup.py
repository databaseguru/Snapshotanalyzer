from setuptools import setup

setup(
    name = 'Snapshotanalyzer-30000',
    version = '0.1',
    author = "Kalpit Parikh",
    author_email = "parikh.kalpit@gmail.com",
    description = "Snapshotanalyzer 30000 is a tool to manage AWS snapshots",
    license = "GPLv3+",
    packages = ['shotty'],
    url = "https://github.com/databaseguru/Snapshotanalyzer",
    install_requires = [
        'click',
        'boto3'
    ],
    entry_points = '''
        [console_scripts]
        shotty=shotty.shotty:cli
        ''',
)
