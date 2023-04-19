---
title: regions
hide_title: false
hide_table_of_contents: false
keywords:
  - regions
  - regions
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
<tr><td><b>Id</b></td><td><code>digitalocean.regions.regions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The display name of the region.  This will be a full name that is used in the control panel and other interfaces. |
| `sizes` | `` | This attribute is set to an array which contains the identifying slugs for the sizes available in this region. |
| `slug` | `string` | A human-readable string that is used as a unique identifier for each region. |
| `available` | `boolean` | This is a boolean value that represents whether new Droplets can be created in this region. |
| `features` | `` | This attribute is set to an array which contains features available in this region |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` |  |
| `_list` | `EXEC` |  |
