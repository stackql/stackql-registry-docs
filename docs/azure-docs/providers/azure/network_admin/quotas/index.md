---
title: quotas
hide_title: false
hide_table_of_contents: false
keywords:
  - quotas
  - network_admin
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
<tr><td><b>Name</b></td><td><code>quotas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network_admin.quotas</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | URI of the resource. |
| `name` | `string` | Name of the resource. |
| `type` | `string` | Type of resource. |
| `location` | `string` | Region location of resource. |
| `properties` | `object` | Properties of a quota. |
| `tags` | `object` | List of key value pairs. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Quotas_Get` | `SELECT` | `location, resourceName, subscriptionId` | Get a quota by name. |
| `Quotas_List` | `SELECT` | `location, subscriptionId` | List all quotas. |
| `Quotas_CreateOrUpdate` | `INSERT` | `location, resourceName, subscriptionId` | Create or update a quota. |
| `Quotas_Delete` | `DELETE` | `location, resourceName, subscriptionId` | Delete a quota by name. |
