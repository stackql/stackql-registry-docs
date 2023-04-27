---
title: views
hide_title: false
hide_table_of_contents: false
keywords:
  - views
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
<tr><td><b>Name</b></td><td><code>views</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.views</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `timestamp` | `string` |
| `uniques` | `integer` |
| `count` | `integer` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_views` | `SELECT` | `owner, repo` |
