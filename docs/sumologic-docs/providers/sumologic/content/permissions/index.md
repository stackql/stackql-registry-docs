---
title: permissions
hide_title: false
hide_table_of_contents: false
keywords:
  - permissions
  - content
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
<tr><td><b>Name</b></td><td><code>permissions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>sumologic.content.permissions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `explicitPermissions` | `array` | Explicitly assigned content permissions. |
| `implicitPermissions` | `array` | Implicitly inherited content permissions. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `getContentPermissions` | `SELECT` | `id, region` |
