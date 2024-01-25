---
title: labels
hide_title: false
hide_table_of_contents: false
keywords:
  - labels
  - defender
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
<tr><td><b>Name</b></td><td><code>labels</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.defender.labels</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_by_workspace` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` | Returns a list of labels in the given workspace. |
| `delete` | `DELETE` | `labelName, resourceGroupName, subscriptionId, workspaceName` | Delete a Label. |
| `_list_by_workspace` | `EXEC` | `resourceGroupName, subscriptionId, workspaceName` | Returns a list of labels in the given workspace. |
| `create_and_update` | `EXEC` | `labelName, resourceGroupName, subscriptionId, workspaceName` | Create or update a Label. |
| `get_by_workspace` | `EXEC` | `labelName, resourceGroupName, subscriptionId, workspaceName` | Returns a label in the given workspace. |
| `update` | `EXEC` | `labelName, resourceGroupName, subscriptionId, workspaceName` | Update a Label. |
