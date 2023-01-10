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
| `path` | `string` |
| `start_line` | `integer` |
| `title` | `string` |
| `end_column` | `integer` |
| `blob_href` | `string` |
| `annotation_level` | `string` |
| `end_line` | `integer` |
| `raw_details` | `string` |
| `message` | `string` |
| `start_column` | `integer` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_annotations` | `SELECT` | `check_run_id, owner, repo` |
