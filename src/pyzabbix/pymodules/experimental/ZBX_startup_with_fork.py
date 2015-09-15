##
## Zabbix-Python startup procedures
##


import imp,os,time

def main(cfg_path):
    import traceback
    print "Python-Zabbix extention is initialized"
    if os.fork() == 0:
	while True:
		f = open("/tmp/metrik.1","a")
		f.write("%s\n"%time.ctime())
		f.close()
		time.sleep(5)
