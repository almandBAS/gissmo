# -*- coding: utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
from docker import Client

DOCKER_CONTAINER_NAME = 'gissmo'
DOCKER_CONTAINER_DEFAULT_PORT = '8000'
DEFAULT_ADMIN_LOGIN = 'olivier'
DEFAULT_ADMIN_PASSWORD = 'olivier'

class SimpleTest(unittest.TestCase):
    """
    A set of tests that only load some webpages from Gissmo.
    """

    def setUp(self):
        """
        Launch Firefox as Web Testing Platform.
        """
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
        # search for gissmo instance IP (in Docker)
        c = Client(base_url='unix://var/run/docker.sock')
        container_metadata = c.inspect_container(DOCKER_CONTAINER_NAME)
        try:
            self.ip = container_metadata['NetworkSettings']['IPAddress']
        except KeyError as e:
            self.ip = 'localhost'
        try:
            self.ports = container_metadata['NetworkSettings']['Ports']
        except KeyError as e:
            self.ports = None
        self.port = DOCKER_CONTAINER_DEFAULT_PORT
        # DOCKER BUG: Don't know why 8000 is the default one
#        if self.ports:
#            try:
#                self.port = self.ports['8000/tcp'][0]['HostPort']
#            except KeyError as e:
#                self.port = None
        self.url = 'http://%s:%s/' % (self.ip, self.port)

    def tearDown(self):
        """
        Close Browser.
        """
        self.browser.quit()

    def test_can_get_main_pages(self):
        """
        Check that each page don't send a 404 error message
        """
        # Martin Dupont start using the site. He goes to check the website 
        #+ homepage.
        url = self.url
        self.browser.get(url)

        # He receive a 404 error: Page not found. He remembers that we should 
        #+ type /gissmo after the URL
        self.assertIn('Page not found', self.browser.title, 
            'Problem loading %s' % url)
        url = self.url + 'gissmo/'
        self.browser.get(url)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Gissmo', header_text, 
            'Problem loading %s' % url)

        # He puts his username and password to connect the admin interface
        self.assertIn('Log in', self.browser.title, 
            'Problem loading %s: Not login page' % url)
        inputlogin = self.browser.find_element_by_id('id_username')
        inputpassword = self.browser.find_element_by_id('id_password')
        inputlogin.send_keys(DEFAULT_ADMIN_LOGIN)
        inputpassword.send_keys(DEFAULT_ADMIN_PASSWORD)

        # When he hits enter, the page updates, and now administration appears
        inputpassword.send_keys(Keys.ENTER)
        self.assertIn('Site administration', self.browser.title, 
            'Login problem on %s: no administration interface found.')

        # He gets "Sites" list
        self.fail('Finish the test!')

        # He gets "Modèle des équipements" list

        # He gets "Equipements" list

        # He gets "Interventions" list

if __name__ == "__main__":
    unittest.main()
