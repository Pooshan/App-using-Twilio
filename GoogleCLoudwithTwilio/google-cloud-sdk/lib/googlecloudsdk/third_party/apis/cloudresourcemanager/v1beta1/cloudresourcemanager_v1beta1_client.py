"""Generated client library for cloudresourcemanager version v1beta1."""
# NOTE: This file is autogenerated and should not be edited by hand.
from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.cloudresourcemanager.v1beta1 import cloudresourcemanager_v1beta1_messages as messages


class CloudresourcemanagerV1beta1(base_api.BaseApiClient):
  """Generated client library for service cloudresourcemanager version v1beta1."""

  MESSAGES_MODULE = messages
  BASE_URL = u'https://cloudresourcemanager.googleapis.com/'

  _PACKAGE = u'cloudresourcemanager'
  _SCOPES = [u'https://www.googleapis.com/auth/cloud-platform', u'https://www.googleapis.com/auth/cloud-platform.read-only']
  _VERSION = u'v1beta1'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _CLIENT_CLASS_NAME = u'CloudresourcemanagerV1beta1'
  _URL_VERSION = u'v1beta1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None):
    """Create a new cloudresourcemanager handle."""
    url = url or self.BASE_URL
    super(CloudresourcemanagerV1beta1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers)
    self.organizations = self.OrganizationsService(self)
    self.projects = self.ProjectsService(self)

  class OrganizationsService(base_api.BaseApiService):
    """Service class for the organizations resource."""

    _NAME = u'organizations'

    def __init__(self, client):
      super(CloudresourcemanagerV1beta1.OrganizationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      """Fetches an Organization resource identified by the specified resource name.

      Args:
        request: (CloudresourcemanagerOrganizationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Organization) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'cloudresourcemanager.organizations.get',
        ordered_params=[u'organizationsId'],
        path_params=[u'organizationsId'],
        query_params=[u'organizationId'],
        relative_path=u'v1beta1/organizations/{organizationsId}',
        request_field='',
        request_type_name=u'CloudresourcemanagerOrganizationsGetRequest',
        response_type_name=u'Organization',
        supports_download=False,
    )

    def GetIamPolicy(self, request, global_params=None):
      """Gets the access control policy for an Organization resource. May be empty.
if no such policy or resource exists. The `resource` field should be the
organization's resource name, e.g. "organizations/123".

      Args:
        request: (CloudresourcemanagerOrganizationsGetIamPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Policy) The response message.
      """
      config = self.GetMethodConfig('GetIamPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    GetIamPolicy.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'cloudresourcemanager.organizations.getIamPolicy',
        ordered_params=[u'organizationsId'],
        path_params=[u'organizationsId'],
        query_params=[],
        relative_path=u'v1beta1/organizations/{organizationsId}:getIamPolicy',
        request_field=u'getIamPolicyRequest',
        request_type_name=u'CloudresourcemanagerOrganizationsGetIamPolicyRequest',
        response_type_name=u'Policy',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      """Lists Organization resources that are visible to the user and satisfy.
the specified filter. This method returns Organizations in an unspecified
order. New Organizations do not necessarily appear at the end of the list.

      Args:
        request: (CloudresourcemanagerOrganizationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListOrganizationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'cloudresourcemanager.organizations.list',
        ordered_params=[],
        path_params=[],
        query_params=[u'filter', u'pageSize', u'pageToken'],
        relative_path=u'v1beta1/organizations',
        request_field='',
        request_type_name=u'CloudresourcemanagerOrganizationsListRequest',
        response_type_name=u'ListOrganizationsResponse',
        supports_download=False,
    )

    def SetIamPolicy(self, request, global_params=None):
      """Sets the access control policy on an Organization resource. Replaces any.
existing policy. The `resource` field should be the organization's resource
name, e.g. "organizations/123".

      Args:
        request: (CloudresourcemanagerOrganizationsSetIamPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Policy) The response message.
      """
      config = self.GetMethodConfig('SetIamPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    SetIamPolicy.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'cloudresourcemanager.organizations.setIamPolicy',
        ordered_params=[u'organizationsId'],
        path_params=[u'organizationsId'],
        query_params=[],
        relative_path=u'v1beta1/organizations/{organizationsId}:setIamPolicy',
        request_field=u'setIamPolicyRequest',
        request_type_name=u'CloudresourcemanagerOrganizationsSetIamPolicyRequest',
        response_type_name=u'Policy',
        supports_download=False,
    )

    def TestIamPermissions(self, request, global_params=None):
      """Returns permissions that a caller has on the specified Organization.
The `resource` field should be the organization's resource name,
e.g. "organizations/123".

      Args:
        request: (CloudresourcemanagerOrganizationsTestIamPermissionsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (TestIamPermissionsResponse) The response message.
      """
      config = self.GetMethodConfig('TestIamPermissions')
      return self._RunMethod(
          config, request, global_params=global_params)

    TestIamPermissions.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'cloudresourcemanager.organizations.testIamPermissions',
        ordered_params=[u'organizationsId'],
        path_params=[u'organizationsId'],
        query_params=[],
        relative_path=u'v1beta1/organizations/{organizationsId}:testIamPermissions',
        request_field=u'testIamPermissionsRequest',
        request_type_name=u'CloudresourcemanagerOrganizationsTestIamPermissionsRequest',
        response_type_name=u'TestIamPermissionsResponse',
        supports_download=False,
    )

    def Update(self, request, global_params=None):
      """Updates an Organization resource identified by the specified resource name.

      Args:
        request: (CloudresourcemanagerOrganizationsUpdateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Organization) The response message.
      """
      config = self.GetMethodConfig('Update')
      return self._RunMethod(
          config, request, global_params=global_params)

    Update.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'PUT',
        method_id=u'cloudresourcemanager.organizations.update',
        ordered_params=[u'organizationsId'],
        path_params=[u'organizationsId'],
        query_params=[],
        relative_path=u'v1beta1/organizations/{organizationsId}',
        request_field=u'organization',
        request_type_name=u'CloudresourcemanagerOrganizationsUpdateRequest',
        response_type_name=u'Organization',
        supports_download=False,
    )

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = u'projects'

    def __init__(self, client):
      super(CloudresourcemanagerV1beta1.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      """Creates a Project resource.

Initially, the Project resource is owned by its creator exclusively.
The creator can later grant permission to others to read or update the
Project.

Several APIs are activated automatically for the Project, including
Google Cloud Storage.

      Args:
        request: (CloudresourcemanagerProjectsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Project) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'cloudresourcemanager.projects.create',
        ordered_params=[],
        path_params=[],
        query_params=[u'useLegacyStack'],
        relative_path=u'v1beta1/projects',
        request_field=u'project',
        request_type_name=u'CloudresourcemanagerProjectsCreateRequest',
        response_type_name=u'Project',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      """Marks the Project identified by the specified.
`project_id` (for example, `my-project-123`) for deletion.
This method will only affect the Project if the following criteria are met:

+ The Project does not have a billing account associated with it.
+ The Project has a lifecycle state of
ACTIVE.

This method changes the Project's lifecycle state from
ACTIVE
to DELETE_REQUESTED.
The deletion starts at an unspecified time, at which point the project is
no longer accessible.

Until the deletion completes, you can check the lifecycle state
checked by retrieving the Project with GetProject,
and the Project remains visible to ListProjects.
However, you cannot update the project.

After the deletion completes, the Project is not retrievable by
the  GetProject and
ListProjects methods.

The caller must have modify permissions for this Project.

      Args:
        request: (CloudresourcemanagerProjectsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'DELETE',
        method_id=u'cloudresourcemanager.projects.delete',
        ordered_params=[u'projectId'],
        path_params=[u'projectId'],
        query_params=[],
        relative_path=u'v1beta1/projects/{projectId}',
        request_field='',
        request_type_name=u'CloudresourcemanagerProjectsDeleteRequest',
        response_type_name=u'Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      """Retrieves the Project identified by the specified.
`project_id` (for example, `my-project-123`).

The caller must have read permissions for this Project.

      Args:
        request: (CloudresourcemanagerProjectsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Project) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'cloudresourcemanager.projects.get',
        ordered_params=[u'projectId'],
        path_params=[u'projectId'],
        query_params=[],
        relative_path=u'v1beta1/projects/{projectId}',
        request_field='',
        request_type_name=u'CloudresourcemanagerProjectsGetRequest',
        response_type_name=u'Project',
        supports_download=False,
    )

    def GetAncestry(self, request, global_params=None):
      """Gets a list of ancestors in the resource hierarchy for the Project.
identified by the specified `project_id` (for example, `my-project-123`).

The caller must have read permissions for this Project.

      Args:
        request: (CloudresourcemanagerProjectsGetAncestryRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GetAncestryResponse) The response message.
      """
      config = self.GetMethodConfig('GetAncestry')
      return self._RunMethod(
          config, request, global_params=global_params)

    GetAncestry.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'cloudresourcemanager.projects.getAncestry',
        ordered_params=[u'projectId'],
        path_params=[u'projectId'],
        query_params=[],
        relative_path=u'v1beta1/projects/{projectId}:getAncestry',
        request_field=u'getAncestryRequest',
        request_type_name=u'CloudresourcemanagerProjectsGetAncestryRequest',
        response_type_name=u'GetAncestryResponse',
        supports_download=False,
    )

    def GetIamPolicy(self, request, global_params=None):
      """Returns the IAM access control policy for the specified Project.
Permission is denied if the policy or the resource does not exist.

      Args:
        request: (CloudresourcemanagerProjectsGetIamPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Policy) The response message.
      """
      config = self.GetMethodConfig('GetIamPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    GetIamPolicy.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'cloudresourcemanager.projects.getIamPolicy',
        ordered_params=[u'resource'],
        path_params=[u'resource'],
        query_params=[],
        relative_path=u'v1beta1/projects/{resource}:getIamPolicy',
        request_field=u'getIamPolicyRequest',
        request_type_name=u'CloudresourcemanagerProjectsGetIamPolicyRequest',
        response_type_name=u'Policy',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      """Lists Projects that are visible to the user and satisfy the.
specified filter. This method returns Projects in an unspecified order.
New Projects do not necessarily appear at the end of the list.

      Args:
        request: (CloudresourcemanagerProjectsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListProjectsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'cloudresourcemanager.projects.list',
        ordered_params=[],
        path_params=[],
        query_params=[u'filter', u'pageSize', u'pageToken'],
        relative_path=u'v1beta1/projects',
        request_field='',
        request_type_name=u'CloudresourcemanagerProjectsListRequest',
        response_type_name=u'ListProjectsResponse',
        supports_download=False,
    )

    def SetIamPolicy(self, request, global_params=None):
      """Sets the IAM access control policy for the specified Project. Replaces.
any existing policy.

The following constraints apply when using `setIamPolicy()`:

+ Project does not support `allUsers` and `allAuthenticatedUsers` as
`members` in a `Binding` of a `Policy`.

+ The owner role can be granted only to `user` and `serviceAccount`.

+ Service accounts can be made owners of a project directly
without any restrictions. However, to be added as an owner, a user must be
invited via Cloud Platform console and must accept the invitation.

+ A user cannot be granted the owner role using `setIamPolicy()`. The user
must be granted the owner role using the Cloud Platform Console and must
explicitly accept the invitation.

+ Invitations to grant the owner role cannot be sent using `setIamPolicy()`;
they must be sent only using the Cloud Platform Console.

+ Membership changes that leave the project without any owners that have
accepted the Terms of Service (ToS) will be rejected.

+ There must be at least one owner who has accepted the Terms of
Service (ToS) agreement in the policy. Calling `setIamPolicy()` to
to remove the last ToS-accepted owner from the policy will fail. This
restriction also applies to legacy projects that no longer have owners
who have accepted the ToS. Edits to IAM policies will be rejected until
the lack of a ToS-accepting owner is rectified.

+ Calling this method requires enabling the App Engine Admin API.

Note: Removing service accounts from policies or changing their roles
can render services completely inoperable. It is important to understand
how the service account is being used before removing or updating its roles.

      Args:
        request: (CloudresourcemanagerProjectsSetIamPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Policy) The response message.
      """
      config = self.GetMethodConfig('SetIamPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    SetIamPolicy.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'cloudresourcemanager.projects.setIamPolicy',
        ordered_params=[u'resource'],
        path_params=[u'resource'],
        query_params=[],
        relative_path=u'v1beta1/projects/{resource}:setIamPolicy',
        request_field=u'setIamPolicyRequest',
        request_type_name=u'CloudresourcemanagerProjectsSetIamPolicyRequest',
        response_type_name=u'Policy',
        supports_download=False,
    )

    def TestIamPermissions(self, request, global_params=None):
      """Returns permissions that a caller has on the specified Project.

      Args:
        request: (CloudresourcemanagerProjectsTestIamPermissionsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (TestIamPermissionsResponse) The response message.
      """
      config = self.GetMethodConfig('TestIamPermissions')
      return self._RunMethod(
          config, request, global_params=global_params)

    TestIamPermissions.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'cloudresourcemanager.projects.testIamPermissions',
        ordered_params=[u'resource'],
        path_params=[u'resource'],
        query_params=[],
        relative_path=u'v1beta1/projects/{resource}:testIamPermissions',
        request_field=u'testIamPermissionsRequest',
        request_type_name=u'CloudresourcemanagerProjectsTestIamPermissionsRequest',
        response_type_name=u'TestIamPermissionsResponse',
        supports_download=False,
    )

    def Undelete(self, request, global_params=None):
      """Restores the Project identified by the specified.
`project_id` (for example, `my-project-123`).
You can only use this method for a Project that has a lifecycle state of
DELETE_REQUESTED.
After deletion starts, the Project cannot be restored.

The caller must have modify permissions for this Project.

      Args:
        request: (CloudresourcemanagerProjectsUndeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Undelete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Undelete.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'cloudresourcemanager.projects.undelete',
        ordered_params=[u'projectId'],
        path_params=[u'projectId'],
        query_params=[],
        relative_path=u'v1beta1/projects/{projectId}:undelete',
        request_field=u'undeleteProjectRequest',
        request_type_name=u'CloudresourcemanagerProjectsUndeleteRequest',
        response_type_name=u'Empty',
        supports_download=False,
    )

    def Update(self, request, global_params=None):
      """Updates the attributes of the Project identified by the specified.
`project_id` (for example, `my-project-123`).

The caller must have modify permissions for this Project.

      Args:
        request: (Project) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Project) The response message.
      """
      config = self.GetMethodConfig('Update')
      return self._RunMethod(
          config, request, global_params=global_params)

    Update.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'PUT',
        method_id=u'cloudresourcemanager.projects.update',
        ordered_params=[u'projectId'],
        path_params=[u'projectId'],
        query_params=[],
        relative_path=u'v1beta1/projects/{projectId}',
        request_field='<request>',
        request_type_name=u'Project',
        response_type_name=u'Project',
        supports_download=False,
    )
