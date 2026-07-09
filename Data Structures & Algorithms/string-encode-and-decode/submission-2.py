class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs):
            return r'\@'.join(strs)
        else:
            return r'\!'

    def decode(self, s: str) -> List[str]:
        if s != r'\!':
            return s.split(r'\@')
        else:
            return list()
