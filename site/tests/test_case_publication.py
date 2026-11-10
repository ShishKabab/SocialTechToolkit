"""Publication-boundary regressions, including failures rather than only happy paths."""
import copy
import json
from pathlib import Path
import sys
import unittest
from unittest.mock import patch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
import cases
from editorial_drafts import NOTICE

class CasePublication(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.entries=json.loads((cases.ROOT/'content/catalog.json').read_text())
        for e in cls.entries:e['url']=('/dynamics/' if e['kind']=='D' else '/technologies/')+e['slug']+'/'
        cls.ids={e['id'] for e in cls.entries}
        cls.records=cases.load_cases(cls.entries)

    def test_missing_or_unapproved_status_fails(self):
        for status in (None,'reviewed',''):
            c=copy.deepcopy(self.records[0])
            if status is None:del c['editorial_status']
            else:c['editorial_status']=status
            with self.assertRaises(AssertionError):cases.validate_case(c,self.ids)

    def test_research_fields_fail_closed(self):
        for field in ('research_gaps','gft_reference','editorial_research_notes','sources'):
            c=copy.deepcopy(self.records[0]);c[field]='INTERNAL SENTINEL'
            with self.assertRaises(AssertionError):cases.validate_case(c,self.ids)
        c=copy.deepcopy(self.records[0]);c['sections'][0]['source_ids']=['internal']
        with self.assertRaises(AssertionError):cases.validate_case(c,self.ids)

    def test_render_neither_reads_nor_exports_research(self):
        original=Path.read_text
        def public_read(path,*args,**kwargs):
            self.assertNotIn('research',path.parts)
            return original(path,*args,**kwargs)
        pages={}
        def page(url,title,description,body):pages[url]=body
        with patch.object(Path,'read_text',public_read),patch.object(Path,'write_text',side_effect=AssertionError('Renderer attempted a data export')):
            records=cases.load_cases(self.entries)
            cases.render_cases(page,self.entries,[],records)
        for c in records:
            body=pages['/cases/'+c['id']+'/']
            self.assertEqual(body.count('data-editorial-status="needs-guidance"'),1)
            self.assertIn(NOTICE,body)
        self.assertNotIn('/cases/backlog/',pages)
        self.assertNotIn('case-catalog.json',pages['/cases/'])

if __name__=='__main__':unittest.main()
