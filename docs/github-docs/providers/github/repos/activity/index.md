---
title: activity
hide_title: false
hide_table_of_contents: false
keywords:
  - activity
  - repos
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
<tr><td><b>Name</b></td><td><code>activity</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.activity</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `activity_type` | `string` | The type of the activity that was performed. |
| `actor` | `object` | A GitHub user. |
| `after` | `string` | The SHA of the commit after the activity. |
| `before` | `string` | The SHA of the commit before the activity. |
| `node_id` | `string` |  |
| `ref` | `string` | The full Git reference, formatted as `refs/heads/&lt;branch name&gt;`. |
| `timestamp` | `string` | The time when the activity occurred. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_activities` | `SELECT` | `owner, repo` |
