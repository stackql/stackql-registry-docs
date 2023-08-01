---
title: operation
hide_title: false
hide_table_of_contents: false
keywords:
  - operation
  - saas
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
<tr><td><b>Name</b></td><td><code>operation</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.saas.operation</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource uri |
| `name` | `string` | The name of the resource |
| `tags` | `object` | the resource tags. |
| `type` | `string` | Resource type. |
| `properties` | `object` | saas properties |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `SaaSOperation_Get` | `SELECT` | `operationId` |
