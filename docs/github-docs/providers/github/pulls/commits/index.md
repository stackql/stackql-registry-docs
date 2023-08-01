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
| `commit` | `object` |  |
| `committer` | `object` | Simple User |
| `url` | `string` |  |
| `stats` | `object` |  |
| `node_id` | `string` |  |
| `comments_url` | `string` |  |
| `html_url` | `string` |  |
| `sha` | `string` |  |
| `parents` | `array` |  |
| `author` | `object` | Simple User |
| `files` | `array` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_commits` | `SELECT` | `owner, pull_number, repo` |
