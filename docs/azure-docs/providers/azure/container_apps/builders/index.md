---
title: builders
hide_title: false
hide_table_of_contents: false
keywords:
  - builders
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
<tr><td><b>Name</b></td><td><code>builders</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.container_apps.builders</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `identity` | `object` | Managed service identity (system assigned and/or user assigned identities) |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | The builder properties. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `builderName, resourceGroupName, subscriptionId` | Get a BuilderResource |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | List BuilderResource resources by resource group |
| `list_by_subscription` | `SELECT` | `subscriptionId` | List BuilderResource resources by subscription ID |
| `create_or_update` | `INSERT` | `builderName, resourceGroupName, subscriptionId` | Create or update a BuilderResource |
| `delete` | `DELETE` | `builderName, resourceGroupName, subscriptionId` | Delete a BuilderResource |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | List BuilderResource resources by resource group |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | List BuilderResource resources by subscription ID |
| `update` | `EXEC` | `builderName, resourceGroupName, subscriptionId` | Update a BuilderResource |
