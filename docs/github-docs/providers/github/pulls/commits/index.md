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
| `sha` | `string` |  |
| `url` | `string` |  |
| `committer` | `object` | Simple User |
| `files` | `array` |  |
| `node_id` | `string` |  |
| `comments_url` | `string` |  |
| `commit` | `object` |  |
| `author` | `object` | Simple User |
| `stats` | `object` |  |
| `parents` | `array` |  |
| `html_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_commits` | `SELECT` | `owner, pull_number, repo` |
