---
title: status_check_contexts
hide_title: false
hide_table_of_contents: false
keywords:
  - status_check_contexts
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
<tr><td><b>Name</b></td><td><code>status_check_contexts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.status_check_contexts</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_all_status_check_contexts` | `SELECT` | `branch, owner, repo` |
| `add_status_check_contexts` | `INSERT` | `branch, owner, repo` |
| `remove_status_check_contexts` | `DELETE` | `branch, owner, repo` |
| `set_status_check_contexts` | `EXEC` | `branch, owner, repo` |
