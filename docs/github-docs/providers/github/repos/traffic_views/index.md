---
title: traffic_views
hide_title: false
hide_table_of_contents: false
keywords:
  - traffic_views
  - repos
  - github    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GitHub resources using SQL
custom_edit_url: null
image: /img/providers/github/stackql-github-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>traffic_views</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.traffic_views</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `count` | `integer` |
| `uniques` | `integer` |
| `views` | `array` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_views` | `SELECT` | `owner, repo` |
