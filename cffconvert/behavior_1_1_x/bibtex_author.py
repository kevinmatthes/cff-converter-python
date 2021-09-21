from cffconvert.behavior_shared.bibtex_author_shared import BibtexAuthorShared as Shared


class BibtexAuthor(Shared):

    def __init__(self, author):
        super().__init__(author)

    def as_string(self):
        key = ''.join([
            self._has_given_name(),
            self._has_family_name(),
            self._has_alias(),
            self._has_name()
        ])
        return self._behaviors[key]()
