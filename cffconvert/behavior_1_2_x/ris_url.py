from cffconvert.behavior_shared.ris_url_shared import RisUrlShared as Shared


class RisUrl(Shared):

    def __init__(self, cffobj):
        super().__init__(cffobj)

    def as_string(self):
        key = ''.join([
            self._has_identifiers_url(),
            self._has_repository(),
            self._has_repository_artifact(),
            self._has_repository_code(),
            self._has_url()
        ])
        return self._behaviors[key]()
