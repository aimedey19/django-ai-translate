import polib

def load_po_file(path):
    return polib.pofile(path)


def save_po_file(po, path):
    po.save(path)


def get_untranslated_entries(po):
    return [entry for entry in po if not entry.translated()]


def get_all_entries(po):
    return [entry for entry in po]
