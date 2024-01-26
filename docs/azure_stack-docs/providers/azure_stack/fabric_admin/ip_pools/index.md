---
title: ip_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - ip_pools
  - fabric_admin
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
<tr><td><b>Name</b></td><td><code>ip_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_stack.fabric_admin.ip_pools</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | URI of the resource. |
| `name` | `string` | Name of the resource. |
| `location` | `string` | The region where the resource is located. |
| `properties` | `object` | Properties of an IpPool. |
| `tags` | `object` | List of key-value pairs. |
| `type` | `string` | Type of resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `ipPool, location, resourceGroupName, subscriptionId` | Return the requested IP pool. |
| `list` | `SELECT` | `location, resourceGroupName, subscriptionId` | Returns a list of all IP pools at a certain location. |
| `create_or_update` | `INSERT` | `ipPool, location, resourceGroupName, subscriptionId` | Create an IP pool.  Once created an IP pool cannot be deleted. |
| `_list` | `EXEC` | `location, resourceGroupName, subscriptionId` | Returns a list of all IP pools at a certain location. |
