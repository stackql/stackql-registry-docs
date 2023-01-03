---
title: package_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - stackql
  - github
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GitHub resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>package_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.packages.package_versions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | Unique identifier of the package version. |
| `name` | `string` | The name of the package version. |
| `description` | `string` |  |
| `created_at` | `string` |  |
| `metadata` | `object` |  |
| `updated_at` | `string` |  |
| `license` | `string` |  |
| `package_html_url` | `string` |  |
| `deleted_at` | `string` |  |
| `url` | `string` |  |
| `html_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_all_package_versions_for_package_owned_by_authenticated_user` | `SELECT` | `package_name, package_type` | Returns all package versions for a package owned by the authenticated user.<br /><br />To use this endpoint, you must authenticate using an access token with the `packages:read` scope.<br />If `package_type` is not `container`, your token must also include the `repo` scope. |
| `get_all_package_versions_for_package_owned_by_org` | `SELECT` | `org, package_name, package_type` | Returns all package versions for a package owned by an organization.<br /><br />To use this endpoint, you must authenticate using an access token with the `packages:read` scope.<br />If `package_type` is not `container`, your token must also include the `repo` scope. |
| `get_all_package_versions_for_package_owned_by_user` | `SELECT` | `package_name, package_type, username` | Returns all package versions for a public package owned by a specified user.<br /><br />To use this endpoint, you must authenticate using an access token with the `packages:read` scope.<br />If `package_type` is not `container`, your token must also include the `repo` scope. |
| `get_package_version_for_authenticated_user` | `SELECT` | `package_name, package_type, package_version_id` | Gets a specific package version for a package owned by the authenticated user.<br /><br />To use this endpoint, you must authenticate using an access token with the `packages:read` scope.<br />If `package_type` is not `container`, your token must also include the `repo` scope. |
| `get_package_version_for_organization` | `SELECT` | `org, package_name, package_type, package_version_id` | Gets a specific package version in an organization.<br /><br />You must authenticate using an access token with the `packages:read` scope.<br />If `package_type` is not `container`, your token must also include the `repo` scope. |
| `get_package_version_for_user` | `SELECT` | `package_name, package_type, package_version_id, username` | Gets a specific package version for a public package owned by a specified user.<br /><br />At this time, to use this endpoint, you must authenticate using an access token with the `packages:read` scope.<br />If `package_type` is not `container`, your token must also include the `repo` scope. |
| `delete_package_version_for_authenticated_user` | `DELETE` | `package_name, package_type, package_version_id` | Deletes a specific package version for a package owned by the authenticated user.  If the package is public and the package version has more than 5,000 downloads, you cannot delete the package version. In this scenario, contact GitHub support for further assistance.<br /><br />To use this endpoint, you must have admin permissions in the organization and authenticate using an access token with the `packages:read` and `packages:delete` scopes.<br />If `package_type` is not `container`, your token must also include the `repo` scope. |
| `delete_package_version_for_org` | `DELETE` | `org, package_name, package_type, package_version_id` | Deletes a specific package version in an organization. If the package is public and the package version has more than 5,000 downloads, you cannot delete the package version. In this scenario, contact GitHub support for further assistance.<br /><br />To use this endpoint, you must have admin permissions in the organization and authenticate using an access token with the `packages:read` and `packages:delete` scopes. In addition:<br />- If `package_type` is not `container`, your token must also include the `repo` scope.<br />- If `package_type` is `container`, you must also have admin permissions to the container you want to delete. |
| `delete_package_version_for_user` | `DELETE` | `package_name, package_type, package_version_id, username` | Deletes a specific package version for a user. If the package is public and the package version has more than 5,000 downloads, you cannot delete the package version. In this scenario, contact GitHub support for further assistance.<br /><br />To use this endpoint, you must authenticate using an access token with the `packages:read` and `packages:delete` scopes. In addition:<br />- If `package_type` is not `container`, your token must also include the `repo` scope.<br />- If `package_type` is `container`, you must also have admin permissions to the container you want to delete. |
| `restore_package_version_for_authenticated_user` | `EXEC` | `package_name, package_type, package_version_id` | Restores a package version owned by the authenticated user.<br /><br />You can restore a deleted package version under the following conditions:<br />  - The package was deleted within the last 30 days.<br />  - The same package namespace and version is still available and not reused for a new package. If the same package namespace is not available, you will not be able to restore your package. In this scenario, to restore the deleted package, you must delete the new package that uses the deleted package's namespace first.<br /><br />To use this endpoint, you must authenticate using an access token with the `packages:read` and `packages:write` scopes. If `package_type` is not `container`, your token must also include the `repo` scope. |
| `restore_package_version_for_org` | `EXEC` | `org, package_name, package_type, package_version_id` | Restores a specific package version in an organization.<br /><br />You can restore a deleted package under the following conditions:<br />  - The package was deleted within the last 30 days.<br />  - The same package namespace and version is still available and not reused for a new package. If the same package namespace is not available, you will not be able to restore your package. In this scenario, to restore the deleted package, you must delete the new package that uses the deleted package's namespace first.<br /><br />To use this endpoint, you must have admin permissions in the organization and authenticate using an access token with the `packages:read` and `packages:write` scopes. In addition:<br />- If `package_type` is not `container`, your token must also include the `repo` scope.<br />- If `package_type` is `container`, you must also have admin permissions to the container that you want to restore. |
| `restore_package_version_for_user` | `EXEC` | `package_name, package_type, package_version_id, username` | Restores a specific package version for a user.<br /><br />You can restore a deleted package under the following conditions:<br />  - The package was deleted within the last 30 days.<br />  - The same package namespace and version is still available and not reused for a new package. If the same package namespace is not available, you will not be able to restore your package. In this scenario, to restore the deleted package, you must delete the new package that uses the deleted package's namespace first.<br /><br />To use this endpoint, you must authenticate using an access token with the `packages:read` and `packages:write` scopes. In addition:<br />- If `package_type` is not `container`, your token must also include the `repo` scope.<br />- If `package_type` is `container`, you must also have admin permissions to the container that you want to restore. |
