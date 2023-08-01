---
title: monitors
hide_title: false
hide_table_of_contents: false
keywords:
  - monitors
  - elastic
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
<tr><td><b>Name</b></td><td><code>monitors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.elastic.monitors</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ARM id of the monitor resource. |
| `name` | `string` | Name of the monitor resource. |
| `properties` | `object` | Properties specific to the monitor resource. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | The tags of the monitor resource. |
| `location` | `string` | The location of the monitor resource |
| `sku` | `object` | Microsoft.Elastic SKU. |
| `type` | `string` | The type of the monitor resource. |
| `identity` | `object` | Identity properties. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `Monitors_Get` | `SELECT` | `monitorName, resourceGroupName, subscriptionId` |
| `Monitors_List` | `SELECT` | `subscriptionId` |
| `Monitors_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` |
| `Monitors_Create` | `INSERT` | `monitorName, resourceGroupName, subscriptionId, data__location` |
| `Monitors_Delete` | `DELETE` | `monitorName, resourceGroupName, subscriptionId` |
| `Monitors_Update` | `EXEC` | `monitorName, resourceGroupName, subscriptionId` |
