---
title: workspace_api_release
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_api_release
  - api_management
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workspace_api_release</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.workspace_api_release</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `apiId, releaseId, resourceGroupName, serviceName, subscriptionId, workspaceId` | Returns the details of an API release. |
| `list_by_service` | `SELECT` | `apiId, resourceGroupName, serviceName, subscriptionId, workspaceId` | Lists all releases of an API. An API release is created when making an API Revision current. Releases are also used to rollback to previous revisions. Results will be paged and can be constrained by the $top and $skip parameters. |
| `create_or_update` | `INSERT` | `apiId, releaseId, resourceGroupName, serviceName, subscriptionId, workspaceId` | Creates a new Release for the API. |
| `delete` | `DELETE` | `If-Match, apiId, releaseId, resourceGroupName, serviceName, subscriptionId, workspaceId` | Deletes the specified release in the API. |
| `_list_by_service` | `EXEC` | `apiId, resourceGroupName, serviceName, subscriptionId, workspaceId` | Lists all releases of an API. An API release is created when making an API Revision current. Releases are also used to rollback to previous revisions. Results will be paged and can be constrained by the $top and $skip parameters. |
| `update` | `EXEC` | `If-Match, apiId, releaseId, resourceGroupName, serviceName, subscriptionId, workspaceId` | Updates the details of the release of the API specified by its identifier. |
