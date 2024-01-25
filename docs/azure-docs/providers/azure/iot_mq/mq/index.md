---
title: mq
hide_title: false
hide_table_of_contents: false
keywords:
  - mq
  - iot_mq
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
<tr><td><b>Name</b></td><td><code>mq</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.iot_mq.mq</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `extendedLocation` | `object` | ExtendedLocation properties |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | MQ Resource properties |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `mqName, resourceGroupName, subscriptionId` | Get a MqResource |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | List MqResource resources by resource group |
| `list_by_subscription` | `SELECT` | `subscriptionId` | List MqResource resources by subscription ID |
| `create_or_update` | `INSERT` | `mqName, resourceGroupName, subscriptionId, data__extendedLocation` | Create a MqResource |
| `delete` | `DELETE` | `mqName, resourceGroupName, subscriptionId` | Delete a MqResource |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | List MqResource resources by resource group |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | List MqResource resources by subscription ID |
| `update` | `EXEC` | `mqName, resourceGroupName, subscriptionId` | Update a MqResource |
