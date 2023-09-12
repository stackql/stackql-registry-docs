---
title: repos_runs_attempts_jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - repos_runs_attempts_jobs
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
<tr><td><b>Name</b></td><td><code>repos_runs_attempts_jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.actions.repos_runs_attempts_jobs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `jobs` | `array` |
| `total_count` | `integer` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_jobs_for_workflow_run_attempt` | `SELECT` | `attempt_number, owner, repo, run_id` |
