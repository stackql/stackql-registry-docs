---
title: factories
hide_title: false
hide_table_of_contents: false
keywords:
  - factories
  - data_factory
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
<tr><td><b>Name</b></td><td><code>factories</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.data_factory.factories</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource identifier. |
| `name` | `string` | The resource name. |
| `eTag` | `string` | Etag identifies change in the resource. |
| `identity` | `object` | Identity properties of the factory resource. |
| `location` | `string` | The resource location. |
| `properties` | `object` | Factory resource properties. |
| `tags` | `object` | The resource tags. |
| `type` | `string` | The resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `api-version, factoryName, resourceGroupName, subscriptionId` | Gets a factory. |
| `list` | `SELECT` | `api-version, subscriptionId` | Lists factories under the specified subscription. |
| `list_by_resource_group` | `SELECT` | `api-version, resourceGroupName, subscriptionId` | Lists factories. |
| `create_or_update` | `INSERT` | `api-version, factoryName, resourceGroupName, subscriptionId` | Creates or updates a factory. |
| `delete` | `DELETE` | `api-version, factoryName, resourceGroupName, subscriptionId` | Deletes a factory. |
| `_list` | `EXEC` | `api-version, subscriptionId` | Lists factories under the specified subscription. |
| `_list_by_resource_group` | `EXEC` | `api-version, resourceGroupName, subscriptionId` | Lists factories. |
| `configure_factory_repo` | `EXEC` | `api-version, locationId, subscriptionId` | Updates a factory's repo information. |
| `update` | `EXEC` | `api-version, factoryName, resourceGroupName, subscriptionId` | Updates a factory. |
