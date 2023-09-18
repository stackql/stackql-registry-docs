---
title: commits
hide_title: false
hide_table_of_contents: false
keywords:
  - commits
  - search
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
<tr><td><b>Id</b></td><td><code>github.search.commits</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `url` | `string` |  |
| `sha` | `string` |  |
| `comments_url` | `string` |  |
| `score` | `number` |  |
| `parents` | `array` |  |
| `repository` | `object` | Minimal Repository |
| `html_url` | `string` |  |
| `committer` | `object` | Metaproperties for Git author/committer information. |
| `text_matches` | `array` |  |
| `node_id` | `string` |  |
| `commit` | `object` |  |
| `author` | `object` | A GitHub user. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `commits` | `SELECT` | `q` |
