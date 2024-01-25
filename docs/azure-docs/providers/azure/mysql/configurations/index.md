---
title: configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - configurations
  - mysql
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
<tr><td><b>Name</b></td><td><code>configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.mysql.configurations</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `configurationName, resourceGroupName, serverName, subscriptionId` | Gets information about a configuration of server. |
| `list_by_server` | `SELECT` | `resourceGroupName, serverName, subscriptionId` | List all the configurations in a given server. |
| `create_or_update` | `INSERT` | `configurationName, resourceGroupName, serverName, subscriptionId` | Updates a configuration of a server. |
| `_list_by_server` | `EXEC` | `resourceGroupName, serverName, subscriptionId` | List all the configurations in a given server. |
| `batch_update` | `EXEC` | `resourceGroupName, serverName, subscriptionId` | Update a list of configurations in a given server. |
| `update` | `EXEC` | `configurationName, resourceGroupName, serverName, subscriptionId` | Updates a configuration of a server. |
