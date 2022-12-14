---
title: entities
hide_title: false
hide_table_of_contents: false
keywords:
  - entities
  - management_groups
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
<tr><td><b>Name</b></td><td><code>entities</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.management_groups.entities</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextLink` | `string` | The URL to use for getting the next set of results. |
| `value` | `array` | The list of entities. |
| `count` | `integer` | Total count of records that match the filter |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `Entities_List` | `SELECT` |  |
