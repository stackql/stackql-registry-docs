---
title: usages
hide_title: false
hide_table_of_contents: false
keywords:
  - usages
  - dev_center
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
<tr><td><b>Name</b></td><td><code>usages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.dev_center.usages</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `object` | The Usage Names. |
| `unit` | `string` | The unit details. |
| `currentValue` | `integer` | The current usage. |
| `limit` | `integer` | The limit integer. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `Usages_ListByLocation` | `SELECT` | `location, subscriptionId` |
