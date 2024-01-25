---
title: operations
hide_title: false
hide_table_of_contents: false
keywords:
  - operations
  - customer_lockbox
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
<tr><td><b>Id</b></td><td><code>azure.customer_lockbox.operations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Gets or sets action name |
| `display` | `object` | Contains the localized display information for this particular operation / action. |
| `isDataAction` | `string` | Gets or sets a value indicating whether it is a data plane action |
| `origin` | `string` | Gets or sets origin |
| `properties` | `string` | Gets or sets properties |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` |  |
| `_list` | `EXEC` |  |
