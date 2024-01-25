---
title: resource_health_metadata
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_health_metadata
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
<tr><td><b>Name</b></td><td><code>resource_health_metadata</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.app_service.resource_health_metadata</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id. |
| `name` | `string` | Resource Name. |
| `kind` | `string` | Kind of resource. |
| `properties` | `object` | ResourceHealthMetadata resource specific properties |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list` | `SELECT` | `subscriptionId` | Description for List all ResourceHealthMetadata for all sites in the subscription. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Description for List all ResourceHealthMetadata for all sites in the resource group in the subscription. |
| `list_by_site` | `SELECT` | `name, resourceGroupName, subscriptionId` | Description for Gets the category of ResourceHealthMetadata to use for the given site as a collection |
| `list_by_site_slot` | `SELECT` | `name, resourceGroupName, slot, subscriptionId` | Description for Gets the category of ResourceHealthMetadata to use for the given site as a collection |
| `_list` | `EXEC` | `subscriptionId` | Description for List all ResourceHealthMetadata for all sites in the subscription. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Description for List all ResourceHealthMetadata for all sites in the resource group in the subscription. |
| `_list_by_site` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Gets the category of ResourceHealthMetadata to use for the given site as a collection |
| `_list_by_site_slot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Gets the category of ResourceHealthMetadata to use for the given site as a collection |
| `get_by_site` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Gets the category of ResourceHealthMetadata to use for the given site |
| `get_by_site_slot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Gets the category of ResourceHealthMetadata to use for the given site |
