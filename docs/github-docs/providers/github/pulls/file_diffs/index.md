---
title: file_diffs
hide_title: false
hide_table_of_contents: false
keywords:
  - file_diffs
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
<tr><td><b>Name</b></td><td><code>file_diffs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.pulls.file_diffs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `previous_filename` | `string` |
| `sha` | `string` |
| `blob_url` | `string` |
| `deletions` | `integer` |
| `patch` | `string` |
| `raw_url` | `string` |
| `contents_url` | `string` |
| `filename` | `string` |
| `changes` | `integer` |
| `additions` | `integer` |
| `status` | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_files` | `SELECT` | `owner, pull_number, repo` |
