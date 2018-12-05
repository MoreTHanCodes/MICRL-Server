import argparse
import os
import time


class Updater(object):
    def __init__(self, server_num=1):
        self.server_num = server_num
        self.ip = self.get_ip()
        self.stop_num = 0
        self.pull()
        self.write_ip()
        self.push()

    def get_ip(self):
        ip_str = os.popen("ifconfig -a | awk '/wlx/{nr[NR]; nr[NR+1]}; NR in nr' | grep inet | grep -v inet6 | awk '{print $2}'").read().splitlines()[0]
        return ip_str[5:20]

    def _restart_wifi_module(self):
        os.system("nmcli networking off")
        print "Shut down WIFI ..."
        time.sleep(3)
        os.system("nmcli networking on")
        print "Restart WIFI ..."

    def run(self):
        while True:
            try:
                ip = self.get_ip()
                if ip != self.ip:
                    print self.ip, " --> ", self.get_ip()
                    self.ip = self.get_ip()
                    self.update_ip()
                else:
                    print "IP: ", self.ip
                self.stop_num = 0
            except:
                print "Cannot get IP ...."
                self.stop_num += 1
                if self.stop_num > 5:
                    self._restart_wifi_module()
                    self.stop_num = 0
            
            time.sleep(10)

    def update_ip(self):
        self.pull()
        self.write_ip()
        self.push()

    def write_ip(self):
        f = open("README.md", "r+")
        flist = f.readlines()
        flist[2 * self.server_num] = self.ip + "\n"
        f = open("README.md", "w+")
        f.writelines(flist)
        f.close()

    def pull(self):
        os.system("git pull")

    def push(self):
        os.system("git add -A")
        os.system("git commit -a --allow-empty-message -m ''")
        os.system("git push -u origin gh-pages")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--server_num', default=1, type=int
    )
    args = parser.parse_args()
    updater = Updater(args.server_num)
    updater.run()
