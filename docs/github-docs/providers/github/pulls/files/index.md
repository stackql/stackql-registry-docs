---
title: files
hide_title: false
hide_table_of_contents: false
keywords:
  - files
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
<tr><td><b>Name</b></td><td><code>files</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.pulls.files</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `previous_filename` | `string` |
| `blob_url` | `string` |
| `sha` | `string` |
| `changes` | `integer` |
| `additions` | `integer` |
| `filename` | `string` |
| `raw_url` | `string` |
| `patch` | `string` |
| `deletions` | `integer` |
| `contents_url` | `string` |
| `status` | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_files` | `SELECT` | `owner, pull_number, repo` |
