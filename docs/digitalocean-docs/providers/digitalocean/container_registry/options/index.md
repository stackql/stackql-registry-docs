---
title: options
hide_title: false
hide_table_of_contents: false
keywords:
  - options
  - container_registry
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
<tr><td><b>Name</b></td><td><code>options</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>digitalocean.container_registry.options</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `available_regions` | `array` |
| `subscription_tiers` | `array` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `registry_get_options` | `SELECT` |  |
| `_registry_get_options` | `EXEC` |  |
