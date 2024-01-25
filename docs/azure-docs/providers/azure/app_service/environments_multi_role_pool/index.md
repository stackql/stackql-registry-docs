---
title: environments_multi_role_pool
hide_title: false
hide_table_of_contents: false
keywords:
  - environments_multi_role_pool
  - app_service
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
<tr><td><b>Name</b></td><td><code>environments_multi_role_pool</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.app_service.environments_multi_role_pool</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id. |
| `name` | `string` | Resource Name. |
| `kind` | `string` | Kind of resource. |
| `properties` | `object` | Worker pool of an App Service Environment. |
| `sku` | `object` | Description of a SKU for a scalable resource. |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `name, resourceGroupName, subscriptionId` | Description for Get properties of a multi-role pool. |
| `create_or_update` | `INSERT` | `name, resourceGroupName, subscriptionId` | Description for Create or update a multi-role pool. |
| `update` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Create or update a multi-role pool. |
