#!/usr/bin/env python

import string
import random
from locust import HttpLocust, TaskSet, task

class WebsiteTasks(TaskSet):

    def id_generator(self, size=6, chars=string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    @task
    def post(self):
        self.client.post("/", {
            "url": "https://www." + self.id_generator() + ".com"
        })

class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    min_wait = 5000
    max_wait = 15000
    host = 'http://127.0.0.1:80'
