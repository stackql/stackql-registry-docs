---
title: code
hide_title: false
hide_table_of_contents: false
keywords:
  - code
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
<tr><td><b>Name</b></td><td><code>code</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.search.code</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` |  |
| `path` | `string` |  |
| `git_url` | `string` |  |
| `line_numbers` | `array` |  |
| `score` | `number` |  |
| `url` | `string` |  |
| `last_modified_at` | `string` |  |
| `file_size` | `integer` |  |
| `html_url` | `string` |  |
| `sha` | `string` |  |
| `repository` | `object` | Minimal Repository |
| `text_matches` | `array` |  |
| `language` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `code` | `SELECT` | `q` |
