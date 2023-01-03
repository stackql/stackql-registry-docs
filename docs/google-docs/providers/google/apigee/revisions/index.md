---
title: revisions
hide_title: false
hide_table_of_contents: false
keywords:
  - revisions
  - apigee
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>revisions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.apigee.revisions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `contentType` | `string` | The HTTP Content-Type header value specifying the content type of the body. |
| `data` | `string` | The HTTP request/response body as raw binary. |
| `extensions` | `array` | Application specific response metadata. Must be set in the first response for streaming APIs. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `organizations_apis_revisions_get` | `SELECT` | `apisId, organizationsId, revisionsId` | Gets an API proxy revision. To download the API proxy configuration bundle for the specified revision as a zip file, set the `format` query parameter to `bundle`. If you are using curl, specify `-o filename.zip` to save the output to a file; otherwise, it displays to `stdout`. Then, develop the API proxy configuration locally and upload the updated API proxy configuration revision, as described in [updateApiProxyRevision](updateApiProxyRevision). |
| `organizations_sharedflows_revisions_get` | `SELECT` | `organizationsId, revisionsId, sharedflowsId` | Gets a revision of a shared flow. To download the shared flow configuration bundle for the specified revision as a zip file, set the `format` query parameter to `bundle`. If you are using curl, specify `-o filename.zip` to save the output to a file; otherwise, it displays to `stdout`. Then, develop the shared flow configuration locally and upload the updated sharedFlow configuration revision, as described in [updateSharedFlowRevision](updateSharedFlowRevision). |
| `organizations_apis_revisions_delete` | `DELETE` | `apisId, organizationsId, revisionsId` | Deletes an API proxy revision and all policies, resources, endpoints, and revisions associated with it. The API proxy revision must be undeployed before you can delete it. |
| `organizations_sharedflows_revisions_delete` | `DELETE` | `organizationsId, revisionsId, sharedflowsId` | Deletes a shared flow and all associated policies, resources, and revisions. You must undeploy the shared flow before deleting it. |
| `organizations_apis_revisions_updateApiProxyRevision` | `EXEC` | `apisId, organizationsId, revisionsId` | Updates an existing API proxy revision by uploading the API proxy configuration bundle as a zip file from your local machine. You can update only API proxy revisions that have never been deployed. After deployment, an API proxy revision becomes immutable, even if it is undeployed. Set the `Content-Type` header to either `multipart/form-data` or `application/octet-stream`. |
| `organizations_environments_apis_revisions_deploy` | `EXEC` | `apisId, environmentsId, organizationsId, revisionsId` | Deploys a revision of an API proxy. If another revision of the same API proxy revision is currently deployed, set the `override` parameter to `true` to have this revision replace the currently deployed revision. You cannot invoke an API proxy until it has been deployed to an environment. After you deploy an API proxy revision, you cannot edit it. To edit the API proxy, you must create and deploy a new revision. For a request path `organizations/{org}/environments/{env}/apis/{api}/revisions/{rev}/deployments`, two permissions are required: * `apigee.deployments.create` on the resource `organizations/{org}/environments/{env}` * `apigee.proxyrevisions.deploy` on the resource `organizations/{org}/apis/{api}/revisions/{rev}`  |
| `organizations_environments_apis_revisions_undeploy` | `EXEC` | `apisId, environmentsId, organizationsId, revisionsId` | Undeploys an API proxy revision from an environment. For a request path `organizations/{org}/environments/{env}/apis/{api}/revisions/{rev}/deployments`, two permissions are required: * `apigee.deployments.delete` on the resource `organizations/{org}/environments/{env}` * `apigee.proxyrevisions.undeploy` on the resource `organizations/{org}/apis/{api}/revisions/{rev}` |
| `organizations_environments_sharedflows_revisions_deploy` | `EXEC` | `environmentsId, organizationsId, revisionsId, sharedflowsId` | Deploys a revision of a shared flow. If another revision of the same shared flow is currently deployed, set the `override` parameter to `true` to have this revision replace the currently deployed revision. You cannot use a shared flow until it has been deployed to an environment. For a request path `organizations/{org}/environments/{env}/sharedflows/{sf}/revisions/{rev}/deployments`, two permissions are required: * `apigee.deployments.create` on the resource `organizations/{org}/environments/{env}` * `apigee.sharedflowrevisions.deploy` on the resource `organizations/{org}/sharedflows/{sf}/revisions/{rev}` |
| `organizations_environments_sharedflows_revisions_undeploy` | `EXEC` | `environmentsId, organizationsId, revisionsId, sharedflowsId` | Undeploys a shared flow revision from an environment. For a request path `organizations/{org}/environments/{env}/sharedflows/{sf}/revisions/{rev}/deployments`, two permissions are required: * `apigee.deployments.delete` on the resource `organizations/{org}/environments/{env}` * `apigee.sharedflowrevisions.undeploy` on the resource `organizations/{org}/sharedflows/{sf}/revisions/{rev}` |
| `organizations_sharedflows_revisions_updateSharedFlowRevision` | `EXEC` | `organizationsId, revisionsId, sharedflowsId` | Updates a shared flow revision. This operation is only allowed on revisions which have never been deployed. After deployment a revision becomes immutable, even if it becomes undeployed. The payload is a ZIP-formatted shared flow. Content type must be either multipart/form-data or application/octet-stream. |
