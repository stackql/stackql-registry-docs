---
title: virtual_appliance_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_appliance_connections
  - network
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
<tr><td><b>Name</b></td><td><code>virtual_appliance_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.virtual_appliance_connections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | The name of the resource. |
| `properties` | `object` | Properties of the NetworkVirtualApplianceConnection subresource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `connectionName, networkVirtualApplianceName, resourceGroupName, subscriptionId` | Retrieves the details of specified NVA connection. |
| `list` | `SELECT` | `networkVirtualApplianceName, resourceGroupName, subscriptionId` | Lists NetworkVirtualApplianceConnections under the NVA. |
| `create_or_update` | `INSERT` | `connectionName, networkVirtualApplianceName, resourceGroupName, subscriptionId` | Creates a connection to Network Virtual Appliance, if it doesn't exist else updates the existing NVA connection' |
| `delete` | `DELETE` | `connectionName, networkVirtualApplianceName, resourceGroupName, subscriptionId` | Deletes a NVA connection. |
| `_list` | `EXEC` | `networkVirtualApplianceName, resourceGroupName, subscriptionId` | Lists NetworkVirtualApplianceConnections under the NVA. |
