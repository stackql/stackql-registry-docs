---
title: services
hide_title: false
hide_table_of_contents: false
keywords:
  - services
  - api_center
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
<tr><td><b>Name</b></td><td><code>services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_center.services</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `identity` | `object` | Managed service identity (system assigned and/or user assigned identities) |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | The properties of the service. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, serviceName, subscriptionId` | Returns details of the service. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Returns a collection of services within the resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Lists services within an Azure subscription. |
| `create_or_update` | `INSERT` | `resourceGroupName, serviceName, subscriptionId` | Creates new or updates existing API. |
| `delete` | `DELETE` | `resourceGroupName, serviceName, subscriptionId` | Deletes specified service. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Returns a collection of services within the resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Lists services within an Azure subscription. |
| `export_metadata_schema` | `EXEC` |  | Exports the effective metadata schema. |
| `update` | `EXEC` | `resourceGroupName, serviceName, subscriptionId` | Updates existing service. |
