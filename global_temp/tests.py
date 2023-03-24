from django.test import TestCase

class TemeratureTests(TestCase):
    
    def test_Global_test(self):
        url = '/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'global_temp/index.html')
        self.assertContains(response, 'The Global Historical Climatology Network (GHCN) is an integrated database of climate that summaries from land surface stations across the globe')
