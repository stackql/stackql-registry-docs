---
title: instances
hide_title: false
hide_table_of_contents: false
keywords:
  - instances
  - device_update
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
<tr><td><b>Name</b></td><td><code>instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.device_update.instances</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Device Update instance properties. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `accountName, instanceName, resourceGroupName, subscriptionId` | Returns instance details for the given instance and account name. |
| `list_by_account` | `SELECT` | `accountName, resourceGroupName, subscriptionId` | Returns instances for the given account name. |
| `create` | `INSERT` | `accountName, instanceName, resourceGroupName, subscriptionId, data__properties` | Creates or updates instance. |
| `delete` | `DELETE` | `accountName, instanceName, resourceGroupName, subscriptionId` | Deletes instance. |
| `_list_by_account` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Returns instances for the given account name. |
| `head` | `EXEC` | `accountName, instanceName, resourceGroupName, subscriptionId` | Checks whether instance exists. |
| `update` | `EXEC` | `accountName, instanceName, resourceGroupName, subscriptionId` | Updates instance's tags. |
