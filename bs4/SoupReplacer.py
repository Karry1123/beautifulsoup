class SoupReplacer:
    def __init__(
            self,
            og_tag = None,
            alt_tag = None,
            *,
            name_xformer = None,
            attrs_xformer = None,
            xformer = None,
    ):
        self.og_tag = og_tag
        self.alt_tag = alt_tag
        self.name_xformer = name_xformer
        self.attrs_xformer = attrs_xformer
        self.xformer = xformer

    def replace_tag_name(self, name):
        """Return replaced tag name if matches og_tag."""
        if self.og_tag and name == self.og_tag:
            return self.alt_tag

        if self.name_xformer:
            class DummyTag:
                def __init__(self, name):
                    self.name = name

            dummy = DummyTag(name)
            return self.name_xformer(dummy)

        return name

    def replace_attrs(self, tag):
        """Return possibly transformed attributes."""
        if self.attrs_xformer:
            new_attrs = self.attrs_xformer(tag)
            if new_attrs is not None:
                tag.attrs = new_attrs
        return tag.attrs

    def apply_xformer(self, tag):
        if self.xformer:
            self.xformer(tag)