---
title: incident_comments
hide_title: false
hide_table_of_contents: false
keywords:
  - incident_comments
  - sentinel
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
<tr><td><b>Name</b></td><td><code>incident_comments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sentinel.incident_comments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `etag` | `string` | Etag of the azure resource |
| `properties` | `object` | Incident comment property bag. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `incidentCommentId, incidentId, resourceGroupName, subscriptionId, workspaceName` | Gets a comment for a given incident. |
| `list` | `SELECT` | `incidentId, resourceGroupName, subscriptionId, workspaceName` | Gets all comments for a given incident. |
| `create_or_update` | `INSERT` | `incidentCommentId, incidentId, resourceGroupName, subscriptionId, workspaceName` | Creates or updates a comment for a given incident. |
| `delete` | `DELETE` | `incidentCommentId, incidentId, resourceGroupName, subscriptionId, workspaceName` | Deletes a comment for a given incident. |
| `_list` | `EXEC` | `incidentId, resourceGroupName, subscriptionId, workspaceName` | Gets all comments for a given incident. |
