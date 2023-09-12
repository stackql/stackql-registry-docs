---
title: repos_devcontainers
hide_title: false
hide_table_of_contents: false
keywords:
  - repos_devcontainers
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
<tr><td><b>Name</b></td><td><code>repos_devcontainers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.codespaces.repos_devcontainers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `devcontainers` | `array` |
| `total_count` | `integer` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_devcontainers_in_repository_for_authenticated_user` | `SELECT` | `owner, repo` |
