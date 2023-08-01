---
title: annotations
hide_title: false
hide_table_of_contents: false
keywords:
  - annotations
  - checks
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
<tr><td><b>Name</b></td><td><code>annotations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.checks.annotations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `message` | `string` |
| `start_line` | `integer` |
| `title` | `string` |
| `end_line` | `integer` |
| `start_column` | `integer` |
| `path` | `string` |
| `end_column` | `integer` |
| `annotation_level` | `string` |
| `blob_href` | `string` |
| `raw_details` | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_annotations` | `SELECT` | `check_run_id, owner, repo` |
