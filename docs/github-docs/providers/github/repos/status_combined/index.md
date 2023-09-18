---
title: status_combined
hide_title: false
hide_table_of_contents: false
keywords:
  - status_combined
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
<tr><td><b>Name</b></td><td><code>status_combined</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.status_combined</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `url` | `string` |  |
| `commit_url` | `string` |  |
| `repository` | `object` | Minimal Repository |
| `sha` | `string` |  |
| `state` | `string` |  |
| `statuses` | `array` |  |
| `total_count` | `integer` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_combined_status_for_ref` | `SELECT` | `owner, ref, repo` |
