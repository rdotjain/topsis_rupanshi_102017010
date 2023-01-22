from distutils.core import setup
setup(
  name = 'topsis_rupanshi_102017010',
  packages = ['topsis_rupanshi_102017010'],
  version = '0.1',
  license='MIT',
  description = 'topsis_rupanshi_102017010 is a Python library for dealing with Multiple Criteria Decision Making(MCDM) problems by using Technique for Order of Preference by Similarity to Ideal Solution(TOPSIS).',
  author = 'Rupanshi Jain',
  author_email = 'rupanshijain45678@gmail.com',
  url = 'https://github.com/rdotjain/topsis_rupanshi_102017010',
  download_url = 'https://github.com/rdotjain/topsis_rupanshi_102017010/archive/refs/tags/v_01.tar.gz',
  keywords = ['topsis', 'MCDM', 'KEYWORDS'],
  install_requires=[            # I get to this in a second
          'pandas',
          'numpy',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)