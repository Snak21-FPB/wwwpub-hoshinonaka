from django.test import TestCase
import freezegun
from posts.models import Bureau
from datetime import datetime
import datetime as dt

class TestBureauModel(TestCase):
    @classmethod
    @freezegun.freeze_time("2023-02-01 21:21:21")
    def setUpTestData(cls):
        bureaus = [Bureau(name=f"テスト局{i}",keyword=f"test_bureau_{i}",sort_num=10-i) for i in range(10)]
        Bureau.objects.bulk_create(bureaus)

    def setUp(self):
        self.bureau = Bureau.objects.get(name="テスト局1")

    def test_created_at(self):
        self.assertEqual(self.bureau.created_at, datetime(2023,2,1,21,21,21, tzinfo=dt.timezone.utc))
    
    @freezegun.freeze_time("2023-02-01 22:22:22")
    def test_updated_at(self):
        self.bureau.outline = "更新"
        self.bureau.save()
        self.assertEqual(self.bureau.updated_at, datetime(2023,2,1,22,22,22,tzinfo=dt.timezone.utc))