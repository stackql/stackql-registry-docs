---
title: kernels
hide_title: false
hide_table_of_contents: false
keywords:
  - kernels
  - droplets
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
<tr><td><b>Name</b></td><td><code>kernels</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>digitalocean.droplets.kernels</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | A unique number used to identify and reference a specific kernel. |
| `name` | `string` | The display name of the kernel. This is shown in the web UI and is generally a descriptive title for the kernel in question. |
| `version` | `string` | A standard kernel version string representing the version, patch, and release information. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_kernels` | `SELECT` | `droplet_id` |
| `_list_kernels` | `EXEC` | `droplet_id` |
