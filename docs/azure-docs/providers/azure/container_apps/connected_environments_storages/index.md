---
title: connected_environments_storages
hide_title: false
hide_table_of_contents: false
keywords:
  - connected_environments_storages
  - container_apps
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
<tr><td><b>Name</b></td><td><code>connected_environments_storages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.container_apps.connected_environments_storages</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `connectedEnvironmentName, resourceGroupName, storageName, subscriptionId` | Get storage for a connectedEnvironment. |
| `list` | `SELECT` | `connectedEnvironmentName, resourceGroupName, subscriptionId` | Get all storages for a connectedEnvironment. |
| `create_or_update` | `INSERT` | `connectedEnvironmentName, resourceGroupName, storageName, subscriptionId` | Create or update storage for a connectedEnvironment. |
| `delete` | `DELETE` | `connectedEnvironmentName, resourceGroupName, storageName, subscriptionId` | Delete storage for a connectedEnvironment. |
| `_list` | `EXEC` | `connectedEnvironmentName, resourceGroupName, subscriptionId` | Get all storages for a connectedEnvironment. |
