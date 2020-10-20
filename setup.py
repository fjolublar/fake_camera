from distutils.core import setup
setup(
  name = 'fake_camera',         # How you named your package folder (MyLib)
  packages = ['fake_camera'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'A Camera Simulator. It creates a moving image in the screen.',   # Give a short description about your library
  author = 'Fjolublar',                   # Type in your name
  url = 'https://github.com/fjolublar/fake_camera',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/fjolublar/fake_camera/archive/v_0.1.tar.gz',    # I explain this later on
  keywords = ['Fake Camera', 'Moving Image', 'Camera Simulator'],   # Keywords that define your package best
  install_requires=[            
          'Pillow',
          'numpy',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3.7',
  ],
)
