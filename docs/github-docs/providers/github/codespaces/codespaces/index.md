---
title: codespaces
hide_title: false
hide_table_of_contents: false
keywords:
  - codespaces
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>codespaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.codespaces.codespaces" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="codespaces" /> | `array` |
| <CopyableCode code="total_count" /> | `integer` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_for_authenticated_user" /> | `SELECT` | <CopyableCode code="codespace_name" /> | Gets information about a user's codespace.<br /><br />You must authenticate using an access token with the `codespace` scope to use this endpoint.<br /><br />GitHub Apps must have read access to the `codespaces` repository permission to use this endpoint. |
| <CopyableCode code="list_for_authenticated_user" /> | `SELECT` |  | Lists the authenticated user's codespaces.<br /><br />You must authenticate using an access token with the `codespace` scope to use this endpoint.<br /><br />GitHub Apps must have read access to the `codespaces` repository permission to use this endpoint. |
| <CopyableCode code="list_in_repository_for_authenticated_user" /> | `SELECT` | <CopyableCode code="owner, repo" /> | Lists the codespaces associated to a specified repository and the authenticated user.<br /><br />You must authenticate using an access token with the `codespace` scope to use this endpoint.<br /><br />GitHub Apps must have read access to the `codespaces` repository permission to use this endpoint. |
| <CopyableCode code="create_for_authenticated_user" /> | `INSERT` |  | Creates a new codespace, owned by the authenticated user.<br /><br />This endpoint requires either a `repository_id` OR a `pull_request` but not both.<br /><br />You must authenticate using an access token with the `codespace` scope to use this endpoint.<br /><br />GitHub Apps must have write access to the `codespaces` repository permission to use this endpoint. |
| <CopyableCode code="delete_for_authenticated_user" /> | `DELETE` | <CopyableCode code="codespace_name" /> | Deletes a user's codespace.<br /><br />You must authenticate using an access token with the `codespace` scope to use this endpoint.<br /><br />GitHub Apps must have write access to the `codespaces` repository permission to use this endpoint. |
| <CopyableCode code="create_with_pr_for_authenticated_user" /> | `EXEC` | <CopyableCode code="owner, pull_number, repo" /> | Creates a codespace owned by the authenticated user for the specified pull request.<br /><br />You must authenticate using an access token with the `codespace` scope to use this endpoint.<br /><br />GitHub Apps must have write access to the `codespaces` repository permission to use this endpoint. |
| <CopyableCode code="create_with_repo_for_authenticated_user" /> | `EXEC` | <CopyableCode code="owner, repo" /> | Creates a codespace owned by the authenticated user in the specified repository.<br /><br />You must authenticate using an access token with the `codespace` scope to use this endpoint.<br /><br />GitHub Apps must have write access to the `codespaces` repository permission to use this endpoint. |
| <CopyableCode code="export_for_authenticated_user" /> | `EXEC` | <CopyableCode code="codespace_name" /> | Triggers an export of the specified codespace and returns a URL and ID where the status of the export can be monitored.<br /><br />If changes cannot be pushed to the codespace's repository, they will be pushed to a new or previously-existing fork instead.<br /><br />You must authenticate using a personal access token with the `codespace` scope to use this endpoint.<br /><br />GitHub Apps must have write access to the `codespaces_lifecycle_admin` repository permission to use this endpoint. |
| <CopyableCode code="list_devcontainers_in_repository_for_authenticated_user" /> | `EXEC` | <CopyableCode code="owner, repo" /> | Lists the devcontainer.json files associated with a specified repository and the authenticated user. These files<br />specify launchpoint configurations for codespaces created within the repository.<br /><br />You must authenticate using an access token with the `codespace` scope to use this endpoint.<br /><br />GitHub Apps must have read access to the `codespaces_metadata` repository permission to use this endpoint. |
| <CopyableCode code="pre_flight_with_repo_for_authenticated_user" /> | `EXEC` | <CopyableCode code="owner, repo" /> | Gets the default attributes for codespaces created by the user with the repository.<br /><br />You must authenticate using an access token with the `codespace` scope to use this endpoint.<br /><br />GitHub Apps must have write access to the `codespaces` repository permission to use this endpoint. |
| <CopyableCode code="publish_for_authenticated_user" /> | `EXEC` | <CopyableCode code="codespace_name" /> | Publishes an unpublished codespace, creating a new repository and assigning it to the codespace.<br /><br />The codespace's token is granted write permissions to the repository, allowing the user to push their changes.<br /><br />This will fail for a codespace that is already published, meaning it has an associated repository.<br /><br />You must authenticate using a personal access token with the `codespace` scope to use this endpoint.<br /><br />GitHub Apps must have write access to the `codespaces` repository permission to use this endpoint. |
| <CopyableCode code="start_for_authenticated_user" /> | `EXEC` | <CopyableCode code="codespace_name" /> | Starts a user's codespace.<br /><br />You must authenticate using an access token with the `codespace` scope to use this endpoint.<br /><br />GitHub Apps must have write access to the `codespaces_lifecycle_admin` repository permission to use this endpoint. |
| <CopyableCode code="stop_for_authenticated_user" /> | `EXEC` | <CopyableCode code="codespace_name" /> | Stops a user's codespace.<br /><br />You must authenticate using an access token with the `codespace` scope to use this endpoint.<br /><br />GitHub Apps must have write access to the `codespaces_lifecycle_admin` repository permission to use this endpoint. |
| <CopyableCode code="update_for_authenticated_user" /> | `EXEC` | <CopyableCode code="codespace_name" /> | Updates a codespace owned by the authenticated user. Currently only the codespace's machine type and recent folders can be modified using this endpoint.<br /><br />If you specify a new machine type it will be applied the next time your codespace is started.<br /><br />You must authenticate using an access token with the `codespace` scope to use this endpoint.<br /><br />GitHub Apps must have write access to the `codespaces` repository permission to use this endpoint. |
