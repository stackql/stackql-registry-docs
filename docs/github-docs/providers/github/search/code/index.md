---
title: code
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
<tr><td><b>Name</b></td><td><code>code</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.search.code</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` |  |
| `git_url` | `string` |  |
| `language` | `string` |  |
| `path` | `string` |  |
| `sha` | `string` |  |
| `file_size` | `integer` |  |
| `url` | `string` |  |
| `line_numbers` | `array` |  |
| `last_modified_at` | `string` |  |
| `repository` | `object` | Minimal Repository |
| `score` | `number` |  |
| `text_matches` | `array` |  |
| `html_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `code` | `SELECT` | `q` |
