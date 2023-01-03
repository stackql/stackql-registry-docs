---
title: commits
hide_title: false
hide_table_of_contents: false
keywords:
  - stackql
  - github
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GitHub resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
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
| `text_matches` | `array` |  |
| `comments_url` | `string` |  |
| `parents` | `array` |  |
| `score` | `number` |  |
| `html_url` | `string` |  |
| `node_id` | `string` |  |
| `url` | `string` |  |
| `commit` | `object` |  |
| `repository` | `object` | Minimal Repository |
| `sha` | `string` |  |
| `author` | `object` | Simple User |
| `committer` | `object` | Metaproperties for Git author/committer information. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `commits` | `SELECT` | `q` |
