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
| `apiDeployments` | `array` | The deployments from the specified publisher. |
| `nextPageToken` | `string` | A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_apis_deployments_list` | `SELECT` | `apisId, locationsId, projectsId` | Returns matching deployments. |
| `projects_locations_apis_deployments_create` | `INSERT` | `apisId, locationsId, projectsId` | Creates a specified deployment. |
| `projects_locations_apis_deployments_delete` | `DELETE` | `apisId, deploymentsId, locationsId, projectsId` | Removes a specified deployment, all revisions, and all child resources (e.g., artifacts). |
| `projects_locations_apis_deployments_get` | `EXEC` | `apisId, deploymentsId, locationsId, projectsId` | Returns a specified deployment. |
| `projects_locations_apis_deployments_patch` | `EXEC` | `apisId, deploymentsId, locationsId, projectsId` | Used to modify a specified deployment. |
| `projects_locations_apis_deployments_rollback` | `EXEC` | `apisId, deploymentsId, locationsId, projectsId` | Sets the current revision to a specified prior revision. Note that this creates a new revision with a new revision ID. |
| `projects_locations_apis_deployments_tag_revision` | `EXEC` | `apisId, deploymentsId, locationsId, projectsId` | Adds a tag to a specified revision of a deployment. |
