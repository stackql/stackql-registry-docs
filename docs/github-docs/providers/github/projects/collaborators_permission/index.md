---
title: collaborators_permission
hide_title: false
hide_table_of_contents: false
keywords:
  - collaborators_permission
  - projects
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
<tr><td><b>Name</b></td><td><code>collaborators_permission</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.projects.collaborators_permission</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `permission` | `string` |  |
| `user` | `object` | A GitHub user. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_permission_for_user` | `SELECT` | `project_id, username` |
