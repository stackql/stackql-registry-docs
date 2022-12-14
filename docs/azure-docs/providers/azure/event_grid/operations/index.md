---
title: operations
hide_title: false
hide_table_of_contents: false
keywords:
  - operations
  - event_grid
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
<tr><td><b>Name</b></td><td><code>operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.event_grid.operations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Name of the operation. |
| `origin` | `string` | Origin of the operation. |
| `properties` | `object` | Properties of the operation. |
| `display` | `object` | Information about an operation |
| `isDataAction` | `boolean` | This Boolean is used to determine if the operation is a data plane action or not. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `Operations_List` | `SELECT` |  |
