from setuptools import setup, find_packages

version = '2.0'

setup(name='Products.CMFEditions',
      version=version,
      description="Versioning for Plone",
      long_description=open("README.txt").read() + '\n' +
                       open("CHANGES.txt").read(),
      classifiers=[
        'Framework :: Plone',
        'Framework :: Zope2',
      ],
      keywords='Versioning Plone',
      author='CMFEditions contributers',
      author_email='collective-versioning@lists.sourceforge.net',
      url='http://plone.org/products/cmfeditions',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['Products'],
      include_package_data=True,
      zip_safe=False,
      extras_require=dict(
        test=[
            'zope.testing',
            'zope.app.testing',
            'Products.CMFDynamicViewFTI',
            'Products.PloneTestCase',
        ]
      ),
      install_requires=[
        'setuptools',
        'zope.i18nmessageid',
        'zope.interface',
        'Products.Archetypes',
        'Products.CMFCore',
        'Products.CMFDiffTool',
        'Products.CMFUid',
        'Products.GenericSetup',
        'Products.ZopeVersionControl',
        'Acquisition',
        'DateTime',
        'transaction',
        'ZODB3',
        'Zope2',
      ],
      )
