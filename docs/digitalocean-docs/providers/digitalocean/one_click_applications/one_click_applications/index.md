---
title: one_click_applications
hide_title: false
hide_table_of_contents: false
keywords:
  - one_click_applications
  - one_click_applications
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
<tr><td><b>Name</b></td><td><code>one_click_applications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>digitalocean.one_click_applications.one_click_applications</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `slug` | `string` | The slug identifier for the 1-Click application. |
| `type` | `string` | The type of the 1-Click application. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `oneClicks_list` | `SELECT` |  |
| `_oneClicks_list` | `EXEC` |  |
