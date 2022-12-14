---
title: operations
hide_title: false
hide_table_of_contents: false
keywords:
  - operations
  - iot_central
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
<tr><td><b>Id</b></td><td><code>azure.iot_central.operations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Operation name: &#123;provider&#125;/&#123;resource&#125;/&#123;read \| write \| action \| delete&#125; |
| `display` | `object` | The object that represents the operation. |
| `origin` | `string` | The intended executor of the operation. |
| `properties` | `object` | Additional descriptions for the operation. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `Operations_List` | `SELECT` | `api-version` |
