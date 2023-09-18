---
title: user_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - user_versions
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
<tr><td><b>Name</b></td><td><code>user_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.packages.user_versions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | Unique identifier of the package version. |
| `name` | `string` | The name of the package version. |
| `description` | `string` |  |
| `license` | `string` |  |
| `updated_at` | `string` |  |
| `created_at` | `string` |  |
| `url` | `string` |  |
| `deleted_at` | `string` |  |
| `html_url` | `string` |  |
| `package_html_url` | `string` |  |
| `metadata` | `object` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_all_package_versions_for_package_owned_by_user` | `SELECT` | `package_name, package_type, username` | Lists package versions for a public package owned by a specified user.<br /><br />To use this endpoint, you must authenticate using an access token with the `read:packages` scope. If the `package_type` belongs to a GitHub Packages registry that only supports repository-scoped permissions, your token must also include the `repo` scope. For the list of GitHub Packages registries that only support repository-scoped permissions, see "[About permissions for GitHub Packages](https://docs.github.com/packages/learn-github-packages/about-permissions-for-github-packages#permissions-for-repository-scoped-packages)." |
| `get_package_version_for_user` | `SELECT` | `package_name, package_type, package_version_id, username` | Gets a specific package version for a public package owned by a specified user.<br /><br />At this time, to use this endpoint, you must authenticate using an access token with the `read:packages` scope. If the `package_type` belongs to a GitHub Packages registry that only supports repository-scoped permissions, your token must also include the `repo` scope. For the list of GitHub Packages registries that only support repository-scoped permissions, see "[About permissions for GitHub Packages](https://docs.github.com/packages/learn-github-packages/about-permissions-for-github-packages#permissions-for-repository-scoped-packages)." |
| `delete_package_version_for_user` | `DELETE` | `package_name, package_type, package_version_id, username` | Deletes a specific package version for a user. If the package is public and the package version has more than 5,000 downloads, you cannot delete the package version. In this scenario, contact GitHub support for further assistance.<br /><br />To use this endpoint, you must authenticate using an access token with the `read:packages` and `delete:packages` scopes. In addition:<br />- If the `package_type` belongs to a GitHub Packages registry that only supports repository-scoped permissions, your token must also include the `repo` scope. For the list of these registries, see "[About permissions for GitHub Packages](https://docs.github.com/packages/learn-github-packages/about-permissions-for-github-packages#permissions-for-repository-scoped-packages)."<br />- If the `package_type` belongs to a GitHub Packages registry that supports granular permissions, you must have admin permissions to the package whose version you want to delete. For the list of these registries, see "[About permissions for GitHub Packages](https://docs.github.com/packages/learn-github-packages/about-permissions-for-github-packages#granular-permissions-for-userorganization-scoped-packages)." |
| `restore_package_version_for_user` | `EXEC` | `package_name, package_type, package_version_id, username` | Restores a specific package version for a user.<br /><br />You can restore a deleted package under the following conditions:<br />  - The package was deleted within the last 30 days.<br />  - The same package namespace and version is still available and not reused for a new package. If the same package namespace is not available, you will not be able to restore your package. In this scenario, to restore the deleted package, you must delete the new package that uses the deleted package's namespace first.<br /><br />To use this endpoint, you must authenticate using an access token with the `read:packages` and `write:packages` scopes. In addition:<br />- If the `package_type` belongs to a GitHub Packages registry that only supports repository-scoped permissions, your token must also include the `repo` scope. For the list of these registries, see "[About permissions for GitHub Packages](https://docs.github.com/packages/learn-github-packages/about-permissions-for-github-packages#permissions-for-repository-scoped-packages)."<br />- If the `package_type` belongs to a GitHub Packages registry that supports granular permissions, you must have admin permissions to the package whose version you want to restore. For the list of these registries, see "[About permissions for GitHub Packages](https://docs.github.com/packages/learn-github-packages/about-permissions-for-github-packages#granular-permissions-for-userorganization-scoped-packages)." |
