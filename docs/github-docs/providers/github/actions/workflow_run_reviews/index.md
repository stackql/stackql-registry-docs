---
title: workflow_run_reviews
hide_title: false
hide_table_of_contents: false
keywords:
  - workflow_run_reviews
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
<tr><td><b>Name</b></td><td><code>workflow_run_reviews</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.actions.workflow_run_reviews</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `comment` | `string` | The comment submitted with the deployment review |
| `environments` | `array` | The list of environments that were approved or rejected |
| `state` | `string` | Whether deployment to the environment(s) was approved or rejected or pending (with comments) |
| `user` | `object` | A GitHub user. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_reviews_for_run` | `SELECT` | `owner, repo, run_id` |
