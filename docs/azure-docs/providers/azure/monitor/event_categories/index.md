---
title: event_categories
hide_title: false
hide_table_of_contents: false
keywords:
  - event_categories
  - monitor
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
<tr><td><b>Name</b></td><td><code>event_categories</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.monitor.event_categories</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `value` | `string` | the invariant value. |
| `localizedValue` | `string` | the locale specific value. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `EventCategories_List` | `SELECT` |  |
