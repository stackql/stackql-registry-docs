---
title: page_build_latest
hide_title: false
hide_table_of_contents: false
keywords:
  - page_build_latest
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
<tr><td><b>Name</b></td><td><code>page_build_latest</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.page_build_latest</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `url` | `string` |  |
| `commit` | `string` |  |
| `created_at` | `string` |  |
| `duration` | `integer` |  |
| `error` | `object` |  |
| `pusher` | `object` | A GitHub user. |
| `status` | `string` |  |
| `updated_at` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_latest_pages_build` | `SELECT` | `owner, repo` |
