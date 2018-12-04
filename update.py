import argparse
import os
import time


class Updater(object):
    def __init__(self, server_num=1):
        self.server_num = server_num
        self.ip = self.get_ip()
        self.pull()
        self.write_ip()
        self.push()

    def get_ip(self):
        ip_str = os.popen("ifconfig -a | grep inet | grep -v inet6 | grep -v 127.0.0.1 | grep 175.159. | awk '{print $2}'").read().splitlines()[0]
        return ip_str[5:20]

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
            except:
                print "Cannot get IP ...."
            
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
