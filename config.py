#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

""" Bot Configuration """


class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "616fd6bc-7e6f-4a67-ba4a-9ef1ee917546")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "ZwTgkQhnB/zGf-8IS0lezjx=0PYZPO6[")
