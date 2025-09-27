#!/usr/bin/python

class FilterModule(object):
    ''' Some useful data manipulation filters for dict/list/string '''

    def filters(self):
        return {
            'dictdict2list': self.dictdict2list,
            'split_and_strip': self.split_and_strip,
        }

    def dictdict2list(self, d: dict[dict], key: str = 'key') -> list[dict]:
        return [{
            key: k,
            **v
        } for k, v in d.items()]
    
    def split_and_strip(self, s: str | list[str], sep: str=',') -> list[str]:
        return list(map(
            lambda x: x.strip(),
            s if isinstance(s, list) else s.split(sep)
        ))
