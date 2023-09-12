---
title: repos_matching_refs
hide_title: false
hide_table_of_contents: false
keywords:
  - repos_matching_refs
  - git
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
<tr><td><b>Name</b></td><td><code>repos_matching_refs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.git.repos_matching_refs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `node_id` | `string` |
| `object` | `object` |
| `ref` | `string` |
| `url` | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_matching_refs` | `SELECT` | `owner, ref, repo` |
