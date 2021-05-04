# -*-coding:utf-8-*-

import os
from ftplib import FTP


class FtpClient(object):
    client = FTP()

    def __init__(self, host, port=21):
        # self.ftp.encoding='GBK'
        FtpClient.client.connect(host, port)

    def login(self, username, passwd):
        self.client.set_debuglevel(2)
        self.client.login(username, passwd)
        print(self.ftp.welcome)

    def download_file(self, local_path, remote_path, filename):
        os.chdir(local_path)
        self.client.cwd(remote_path)
        self.client.nlst()
        file_handler = open(filename, 'wb').write
        self.client.retrbinary('RETR %s' % os.path.basename(filename), file_handler, blocksize=1024)

    def close(self):
        self.client.set_debuglevel(0)  # 关闭调试
        self.client.quit()
