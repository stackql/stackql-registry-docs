---
title: users
hide_title: false
hide_table_of_contents: false
keywords:
  - users
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
<tr><td><b>Name</b></td><td><code>users</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.packages.users</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | Unique identifier of the package. |
| `name` | `string` | The name of the package. |
| `created_at` | `string` |  |
| `owner` | `object` | A GitHub user. |
| `url` | `string` |  |
| `package_type` | `string` |  |
| `repository` | `object` | Minimal Repository |
| `version_count` | `integer` | The number of versions of the package. |
| `visibility` | `string` |  |
| `updated_at` | `string` |  |
| `html_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_package_for_user` | `SELECT` | `package_name, package_type, username` | Gets a specific package metadata for a public package owned by a user.<br /><br />To use this endpoint, you must authenticate using an access token with the `read:packages` scope. If the `package_type` belongs to a GitHub Packages registry that only supports repository-scoped permissions, your token must also include the `repo` scope. For the list of GitHub Packages registries that only support repository-scoped permissions, see "[About permissions for GitHub Packages](https://docs.github.com/packages/learn-github-packages/about-permissions-for-github-packages#permissions-for-repository-scoped-packages)." |
| `list_packages_for_user` | `SELECT` | `package_type, username` | Lists all packages in a user's namespace for which the requesting user has access.<br /><br />To use this endpoint, you must authenticate using an access token with the `read:packages` scope. If the `package_type` belongs to a GitHub Packages registry that only supports repository-scoped permissions, your token must also include the `repo` scope. For the list of GitHub Packages registries that only support repository-scoped permissions, see "[About permissions for GitHub Packages](https://docs.github.com/packages/learn-github-packages/about-permissions-for-github-packages#permissions-for-repository-scoped-packages)." |
| `delete_package_for_user` | `DELETE` | `package_name, package_type, username` | Deletes an entire package for a user. You cannot delete a public package if any version of the package has more than 5,000 downloads. In this scenario, contact GitHub support for further assistance.<br /><br />To use this endpoint, you must authenticate using an access token with the `read:packages` and `delete:packages` scopes. In addition:<br />- If the `package_type` belongs to a GitHub Packages registry that only supports repository-scoped permissions, your token must also include the `repo` scope. For the list of these registries, see "[About permissions for GitHub Packages](https://docs.github.com/packages/learn-github-packages/about-permissions-for-github-packages#permissions-for-repository-scoped-packages)."<br />- If the `package_type` belongs to a GitHub Packages registry that supports granular permissions, you must have admin permissions to the package you want to delete. For the list of these registries, see "[About permissions for GitHub Packages](https://docs.github.com/packages/learn-github-packages/about-permissions-for-github-packages#granular-permissions-for-userorganization-scoped-packages)." |
| `restore_package_for_user` | `EXEC` | `package_name, package_type, username` | Restores an entire package for a user.<br /><br />You can restore a deleted package under the following conditions:<br />  - The package was deleted within the last 30 days.<br />  - The same package namespace and version is still available and not reused for a new package. If the same package namespace is not available, you will not be able to restore your package. In this scenario, to restore the deleted package, you must delete the new package that uses the deleted package's namespace first.<br /><br />To use this endpoint, you must authenticate using an access token with the `read:packages` and `write:packages` scopes. In addition:<br />- If the `package_type` belongs to a GitHub Packages registry that only supports repository-scoped permissions, your token must also include the `repo` scope. For the list of these registries, see "[About permissions for GitHub Packages](https://docs.github.com/packages/learn-github-packages/about-permissions-for-github-packages#permissions-for-repository-scoped-packages)."<br />- If the `package_type` belongs to a GitHub Packages registry that supports granular permissions, you must have admin permissions to the package you want to restore. For the list of these registries, see "[About permissions for GitHub Packages](https://docs.github.com/packages/learn-github-packages/about-permissions-for-github-packages#granular-permissions-for-userorganization-scoped-packages)." |
