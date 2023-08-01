---
title: commit_files
hide_title: false
hide_table_of_contents: false
keywords:
  - commit_files
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
<tr><td><b>Name</b></td><td><code>commit_files</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.commit_files</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `previous_filename` | `string` |
| `sha` | `string` |
| `contents_url` | `string` |
| `changes` | `integer` |
| `filename` | `string` |
| `blob_url` | `string` |
| `patch` | `string` |
| `additions` | `integer` |
| `status` | `string` |
| `deletions` | `integer` |
| `raw_url` | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_commit_files` | `SELECT` | `owner, ref, repo` |
