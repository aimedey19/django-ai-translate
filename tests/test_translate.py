# tests/test_translate.py

from time import sleep
import unittest
import asyncio
import pytest
from cappa import command
from django_ai_translate import translate_text, async_translate_text
from django_ai_translate.po_handler import load_po_file, save_po_file, get_untranslated_entries
from tqdm.asyncio import tqdm
from yaspin import yaspin

import os

from django_ai_translate.translator import translate_in_batches
from helpers import chunked

def test_translation():
        file_path = os.path.join(os.path.dirname(__file__), "tests.po")
        po = load_po_file(file_path)
        entries = get_untranslated_entries(po)
        msgids = [entry.msgid for entry in tqdm(entries, desc="Extracting msgids")]
        msgids = "<sep>".join(msgids)
        with open("msgids.txt", "w") as f:
                msgids_txt = msgids.split("<sep>")
                for msgid in msgids_txt:
                        f.write(msgid + "\n\n\n\n\n\n")

        tqdm.write("")
        with yaspin(text="Translating...") as spinner:
            results = translate_text(msgids)
            spinner.ok("✅")
            with open("results.txt", "w") as f:
                f.write(results)
            results = results.split("<sep>")
        tqdm.write("")

        zipped = zip(entries, results)
        for entry, result in tqdm(zipped, total=len(zipped), desc="Filling up PO file"):
                entry.msgstr = result

        result = save_po_file(po, file_path)

        assert True


@pytest.mark.asyncio
async def test_async_translation():
        file_path = os.path.join(os.path.dirname(__file__), "tests.po")
        po = load_po_file(file_path)
        entries = get_untranslated_entries(po)
        await translate_in_batches(entries, batch_size=100)

        save_po_file(po, file_path)

        assert True


