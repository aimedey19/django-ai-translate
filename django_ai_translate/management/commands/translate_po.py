from __future__ import unicode_literals

import asyncio
from django.core.management.base import BaseCommand
from django_ai_translate.po_handler import load_po_file, save_po_file, get_untranslated_entries
from django_ai_translate.translator import translate_in_batches
from yaspin import yaspin


class Command(BaseCommand):
    help = 'Automatically translates a .po file using AI (Asynchronous)'

    def add_arguments(self, parser):
        parser.add_argument('-f', '--file', dest='po_file', help='Path to the .po file')
        parser.add_argument('-l', '--language', dest='language', help='Target language (e.g., "en", "fr")')
        parser.add_argument('-bs', '--batch_size', default=100, type=int, nargs='?', help='Enable verbose output')

    def handle(self, *args, **options):
        # Use asyncio.run to call async handler
        asyncio.run(self.async_handle(options))

    async def async_handle(self, options):
        po_file_path = options['po_file']

        po = load_po_file(po_file_path)
        entries = get_untranslated_entries(po)

        await translate_in_batches(entries, options['language'], options['batch_size'])

        save_po_file(po, po_file_path)
        self.stdout.write(self.style.SUCCESS("✅ Translation complete."))
