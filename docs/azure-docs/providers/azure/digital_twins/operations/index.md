---
title: operations
hide_title: false
hide_table_of_contents: false
keywords:
  - operations
  - digital_twins
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
<tr><td><b>Id</b></td><td><code>azure.digital_twins.operations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Operation name: &#123;provider&#125;/&#123;resource&#125;/&#123;read \| write \| action \| delete&#125; |
| `display` | `object` | The object that represents the operation. |
| `isDataAction` | `boolean` | If the operation is a data action (for data plane rbac). |
| `origin` | `string` | The intended executor of the operation. |
| `properties` | `object` | Operation properties. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `api-version` |
| `_list` | `EXEC` | `api-version` |
