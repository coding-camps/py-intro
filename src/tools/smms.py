# -*- coding: utf-8 -*-

import json

import requests


class SMMS(object):
    base_url = r'https://sm.ms/api/v2'

    # init
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.token = None
        self.profile = None
        self.header = {'Content-Type': 'application/json', 'Authorization': self.token}

    # user > get api token
    def get_api_token(self):
        ''' User - Get API-Token '''
        print(r'*' * 100, r'User - Get API-Token')
        url = self.base_url + '/token'
        data = {
            'username': self.username,
            'password': self.password
        }
        resp = requests.post(url, data=data).json()
        self.token = resp['data']['token']
        self.headers = {'Authorization': self.token}
        json_str = json.dumps(resp, indent=4)
        print(json_str)
        return json_str

    # user > get user profile
    def get_profile(self):
        '''User - Get User Profile'''
        print(r'*' * 100, r'User - Get User Profile')
        url = self.base_url + '/profile'
        resp = requests.post(url, headers=self.headers).json()
        self.profile = resp['data']
        json_str = json.dumps(resp, indent=4)
        print(json_str)
        return json_str

    # Image - Clear IP Based Temporary Upload History
    def clear_upload_history(self):
        '''Image - Clear IP Based Temporary Upload History'''
        print(r'*' * 100, r'Image - Clear IP Based Temporary Upload History')
        url = self.base_url + '/clear'
        resp = requests.get(url, headers=self.headers).json()
        json_str = json.dumps(resp, indent=4)
        print(json_str)
        return json_str

    # Image - IP Based Temporary Upload History
    def get_upload_history(self):
        '''Image - IP Based Temporary Upload History'''
        print(r'*' * 100, r'Image - IP Based Temporary Upload History')
        url = self.base_url + '/history'
        resp = requests.get(url, headers=self.headers).json()
        json_str = json.dumps(resp, indent=4)
        print(json_str)
        return json_str

    # image > Deletion - Image Deletion
    def delete_image(self, image_hash):
        '''Image - Image Deletion'''
        print(r'*' * 100, r'Image - Image Deletion')
        url = self.base_url + '/delete/' + image_hash
        resp = requests.get(url, headers=self.headers).json()
        json_str = json.dumps(resp, indent=4)
        print(json_str)
        return json_str

    # Image - Upload History
    def get_uploaded_images(self):
        '''Image - Upload History'''
        print(r'*' * 100, r'Image - Upload History')
        url = self.__class__.base_url + '/upload_history'
        resp = requests.get(url, headers=self.headers).json()
        self.upload_history = resp['data']
        json_str = json.dumps(resp, indent=4)
        print(json_str)
        return json_str

    # Image - Upload Image
    def upload_image(self, path):
        '''Image - Upload Image'''
        print(r'*' * 100, r'Image - Upload Image')
        url = self.base_url + '/upload'
        try:
            with open(path, 'rb') as file:
                files = {'smfile': file}
                resp = requests.post(url, files=files, headers=self.headers).json()
                json_str = json.dumps(resp, indent=4)
                print(json_str)
                return json_str
        except Exception as e:
            print(e)


if __name__ == '__main__':
    client = SMMS("un", "pwd")
    client.get_api_token()
    client.get_profile()

    client.get_upload_history()
    client.get_uploaded_images()

    client.clear_upload_history()

    client.get_upload_history()
    client.get_uploaded_images()

    upinfo = client.upload_image('path/to/xxx.jpg')
    json_info = json.loads(upinfo)
    uphash = json_info.get('data').get('hash')
    client.get_uploaded_images()
    client.delete_image(uphash)
    client.get_uploaded_images()
