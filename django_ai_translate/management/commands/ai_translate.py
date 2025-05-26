from __future__ import unicode_literals
from django.core.management.base import BaseCommand
from django_ai_translate import translate_text
from django_ai_translate import load_po_file, save_po_file, get_untranslated_entries
from tqdm import tqdm
from yaspin import yaspin

class Command(BaseCommand):
    help = 'Automatically translates .po file using AI (Synchronous)'

    def add_arguments(self, parser):
        parser.add_argument('po_file', help='Path to .po file')
        parser.add_argument('language', help='Target language')

    def handle(self, *args, **options):
        # po = load_po_file(options['po_file'])
        # entries = get_untranslated_entries(po)
        # msgids = [entry.msgid for entry in tqdm(entries, desc="Extracting msgids")]
        # msgids = ",".join(msgids)
        # tqdm.write("")
        # with yaspin(text="Translating...") as spinner:
        #     results = translate_text(msgids)
        #     spinner.ok("✅")
        # results = results.split(",")
        # tqdm.write("Filling up PO file...")
        # for entry, result in tqdm(zip(entries, results), total=len(entries), desc="Filling up PO file", leave=True):
        #         entry.msgstr = result
        # save_po_file(po, options['po_file'])
        self.stdout.write(self.style.SUCCESS('Not working yet. Please use async_ai_translate instead.'))
