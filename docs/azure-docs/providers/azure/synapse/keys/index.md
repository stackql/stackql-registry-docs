---
title: keys
hide_title: false
hide_table_of_contents: false
keywords:
  - keys
  - synapse
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
<tr><td><b>Name</b></td><td><code>keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.synapse.keys</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `keyName, resourceGroupName, subscriptionId, workspaceName` | Gets a workspace key |
| `list_by_workspace` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` | Returns a list of keys in a workspace |
| `create_or_update` | `INSERT` | `keyName, resourceGroupName, subscriptionId, workspaceName` | Creates or updates a workspace key |
| `delete` | `DELETE` | `keyName, resourceGroupName, subscriptionId, workspaceName` | Deletes a workspace key |
| `_list_by_workspace` | `EXEC` | `resourceGroupName, subscriptionId, workspaceName` | Returns a list of keys in a workspace |
