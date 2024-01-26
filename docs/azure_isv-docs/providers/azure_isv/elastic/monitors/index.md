---
title: monitors
hide_title: false
hide_table_of_contents: false
keywords:
  - monitors
  - elastic
  - azure_isv    
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
<tr><td><b>Id</b></td><td><code>azure_isv.elastic.monitors</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ARM id of the monitor resource. |
| `name` | `string` | Name of the monitor resource. |
| `identity` | `object` | Identity properties. |
| `location` | `string` | The location of the monitor resource |
| `properties` | `object` | Properties specific to the monitor resource. |
| `sku` | `object` | Microsoft.Elastic SKU. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | The tags of the monitor resource. |
| `type` | `string` | The type of the monitor resource. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `monitorName, resourceGroupName, subscriptionId` |
| `list` | `SELECT` | `subscriptionId` |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` |
| `create` | `INSERT` | `monitorName, resourceGroupName, subscriptionId, data__location` |
| `delete` | `DELETE` | `monitorName, resourceGroupName, subscriptionId` |
| `_list` | `EXEC` | `subscriptionId` |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` |
| `update` | `EXEC` | `monitorName, resourceGroupName, subscriptionId` |
| `upgrade` | `EXEC` | `monitorName, resourceGroupName, subscriptionId` |
