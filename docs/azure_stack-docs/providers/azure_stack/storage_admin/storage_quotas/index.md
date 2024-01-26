---
title: storage_quotas
hide_title: false
hide_table_of_contents: false
keywords:
  - storage_quotas
  - storage_admin
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
<tr><td><b>Name</b></td><td><code>storage_quotas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_stack.storage_admin.storage_quotas</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource Name. |
| `location` | `string` | Resource Location. |
| `properties` | `object` | Storage quota properties. |
| `type` | `string` | Resource Type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `location, quotaName, subscriptionId` | Returns the specified storage quota. |
| `list` | `SELECT` | `location, subscriptionId` | Returns a list of storage quotas at the given location. |
| `create_or_update` | `INSERT` | `location, quotaName, subscriptionId` | Create or update an existing storage quota. |
| `delete` | `DELETE` | `location, quotaName, subscriptionId` | Delete an existing quota |
| `_list` | `EXEC` | `location, subscriptionId` | Returns a list of storage quotas at the given location. |
