python: python.c
	gcc -g -fPIC -shared -Xlinker -export-dynamic -o python.so python.c -I~/zabbix-2.2.4/include -I/usr/include/libxml2 -I/usr/include/python2.6 -lpython2.6
config: python.c
	echo -n "PYTHONPATH=" > python.cfg
	python -c "import sys; print ':'.join(sys.path)" >> python.cfg
	echo -n "PYTHONLIB=" >> python.cfg
	ldd `type -p python`|grep python|cut -f 3 -d " " >> python.cfg
	

