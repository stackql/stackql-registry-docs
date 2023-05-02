---
title: deployments
hide_title: false
hide_table_of_contents: false
keywords:
  - deployments
  - apigeeregistry
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>deployments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.apigeeregistry.deployments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Resource name. |
| `description` | `string` | A detailed description. |
| `intendedAudience` | `string` | Text briefly identifying the intended audience of the API. Changes to this value will not affect the revision. |
| `annotations` | `object` | Annotations attach non-identifying metadata to resources. Annotation keys and values are less restricted than those of labels, but should be generally used for small values of broad interest. Larger, topic- specific metadata should be stored in Artifacts. |
| `endpointUri` | `string` | The address where the deployment is serving. Changes to this value will update the revision. |
| `accessGuidance` | `string` | Text briefly describing how to access the endpoint. Changes to this value will not affect the revision. |
| `apiSpecRevision` | `string` | The full resource name (including revision ID) of the spec of the API being served by the deployment. Changes to this value will update the revision. Format: `apis/&#123;api&#125;/deployments/&#123;deployment&#125;` |
| `labels` | `object` | Labels attach identifying metadata to resources. Identifying metadata can be used to filter list operations. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. No more than 64 user labels can be associated with one resource (System labels are excluded). See https://goo.gl/xmQnxf for more information and examples of labels. System reserved label keys are prefixed with `apigeeregistry.googleapis.com/` and cannot be changed. |
| `createTime` | `string` | Output only. Creation timestamp; when the deployment resource was created. |
| `displayName` | `string` | Human-meaningful name. |
| `revisionId` | `string` | Output only. Immutable. The revision ID of the deployment. A new revision is committed whenever the deployment contents are changed. The format is an 8-character hexadecimal string. |
| `revisionUpdateTime` | `string` | Output only. Last update timestamp: when the represented revision was last modified. |
| `externalChannelUri` | `string` | The address of the external channel of the API (e.g., the Developer Portal). Changes to this value will not affect the revision. |
| `revisionCreateTime` | `string` | Output only. Revision creation timestamp; when the represented revision was created. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_apis_deployments_get` | `SELECT` | `apisId, deploymentsId, locationsId, projectsId` | Returns a specified deployment. |
| `projects_locations_apis_deployments_list` | `SELECT` | `apisId, locationsId, projectsId` | Returns matching deployments. |
| `projects_locations_apis_deployments_create` | `INSERT` | `apisId, locationsId, projectsId` | Creates a specified deployment. |
| `projects_locations_apis_deployments_delete` | `DELETE` | `apisId, deploymentsId, locationsId, projectsId` | Removes a specified deployment, all revisions, and all child resources (e.g., artifacts). |
| `projects_locations_apis_deployments_patch` | `EXEC` | `apisId, deploymentsId, locationsId, projectsId` | Used to modify a specified deployment. |
| `projects_locations_apis_deployments_rollback` | `EXEC` | `apisId, deploymentsId, locationsId, projectsId` | Sets the current revision to a specified prior revision. Note that this creates a new revision with a new revision ID. |
| `projects_locations_apis_deployments_tagRevision` | `EXEC` | `apisId, deploymentsId, locationsId, projectsId` | Adds a tag to a specified revision of a deployment. |
