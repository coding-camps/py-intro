# -*- encoding: utf-8 -*-

class StorageService:

    def upload_file(self, file: bytes): ...


class StorageService2(StorageService):
    def upload_file(self, file: bytes): ...
