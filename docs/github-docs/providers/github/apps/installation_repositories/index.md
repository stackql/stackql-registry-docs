---
title: installation_repositories
hide_title: false
hide_table_of_contents: false
keywords:
  - installation_repositories
  - apps
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
<tr><td><b>Name</b></td><td><code>installation_repositories</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.apps.installation_repositories</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `repositories` | `array` |
| `repository_selection` | `string` |
| `total_count` | `integer` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_repos_accessible_to_installation` | `SELECT` |  |
