---
title: operations
hide_title: false
hide_table_of_contents: false
keywords:
  - operations
  - blockchain
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
<tr><td><b>Id</b></td><td><code>azure_extras.blockchain.operations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Gets or sets the operation name. |
| `display` | `object` | Operation display payload which is exposed in the response of the resource provider. |
| `isDataAction` | `boolean` | Gets or sets a value indicating whether the operation is a data action or not. |
| `origin` | `string` | Gets or sets the origin. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `Operations_List` | `SELECT` |  |
