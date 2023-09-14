---
title: docker_migration_packages
hide_title: false
hide_table_of_contents: false
keywords:
  - docker_migration_packages
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
<tr><td><b>Name</b></td><td><code>docker_migration_packages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.packages.docker_migration_packages</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | Unique identifier of the package. |
| `name` | `string` | The name of the package. |
| `url` | `string` |  |
| `repository` | `object` | Minimal Repository |
| `owner` | `object` | A GitHub user. |
| `package_type` | `string` |  |
| `visibility` | `string` |  |
| `html_url` | `string` |  |
| `updated_at` | `string` |  |
| `version_count` | `integer` | The number of versions of the package. |
| `created_at` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_docker_migration_conflicting_packages_for_authenticated_user` | `SELECT` |  | Lists all packages that are owned by the authenticated user within the user's namespace, and that encountered a conflict during a Docker migration.<br />To use this endpoint, you must authenticate using an access token with the `read:packages` scope. |
| `list_docker_migration_conflicting_packages_for_organization` | `SELECT` | `org` | Lists all packages that are in a specific organization, are readable by the requesting user, and that encountered a conflict during a Docker migration.<br />To use this endpoint, you must authenticate using an access token with the `read:packages` scope. |
| `list_docker_migration_conflicting_packages_for_user` | `SELECT` | `username` | Lists all packages that are in a specific user's namespace, that the requesting user has access to, and that encountered a conflict during Docker migration.<br />To use this endpoint, you must authenticate using an access token with the `read:packages` scope. |
