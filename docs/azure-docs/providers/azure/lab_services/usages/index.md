---
title: usages
hide_title: false
hide_table_of_contents: false
keywords:
  - usages
  - lab_services
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
<tr><td><b>Name</b></td><td><code>usages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.lab_services.usages</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The fully qualified arm resource id. |
| `name` | `object` | The Usage Names. |
| `currentValue` | `integer` | The current usage. |
| `limit` | `integer` | The limit integer. |
| `unit` | `string` | The unit details. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_by_location` | `SELECT` |  |
| `_list_by_location` | `EXEC` |  |
