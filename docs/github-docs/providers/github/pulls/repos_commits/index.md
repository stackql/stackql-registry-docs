---
title: repos_commits
hide_title: false
hide_table_of_contents: false
keywords:
  - repos_commits
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
<tr><td><b>Name</b></td><td><code>repos_commits</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.pulls.repos_commits</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `sha` | `string` |  |
| `html_url` | `string` |  |
| `committer` | `object` | A GitHub user. |
| `commit` | `object` |  |
| `parents` | `array` |  |
| `stats` | `object` |  |
| `author` | `object` | A GitHub user. |
| `files` | `array` |  |
| `node_id` | `string` |  |
| `comments_url` | `string` |  |
| `url` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_commits` | `SELECT` | `owner, pull_number, repo` |
