---
title: quota
hide_title: false
hide_table_of_contents: false
keywords:
  - quota
  - fields
  - sumologic    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Sumologic resources using SQL
custom_edit_url: null
image: /img/providers/sumologic/stackql-sumologic-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>quota</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>sumologic.fields.quota</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `quota` | `integer` | Maximum number of fields available. |
| `remaining` | `integer` | Current number of fields available. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `getFieldQuota` | `SELECT` | `region` |
