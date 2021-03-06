# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateClusterOptionsDetails(object):
    """
    The properties that define extra options updating a cluster.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateClusterOptionsDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param admission_controller_options:
            The value to assign to the admission_controller_options property of this UpdateClusterOptionsDetails.
        :type admission_controller_options: AdmissionControllerOptions

        """
        self.swagger_types = {
            'admission_controller_options': 'AdmissionControllerOptions'
        }

        self.attribute_map = {
            'admission_controller_options': 'admissionControllerOptions'
        }

        self._admission_controller_options = None

    @property
    def admission_controller_options(self):
        """
        Gets the admission_controller_options of this UpdateClusterOptionsDetails.
        Configurable cluster admission controllers


        :return: The admission_controller_options of this UpdateClusterOptionsDetails.
        :rtype: AdmissionControllerOptions
        """
        return self._admission_controller_options

    @admission_controller_options.setter
    def admission_controller_options(self, admission_controller_options):
        """
        Sets the admission_controller_options of this UpdateClusterOptionsDetails.
        Configurable cluster admission controllers


        :param admission_controller_options: The admission_controller_options of this UpdateClusterOptionsDetails.
        :type: AdmissionControllerOptions
        """
        self._admission_controller_options = admission_controller_options

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
