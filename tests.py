import unittest
import heywatch
from heywatch import job
import os
class HeyWatchTestCase(unittest.TestCase):

    def test_submit_job(self):
      conf = """
set source = https://s3-eu-west-1.amazonaws.com/media.heywatch.com/test.mp4
-> mp4 = s3://a:s@bucket/video.mp4
"""

      job = heywatch.job.submit(conf)
      self.assertEqual("ok", job["status"])
      self.assertTrue(job["id"] > 0)

    def test_submit_bad_config(self):
      conf = """
set source = https://s3-eu-west-1.amazonaws.com/media.heywatch.com/test.mp4
"""
      job = heywatch.job.submit(conf)
      self.assertEqual("error", job["status"])
      self.assertEqual("config_not_valid", job["error_code"])

if __name__ == '__main__':
    unittest.main()