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
| `repository` | `object` | Minimal Repository |
| `score` | `number` |  |
| `html_url` | `string` |  |
| `node_id` | `string` |  |
| `comments_url` | `string` |  |
| `parents` | `array` |  |
| `text_matches` | `array` |  |
| `commit` | `object` |  |
| `committer` | `object` | Metaproperties for Git author/committer information. |
| `url` | `string` |  |
| `sha` | `string` |  |
| `author` | `object` | Simple User |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `commits` | `SELECT` | `q` |
