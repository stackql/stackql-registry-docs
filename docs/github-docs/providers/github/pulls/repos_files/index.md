---
title: repos_files
hide_title: false
hide_table_of_contents: false
keywords:
  - repos_files
  - pulls
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
<tr><td><b>Name</b></td><td><code>repos_files</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.pulls.repos_files</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `deletions` | `integer` |
| `raw_url` | `string` |
| `sha` | `string` |
| `blob_url` | `string` |
| `contents_url` | `string` |
| `status` | `string` |
| `filename` | `string` |
| `previous_filename` | `string` |
| `additions` | `integer` |
| `changes` | `integer` |
| `patch` | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_files` | `SELECT` | `owner, pull_number, repo` |
