---
title: packages
hide_title: false
hide_table_of_contents: false
keywords:
  - packages
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
<tr><td><b>Name</b></td><td><code>packages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.packages.packages</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | Unique identifier of the package. |
| `name` | `string` | The name of the package. |
| `owner` | `object` | Simple User |
| `package_type` | `string` |  |
| `version_count` | `integer` | The number of versions of the package. |
| `visibility` | `string` |  |
| `repository` | `object` | Minimal Repository |
| `created_at` | `string` |  |
| `html_url` | `string` |  |
| `updated_at` | `string` |  |
| `url` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_package_for_authenticated_user` | `SELECT` | `package_name, package_type` | Gets a specific package for a package owned by the authenticated user.<br /><br />To use this endpoint, you must authenticate using an access token with the `packages:read` scope.<br />If `package_type` is not `container`, your token must also include the `repo` scope. |
| `get_package_for_organization` | `SELECT` | `org, package_name, package_type` | Gets a specific package in an organization.<br /><br />To use this endpoint, you must authenticate using an access token with the `packages:read` scope.<br />If `package_type` is not `container`, your token must also include the `repo` scope. |
| `get_package_for_user` | `SELECT` | `package_name, package_type, username` | Gets a specific package metadata for a public package owned by a user.<br /><br />To use this endpoint, you must authenticate using an access token with the `packages:read` scope.<br />If `package_type` is not `container`, your token must also include the `repo` scope. |
| `list_packages_for_authenticated_user` | `SELECT` | `package_type` | Lists packages owned by the authenticated user within the user's namespace.<br /><br />To use this endpoint, you must authenticate using an access token with the `packages:read` scope.<br />If `package_type` is not `container`, your token must also include the `repo` scope. |
| `list_packages_for_organization` | `SELECT` | `org, package_type` | Lists all packages in an organization readable by the user.<br /><br />To use this endpoint, you must authenticate using an access token with the `packages:read` scope.<br />If `package_type` is not `container`, your token must also include the `repo` scope. |
| `list_packages_for_user` | `SELECT` | `package_type, username` | Lists all packages in a user's namespace for which the requesting user has access.<br /><br />To use this endpoint, you must authenticate using an access token with the `packages:read` scope.<br />If `package_type` is not `container`, your token must also include the `repo` scope. |
| `delete_package_for_authenticated_user` | `DELETE` | `package_name, package_type` | Deletes a package owned by the authenticated user. You cannot delete a public package if any version of the package has more than 5,000 downloads. In this scenario, contact GitHub support for further assistance.<br /><br />To use this endpoint, you must authenticate using an access token with the `packages:read` and `packages:delete` scopes.<br />If `package_type` is not `container`, your token must also include the `repo` scope. |
| `delete_package_for_org` | `DELETE` | `org, package_name, package_type` | Deletes an entire package in an organization. You cannot delete a public package if any version of the package has more than 5,000 downloads. In this scenario, contact GitHub support for further assistance.<br /><br />To use this endpoint, you must have admin permissions in the organization and authenticate using an access token with the `packages:read` and `packages:delete` scopes. In addition:<br />- If `package_type` is not `container`, your token must also include the `repo` scope.<br />- If `package_type` is `container`, you must also have admin permissions to the container you want to delete. |
| `delete_package_for_user` | `DELETE` | `package_name, package_type, username` | Deletes an entire package for a user. You cannot delete a public package if any version of the package has more than 5,000 downloads. In this scenario, contact GitHub support for further assistance.<br /><br />To use this endpoint, you must authenticate using an access token with the `packages:read` and `packages:delete` scopes. In addition:<br />- If `package_type` is not `container`, your token must also include the `repo` scope.<br />- If `package_type` is `container`, you must also have admin permissions to the container you want to delete. |
| `restore_package_for_authenticated_user` | `EXEC` | `package_name, package_type` | Restores a package owned by the authenticated user.<br /><br />You can restore a deleted package under the following conditions:<br />  - The package was deleted within the last 30 days.<br />  - The same package namespace and version is still available and not reused for a new package. If the same package namespace is not available, you will not be able to restore your package. In this scenario, to restore the deleted package, you must delete the new package that uses the deleted package's namespace first.<br /><br />To use this endpoint, you must authenticate using an access token with the `packages:read` and `packages:write` scopes. If `package_type` is not `container`, your token must also include the `repo` scope. |
| `restore_package_for_org` | `EXEC` | `org, package_name, package_type` | Restores an entire package in an organization.<br /><br />You can restore a deleted package under the following conditions:<br />  - The package was deleted within the last 30 days.<br />  - The same package namespace and version is still available and not reused for a new package. If the same package namespace is not available, you will not be able to restore your package. In this scenario, to restore the deleted package, you must delete the new package that uses the deleted package's namespace first.<br /><br />To use this endpoint, you must have admin permissions in the organization and authenticate using an access token with the `packages:read` and `packages:write` scopes. In addition:<br />- If `package_type` is not `container`, your token must also include the `repo` scope.<br />- If `package_type` is `container`, you must also have admin permissions to the container that you want to restore. |
| `restore_package_for_user` | `EXEC` | `package_name, package_type, username` | Restores an entire package for a user.<br /><br />You can restore a deleted package under the following conditions:<br />  - The package was deleted within the last 30 days.<br />  - The same package namespace and version is still available and not reused for a new package. If the same package namespace is not available, you will not be able to restore your package. In this scenario, to restore the deleted package, you must delete the new package that uses the deleted package's namespace first.<br /><br />To use this endpoint, you must authenticate using an access token with the `packages:read` and `packages:write` scopes. In addition:<br />- If `package_type` is not `container`, your token must also include the `repo` scope.<br />- If `package_type` is `container`, you must also have admin permissions to the container that you want to restore. |
