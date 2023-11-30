from setuptools import setup, find_packages


setup(name='ssqaapitest',
      version='1.0',
      description="Practice API testing",
      author='Yerdos',
      author_email='erdos.sadvakasov@gmail.com',
      packages=find_packages(),
      zip_safe=False,
      install_requires=[
          "pytest==7.4.3",
          "pytest-html==2.1.1",
          "requests==2.23.0",
          "requests-oauthlib==1.3.0",
          "PyMySQL==0.9.3",
          "WooCommerce==2.1.1",
      ]
      )