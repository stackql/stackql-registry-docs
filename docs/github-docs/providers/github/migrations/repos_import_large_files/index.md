---
title: repos_import_large_files
hide_title: false
hide_table_of_contents: false
keywords:
  - repos_import_large_files
  - migrations
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
<tr><td><b>Name</b></td><td><code>repos_import_large_files</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.migrations.repos_import_large_files</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `size` | `integer` |
| `oid` | `string` |
| `path` | `string` |
| `ref_name` | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_large_files` | `SELECT` | `owner, repo` |
