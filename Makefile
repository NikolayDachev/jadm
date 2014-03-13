all:
     python setup.py build

install:
     python setup.py install

clean:
     python setup.py clean
     rm -fr build

test:
     python setup.py test
