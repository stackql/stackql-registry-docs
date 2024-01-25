---
title: incidents
hide_title: false
hide_table_of_contents: false
keywords:
  - incidents
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
<tr><td><b>Name</b></td><td><code>incidents</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sentinel.incidents</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `etag` | `string` | Etag of the azure resource |
| `properties` | `object` | Describes incident properties |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `incidentId, resourceGroupName, subscriptionId, workspaceName` | Gets a given incident. |
| `list` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` | Gets all incidents. |
| `create_or_update` | `INSERT` | `incidentId, resourceGroupName, subscriptionId, workspaceName` | Creates or updates an incident. |
| `delete` | `DELETE` | `incidentId, resourceGroupName, subscriptionId, workspaceName` | Deletes a given incident. |
| `_list` | `EXEC` | `resourceGroupName, subscriptionId, workspaceName` | Gets all incidents. |
