from setuptools import setup, find_packages

version = '1.1'

setup(name='policy.zp5343',
      version=version,
      description="A policy for zone de police 5343",
      long_description=open("README.rst").read() + "\n" +
                       open("CHANGES.txt").read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='',
      author_email='',
      url='http://svn.plone.org/svn/collective/',
      license='gpl',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['policy'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Plone',
          'Products.LinguaPlone',
          'Products.PloneFormGen',
          'cirb.zopemonitoring',
          'plonetheme.zp5343',
          'collective.easyslider',
          'collective.galleriffic',
          'collective.js.galleriffic',
          'webcouturier.dropdownmenu',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
