---
title: directory_tenants
hide_title: false
hide_table_of_contents: false
keywords:
  - directory_tenants
  - subscriptions_admin
  - azure_stack    
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
<tr><td><b>Name</b></td><td><code>directory_tenants</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_stack.subscriptions_admin.directory_tenants</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | URI of the resource. |
| `name` | `string` | Name of the resource. |
| `location` | `string` | Location of the resource |
| `properties` | `object` | Directory tenant. |
| `tags` | `object` | List of key-value pairs. |
| `type` | `string` | Type of resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, subscriptionId, tenant` | Get a directory tenant by name. |
| `list` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all the directory tenants under the current subscription and given resource group name. |
| `create_or_update` | `INSERT` | `resourceGroupName, subscriptionId, tenant` | Create or updates a directory tenant. |
| `delete` | `DELETE` | `resourceGroupName, subscriptionId, tenant` | Delete a directory tenant under a resource group. |
| `_list` | `EXEC` | `resourceGroupName, subscriptionId` | Lists all the directory tenants under the current subscription and given resource group name. |
