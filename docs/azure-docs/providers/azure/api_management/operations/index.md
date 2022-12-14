---
title: operations
hide_title: false
hide_table_of_contents: false
keywords:
  - operations
  - api_management
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
<tr><td><b>Id</b></td><td><code>azure.api_management.operations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Operation name: &#123;provider&#125;/&#123;resource&#125;/&#123;operation&#125; |
| `display` | `` | The object that describes the operation. |
| `origin` | `string` | The operation origin. |
| `properties` | `object` | The operation properties. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `ApiManagementOperations_List` | `SELECT` |  |
