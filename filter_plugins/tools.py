#!/usr/bin/python

class FilterModule(object):
    ''' Some useful data manipulation filters for dict/list/string '''

    def filters(self):
        return {
            'dict2records': self.dict2records,
            'split_and_strip': self.split_and_strip,
        }

    def dict2records(self, d: dict[str, dict], key: str = 'key') -> list[dict]:
        return [{
            key: k,
            **v
        } for k, v in d.items()]
    
    def split_and_strip(self, s: str | list[str], sep: str=',') -> list[str]:
        return list(map(
            lambda x: x.strip(),
            s if isinstance(s, list) else s.split(sep)
        ))
