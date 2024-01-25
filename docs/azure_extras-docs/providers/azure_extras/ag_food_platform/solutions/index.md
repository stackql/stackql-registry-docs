---
title: solutions
hide_title: false
hide_table_of_contents: false
keywords:
  - solutions
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
<tr><td><b>Name</b></td><td><code>solutions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.ag_food_platform.solutions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `eTag` | `string` | The ETag value to implement optimistic concurrency. |
| `properties` | `object` | Solution resource properties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `dataManagerForAgricultureResourceName, resourceGroupName, solutionId, subscriptionId` | Get installed Solution details by Solution id. |
| `list` | `SELECT` | `dataManagerForAgricultureResourceName, resourceGroupName, subscriptionId` | Get installed Solutions details. |
| `create_or_update` | `INSERT` | `dataManagerForAgricultureResourceName, resourceGroupName, solutionId, subscriptionId` | Install Or Update Solution. |
| `delete` | `DELETE` | `dataManagerForAgricultureResourceName, resourceGroupName, solutionId, subscriptionId` | Uninstall Solution. |
| `_list` | `EXEC` | `dataManagerForAgricultureResourceName, resourceGroupName, subscriptionId` | Get installed Solutions details. |
