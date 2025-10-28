class SoupReplacer:
    def __init__(self, og_tag, alt_tag):
        self.og_tag = og_tag
        self.alt_tag = alt_tag

    def replace(self, name):
        """Return replaced tag name if matches og_tag."""
        if name == self.og_tag:
            return self.alt_tag
        return name