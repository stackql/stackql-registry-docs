---
title: operations
hide_title: false
hide_table_of_contents: false
keywords:
  - operations
  - app_platform
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
<tr><td><b>Name</b></td><td><code>operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.app_platform.operations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Name of the operation |
| `properties` | `object` | Extra Operation properties |
| `actionType` | `string` | Enum. Indicates the action type. "Internal" refers to actions that are for internal only APIs. |
| `display` | `object` | Operation display payload |
| `isDataAction` | `boolean` | Indicates whether the operation is a data action |
| `origin` | `string` | Origin of the operation |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `Operations_List` | `SELECT` |  |
