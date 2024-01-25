---
title: managers_extended_info
hide_title: false
hide_table_of_contents: false
keywords:
  - managers_extended_info
  - storsimple_1200_series
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
<tr><td><b>Name</b></td><td><code>managers_extended_info</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.storsimple_1200_series.managers_extended_info</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The identifier. |
| `name` | `string` | The name. |
| `etag` | `string` | ETag of the Resource |
| `properties` | `object` | Properties of the ManagerExtendedInfo |
| `type` | `string` | The type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `managerName, resourceGroupName, subscriptionId` | Returns the extended information of the specified manager name. |
| `create` | `INSERT` | `managerName, resourceGroupName, subscriptionId, data__properties` | Creates the extended info of the manager. |
| `delete` | `DELETE` | `managerName, resourceGroupName, subscriptionId` | Deletes the extended info of the manager. |
| `update` | `EXEC` | `If-Match, managerName, resourceGroupName, subscriptionId, data__properties` | Updates the extended info of the manager. |
