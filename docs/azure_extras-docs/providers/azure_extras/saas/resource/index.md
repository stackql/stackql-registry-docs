---
title: resource
hide_title: false
hide_table_of_contents: false
keywords:
  - resource
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
<tr><td><b>Name</b></td><td><code>resource</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.saas.resource</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource uri |
| `name` | `string` | The name of the resource |
| `properties` | `object` | saas properties |
| `tags` | `object` | the resource tags. |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceId` | Gets information about the specified SaaS. |
| `create` | `INSERT` |  | Creates a SaaS resource. |
| `update` | `EXEC` | `resourceId` | Updates a SaaS resource. |
