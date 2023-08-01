---
title: workflow_run_usage
hide_title: false
hide_table_of_contents: false
keywords:
  - workflow_run_usage
  - actions
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
<tr><td><b>Name</b></td><td><code>workflow_run_usage</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.actions.workflow_run_usage</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `run_duration_ms` | `integer` |
| `billable` | `object` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_workflow_run_usage` | `SELECT` | `owner, repo, run_id` |
