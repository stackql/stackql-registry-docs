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
| `language` | `string` |  |
| `html_url` | `string` |  |
| `last_modified_at` | `string` |  |
| `line_numbers` | `array` |  |
| `repository` | `object` | Minimal Repository |
| `url` | `string` |  |
| `git_url` | `string` |  |
| `file_size` | `integer` |  |
| `score` | `number` |  |
| `sha` | `string` |  |
| `text_matches` | `array` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `code` | `SELECT` | `q` |
