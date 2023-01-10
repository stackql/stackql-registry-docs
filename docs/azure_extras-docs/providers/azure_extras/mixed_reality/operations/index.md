---
title: operations
hide_title: false
hide_table_of_contents: false
keywords:
  - operations
  - mixed_reality
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
<tr><td><b>Id</b></td><td><code>azure_extras.mixed_reality.operations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Operation name: &#123;provider&#125;/&#123;resource&#125;/&#123;operation&#125; |
| `origin` | `string` | The origin |
| `properties` | `object` | Operation properties. |
| `display` | `object` | The object that represents the operation. |
| `isDataAction` | `boolean` | Whether or not this is a data plane operation |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `Operations_List` | `SELECT` |  |