---
title: operations
hide_title: false
hide_table_of_contents: false
keywords:
  - operations
  - confidential_ledger
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
<tr><td><b>Id</b></td><td><code>azure.confidential_ledger.operations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Resource provider operation name. |
| `display` | `object` | Describes the properties of the Operation. |
| `isDataAction` | `boolean` | Indicates whether the operation is data action or not. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` |  |
| `_list` | `EXEC` |  |
