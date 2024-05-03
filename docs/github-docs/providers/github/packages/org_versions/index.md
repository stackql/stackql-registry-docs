---
title: org_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - org_versions
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>org_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.packages.org_versions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `integer` | Unique identifier of the package version. |
| <CopyableCode code="name" /> | `string` | The name of the package version. |
| <CopyableCode code="description" /> | `string` |  |
| <CopyableCode code="created_at" /> | `string` |  |
| <CopyableCode code="deleted_at" /> | `string` |  |
| <CopyableCode code="html_url" /> | `string` |  |
| <CopyableCode code="license" /> | `string` |  |
| <CopyableCode code="metadata" /> | `object` |  |
| <CopyableCode code="package_html_url" /> | `string` |  |
| <CopyableCode code="updated_at" /> | `string` |  |
| <CopyableCode code="url" /> | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_all_package_versions_for_package_owned_by_org" /> | `SELECT` | <CopyableCode code="org, package_name, package_type" /> | Lists package versions for a package owned by an organization.<br /><br />If the `package_type` belongs to a GitHub Packages registry that only supports repository-scoped permissions, your token must also include the `repo` scope. For the list of GitHub Packages registries that only support repository-scoped permissions, see "[About permissions for GitHub Packages](https://docs.github.com/packages/learn-github-packages/about-permissions-for-github-packages#permissions-for-repository-scoped-packages)." |
| <CopyableCode code="get_package_version_for_organization" /> | `SELECT` | <CopyableCode code="org, package_name, package_type, package_version_id" /> | Gets a specific package version in an organization.<br /><br />You must authenticate using an access token with the `read:packages` scope. If the `package_type` belongs to a GitHub Packages registry that only supports repository-scoped permissions, your token must also include the `repo` scope. For the list of GitHub Packages registries that only support repository-scoped permissions, see "[About permissions for GitHub Packages](https://docs.github.com/packages/learn-github-packages/about-permissions-for-github-packages#permissions-for-repository-scoped-packages)." |
| <CopyableCode code="delete_package_version_for_org" /> | `DELETE` | <CopyableCode code="org, package_name, package_type, package_version_id" /> | Deletes a specific package version in an organization. If the package is public and the package version has more than 5,000 downloads, you cannot delete the package version. In this scenario, contact GitHub support for further assistance.<br /><br />To use this endpoint, you must have admin permissions in the organization and authenticate using an access token with the `read:packages` and `delete:packages` scopes. In addition:<br />- If the `package_type` belongs to a GitHub Packages registry that only supports repository-scoped permissions, your token must also include the `repo` scope. For the list of these registries, see "[About permissions for GitHub Packages](https://docs.github.com/packages/learn-github-packages/about-permissions-for-github-packages#permissions-for-repository-scoped-packages)."<br />- If the `package_type` belongs to a GitHub Packages registry that supports granular permissions, you must have admin permissions to the package whose version you want to delete. For the list of these registries, see "[About permissions for GitHub Packages](https://docs.github.com/packages/learn-github-packages/about-permissions-for-github-packages#granular-permissions-for-userorganization-scoped-packages)." |
| <CopyableCode code="restore_package_version_for_org" /> | `EXEC` | <CopyableCode code="org, package_name, package_type, package_version_id" /> | Restores a specific package version in an organization.<br /><br />You can restore a deleted package under the following conditions:<br />  - The package was deleted within the last 30 days.<br />  - The same package namespace and version is still available and not reused for a new package. If the same package namespace is not available, you will not be able to restore your package. In this scenario, to restore the deleted package, you must delete the new package that uses the deleted package's namespace first.<br /><br />To use this endpoint, you must have admin permissions in the organization and authenticate using an access token with the `read:packages` and `write:packages` scopes. In addition:<br />- If the `package_type` belongs to a GitHub Packages registry that only supports repository-scoped permissions, your token must also include the `repo` scope. For the list of these registries, see "[About permissions for GitHub Packages](https://docs.github.com/packages/learn-github-packages/about-permissions-for-github-packages#permissions-for-repository-scoped-packages)."<br />- If the `package_type` belongs to a GitHub Packages registry that supports granular permissions, you must have admin permissions to the package whose version you want to restore. For the list of these registries, see "[About permissions for GitHub Packages](https://docs.github.com/packages/learn-github-packages/about-permissions-for-github-packages#granular-permissions-for-userorganization-scoped-packages)." |
