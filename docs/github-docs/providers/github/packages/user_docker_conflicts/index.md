---
title: user_docker_conflicts
hide_title: false
hide_table_of_contents: false
keywords:
  - user_docker_conflicts
  - packages
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
<tr><td><b>Name</b></td><td><code>user_docker_conflicts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.packages.user_docker_conflicts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | Unique identifier of the package. |
| `name` | `string` | The name of the package. |
| `created_at` | `string` |  |
| `visibility` | `string` |  |
| `updated_at` | `string` |  |
| `url` | `string` |  |
| `version_count` | `integer` | The number of versions of the package. |
| `repository` | `object` | Minimal Repository |
| `owner` | `object` | A GitHub user. |
| `package_type` | `string` |  |
| `html_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_docker_migration_conflicting_packages_for_authenticated_user` | `SELECT` |  |
