---
title: regions
hide_title: false
hide_table_of_contents: false
keywords:
  - regions
  - apps
  - digitalocean    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Sumologic resources using SQL
custom_edit_url: null
image: /img/providers/digitalocean/stackql-digitalocean-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>regions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>digitalocean.apps.regions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `continent` | `string` |  |
| `data_centers` | `array` |  |
| `default` | `boolean` | Whether or not the region is presented as the default. |
| `disabled` | `boolean` |  |
| `flag` | `string` |  |
| `label` | `string` |  |
| `reason` | `string` |  |
| `slug` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_regions` | `SELECT` |  |
| `_list_regions` | `EXEC` |  |
