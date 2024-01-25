---
title: configuration_stores
hide_title: false
hide_table_of_contents: false
keywords:
  - configuration_stores
  - app_configuration
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
<tr><td><b>Name</b></td><td><code>configuration_stores</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.app_configuration.configuration_stores</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `identity` | `object` | An identity that can be associated with a resource. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | The properties of a configuration store. |
| `sku` | `object` | The resource model definition representing SKU |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `configStoreName, resourceGroupName, subscriptionId` | Gets the properties of the specified configuration store. |
| `list` | `SELECT` | `subscriptionId` | Lists the configuration stores for a given subscription. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Lists the configuration stores for a given resource group. |
| `create` | `INSERT` | `configStoreName, resourceGroupName, subscriptionId, data__location, data__sku` | Creates a configuration store with the specified parameters. |
| `delete` | `DELETE` | `configStoreName, resourceGroupName, subscriptionId` | Deletes a configuration store. |
| `_list` | `EXEC` | `subscriptionId` | Lists the configuration stores for a given subscription. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Lists the configuration stores for a given resource group. |
| `purge_deleted` | `EXEC` | `configStoreName, location, subscriptionId` | Permanently deletes the specified configuration store. |
| `regenerate_key` | `EXEC` | `configStoreName, resourceGroupName, subscriptionId` | Regenerates an access key for the specified configuration store. |
| `update` | `EXEC` | `configStoreName, resourceGroupName, subscriptionId` | Updates a configuration store with the specified parameters. |
