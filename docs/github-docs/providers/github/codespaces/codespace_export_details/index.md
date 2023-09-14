---
title: codespace_export_details
hide_title: false
hide_table_of_contents: false
keywords:
  - codespace_export_details
  - codespaces
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
<tr><td><b>Name</b></td><td><code>codespace_export_details</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.codespaces.codespace_export_details</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Id for the export details |
| `sha` | `string` | Git commit SHA of the exported branch |
| `state` | `string` | State of the latest export |
| `branch` | `string` | Name of the exported branch |
| `completed_at` | `string` | Completion time of the last export operation |
| `export_url` | `string` | Url for fetching export details |
| `html_url` | `string` | Web url for the exported branch |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_export_details_for_authenticated_user` | `SELECT` | `codespace_name, export_id` |
