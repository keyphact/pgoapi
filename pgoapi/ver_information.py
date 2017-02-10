class VersionInformation(object):
    ENDPOINT = 'https://pokehash.buddyauth.com/api/v125/hash'
    POGOAPI_VERSION_DEFAULT = 4500
    POGOAPI_VERSION_LATEST = 5500

class Version:  
    def version(self, pogoapi_ver):
        tmp_version = str(pogoapi_ver)
        str_version = '0_' + tmp_version[0:2]
        return str_version