---
title: repos_milestones_labels
hide_title: false
hide_table_of_contents: false
keywords:
  - repos_milestones_labels
  - issues
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
<tr><td><b>Name</b></td><td><code>repos_milestones_labels</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.issues.repos_milestones_labels</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `name` | `string` | The name of the label. |
| `description` | `string` |  |
| `node_id` | `string` |  |
| `url` | `string` | URL for the label |
| `color` | `string` | 6-character hex code, without the leading #, identifying the color |
| `default` | `boolean` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_labels_for_milestone` | `SELECT` | `milestone_number, owner, repo` |
