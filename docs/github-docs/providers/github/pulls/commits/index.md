---
title: commits
hide_title: false
hide_table_of_contents: false
keywords:
  - commits
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
<tr><td><b>Name</b></td><td><code>commits</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.pulls.commits</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `comments_url` | `string` |  |
| `committer` | `object` | A GitHub user. |
| `node_id` | `string` |  |
| `html_url` | `string` |  |
| `sha` | `string` |  |
| `url` | `string` |  |
| `files` | `array` |  |
| `stats` | `object` |  |
| `commit` | `object` |  |
| `parents` | `array` |  |
| `author` | `object` | A GitHub user. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_commits` | `SELECT` | `owner, pull_number, repo` |
