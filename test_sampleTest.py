import pytest

@pytest.mark.usefixtures("setup")
class SampleTestClass:
    def test_google_title(self):
        self.driver.get('https://google.com')
        title = self.driver.title
        print(f'Page title: {title}')
        assert title == 'google'
