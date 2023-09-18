---
title: content_tree
hide_title: false
hide_table_of_contents: false
keywords:
  - content_tree
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
<tr><td><b>Name</b></td><td><code>content_tree</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.content_tree</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `name` | `string` |
| `submodule_git_url` | `string` |
| `content-symlink_sha` | `string` |
| `type` | `string` |
| `content-symlink_type` | `string` |
| `content-symlink_target` | `string` |
| `html_url` | `string` |
| `content-submodule_size` | `integer` |
| `content` | `string` |
| `content-symlink_name` | `string` |
| `content-submodule_type` | `string` |
| `size` | `integer` |
| `content-submodule_url` | `string` |
| `content-submodule__links` | `object` |
| `content-symlink_size` | `integer` |
| `path` | `string` |
| `content-submodule_submodule_git_url` | `string` |
| `encoding` | `string` |
| `content-symlink_download_url` | `string` |
| `content-symlink__links` | `object` |
| `content-symlink_path` | `string` |
| `content-symlink_url` | `string` |
| `download_url` | `string` |
| `content-symlink_git_url` | `string` |
| `content-submodule_sha` | `string` |
| `content-submodule_name` | `string` |
| `_links` | `object` |
| `content-submodule_git_url` | `string` |
| `content-symlink_html_url` | `string` |
| `content-submodule_path` | `string` |
| `content-submodule_html_url` | `string` |
| `content-submodule_download_url` | `string` |
| `sha` | `string` |
| `target` | `string` |
| `url` | `string` |
| `git_url` | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_content` | `SELECT` | `owner, path, repo` |
