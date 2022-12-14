---
title: managed_environments_storages
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_environments_storages
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
<tr><td><b>Name</b></td><td><code>managed_environments_storages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.container_apps.managed_environments_storages</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ManagedEnvironmentsStorages_Get` | `SELECT` | `environmentName, resourceGroupName, storageName, subscriptionId` | Get storage for a managedEnvironment. |
| `ManagedEnvironmentsStorages_List` | `SELECT` | `environmentName, resourceGroupName, subscriptionId` | Get all storages for a managedEnvironment. |
| `ManagedEnvironmentsStorages_CreateOrUpdate` | `INSERT` | `environmentName, resourceGroupName, storageName, subscriptionId` | Create or update storage for a managedEnvironment. |
| `ManagedEnvironmentsStorages_Delete` | `DELETE` | `environmentName, resourceGroupName, storageName, subscriptionId` | Delete storage for a managedEnvironment. |
