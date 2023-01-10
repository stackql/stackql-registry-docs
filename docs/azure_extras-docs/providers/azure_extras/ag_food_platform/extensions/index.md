---
title: extensions
hide_title: false
hide_table_of_contents: false
keywords:
  - extensions
  - ag_food_platform
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
<tr><td><b>Name</b></td><td><code>extensions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.ag_food_platform.extensions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `eTag` | `string` | The ETag value to implement optimistic concurrency. |
| `properties` | `object` | Extension resource properties. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Extensions_Get` | `SELECT` | `extensionId, farmBeatsResourceName, resourceGroupName, subscriptionId` | Get installed extension details by extension id. |
| `Extensions_ListByFarmBeats` | `SELECT` | `farmBeatsResourceName, resourceGroupName, subscriptionId` | Get installed extensions details. |
| `Extensions_Create` | `INSERT` | `extensionId, farmBeatsResourceName, resourceGroupName, subscriptionId` | Install extension. |
| `Extensions_Delete` | `DELETE` | `extensionId, farmBeatsResourceName, resourceGroupName, subscriptionId` | Uninstall extension. |
| `Extensions_Update` | `EXEC` | `extensionId, farmBeatsResourceName, resourceGroupName, subscriptionId` | Upgrade to latest extension. |
