---
title: annotations
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
<tr><td><b>Name</b></td><td><code>annotations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.checks.annotations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `start_column` | `integer` |
| `start_line` | `integer` |
| `end_column` | `integer` |
| `message` | `string` |
| `raw_details` | `string` |
| `annotation_level` | `string` |
| `end_line` | `integer` |
| `path` | `string` |
| `title` | `string` |
| `blob_href` | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_annotations` | `SELECT` | `check_run_id, owner, repo` |
