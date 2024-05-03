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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>docker_migration_packages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.packages.docker_migration_packages" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `integer` | Unique identifier of the package. |
| <CopyableCode code="name" /> | `string` | The name of the package. |
| <CopyableCode code="created_at" /> | `string` |  |
| <CopyableCode code="html_url" /> | `string` |  |
| <CopyableCode code="owner" /> | `object` | A GitHub user. |
| <CopyableCode code="package_type" /> | `string` |  |
| <CopyableCode code="repository" /> | `object` | Minimal Repository |
| <CopyableCode code="updated_at" /> | `string` |  |
| <CopyableCode code="url" /> | `string` |  |
| <CopyableCode code="version_count" /> | `integer` | The number of versions of the package. |
| <CopyableCode code="visibility" /> | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_docker_migration_conflicting_packages_for_authenticated_user" /> | `SELECT` |  | Lists all packages that are owned by the authenticated user within the user's namespace, and that encountered a conflict during a Docker migration.<br />To use this endpoint, you must authenticate using an access token with the `read:packages` scope. |
| <CopyableCode code="list_docker_migration_conflicting_packages_for_organization" /> | `SELECT` | <CopyableCode code="org" /> | Lists all packages that are in a specific organization, are readable by the requesting user, and that encountered a conflict during a Docker migration.<br />To use this endpoint, you must authenticate using an access token with the `read:packages` scope. |
| <CopyableCode code="list_docker_migration_conflicting_packages_for_user" /> | `SELECT` | <CopyableCode code="username" /> | Lists all packages that are in a specific user's namespace, that the requesting user has access to, and that encountered a conflict during Docker migration.<br />To use this endpoint, you must authenticate using an access token with the `read:packages` scope. |
