---
title: instances
hide_title: false
hide_table_of_contents: false
keywords:
  - instances
  - device_update
  - azure_extras    
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
<tr><td><b>Id</b></td><td><code>azure_extras.device_update.instances</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `tags` | `object` | Resource tags. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Device Update instance properties. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Instances_Get` | `SELECT` | `accountName, instanceName, resourceGroupName, subscriptionId` | Returns instance details for the given instance and account name. |
| `Instances_ListByAccount` | `SELECT` | `accountName, resourceGroupName, subscriptionId` | Returns instances for the given account name. |
| `Instances_Create` | `INSERT` | `accountName, instanceName, resourceGroupName, subscriptionId, data__properties` | Creates or updates instance. |
| `Instances_Delete` | `DELETE` | `accountName, instanceName, resourceGroupName, subscriptionId` | Deletes instance. |
| `Instances_Head` | `EXEC` | `accountName, instanceName, resourceGroupName, subscriptionId` | Checks whether instance exists. |
| `Instances_Update` | `EXEC` | `accountName, instanceName, resourceGroupName, subscriptionId` | Updates instance's tags. |
