# Copyright 2023 University of Stuttgart
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


"""Module containing the routes of the Taskmanager API."""

from ..models.services import ServicesSchema, ServiceIDSchema
from typing import Dict, List
from flask.helpers import url_for
from flask.views import MethodView
from dataclasses import dataclass
from http import HTTPStatus

from .root import SERVICES_API


@dataclass
class SERVICES:
    serviceType: str
    description: str
    address: str
    status: str
    name: str
    url: str
    simulator: bool


@SERVICES_API.route("/<string:service_id>/")
class ServicesView(MethodView):
    """Services Endpoint to get properties of a specific service."""

    @SERVICES_API.arguments(ServiceIDSchema(), location="path")
    @SERVICES_API.response(HTTPStatus.OK, ServicesSchema())
    def get(self):
        """Get information about a sinlge service."""
        
        pass

