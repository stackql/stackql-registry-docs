---
title: pages_health_check
hide_title: false
hide_table_of_contents: false
keywords:
  - pages_health_check
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
<tr><td><b>Name</b></td><td><code>pages_health_check</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.pages_health_check</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `domain` | `object` |
| `alt_domain` | `object` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_pages_health_check` | `SELECT` | `owner, repo` |
