---
title: runner_labels
hide_title: false
hide_table_of_contents: false
keywords:
  - runner_labels
  - actions
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
<tr><td><b>Name</b></td><td><code>runner_labels</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.actions.runner_labels" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="labels" /> | `array` |
| <CopyableCode code="total_count" /> | `integer` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_labels_for_self_hosted_runner_for_org" /> | `SELECT` | <CopyableCode code="org, runner_id" /> | Lists all labels for a self-hosted runner configured in an organization.<br /><br />You must authenticate using an access token with the `admin:org` scope to use this endpoint.<br />If the repository is private, you must use an access token with the `repo` scope.<br />GitHub Apps must have the `administration` permission for repositories and the `organization_self_hosted_runners` permission for organizations.<br />Authenticated users must have admin access to repositories or organizations, or the `manage_runners:enterprise` scope for enterprises, to use these endpoints. |
| <CopyableCode code="list_labels_for_self_hosted_runner_for_repo" /> | `SELECT` | <CopyableCode code="owner, repo, runner_id" /> | Lists all labels for a self-hosted runner configured in a repository.<br /><br />You must authenticate using an access token with the `repo` scope to use this endpoint.<br />If the repository is private, you must use an access token with the `repo` scope.<br />GitHub Apps must have the `administration` permission for repositories and the `organization_self_hosted_runners` permission for organizations.<br />Authenticated users must have admin access to repositories or organizations, or the `manage_runners:enterprise` scope for enterprises, to use these endpoints. |
| <CopyableCode code="add_custom_labels_to_self_hosted_runner_for_org" /> | `INSERT` | <CopyableCode code="org, runner_id, data__labels" /> | Add custom labels to a self-hosted runner configured in an organization.<br /><br />You must authenticate using an access token with the `admin:org` scope to use this endpoint.<br />If the repository is private, you must use an access token with the `repo` scope.<br />GitHub Apps must have the `administration` permission for repositories and the `organization_self_hosted_runners` permission for organizations.<br />Authenticated users must have admin access to repositories or organizations, or the `manage_runners:enterprise` scope for enterprises, to use these endpoints. |
| <CopyableCode code="add_custom_labels_to_self_hosted_runner_for_repo" /> | `INSERT` | <CopyableCode code="owner, repo, runner_id, data__labels" /> | Add custom labels to a self-hosted runner configured in a repository.<br /><br />You must authenticate using an access token with the `repo` scope to use this endpoint.<br />If the repository is private, you must use an access token with the `repo` scope.<br />GitHub Apps must have the `administration` permission for repositories and the `organization_self_hosted_runners` permission for organizations.<br />Authenticated users must have admin access to repositories or organizations, or the `manage_runners:enterprise` scope for enterprises, to use these endpoints. |
| <CopyableCode code="remove_all_custom_labels_from_self_hosted_runner_for_org" /> | `DELETE` | <CopyableCode code="org, runner_id" /> | Remove all custom labels from a self-hosted runner configured in an<br />organization. Returns the remaining read-only labels from the runner.<br /><br />You must authenticate using an access token with the `admin:org` scope to use this endpoint.<br />If the repository is private, you must use an access token with the `repo` scope.<br />GitHub Apps must have the `administration` permission for repositories and the `organization_self_hosted_runners` permission for organizations.<br />Authenticated users must have admin access to repositories or organizations, or the `manage_runners:enterprise` scope for enterprises, to use these endpoints. |
| <CopyableCode code="remove_all_custom_labels_from_self_hosted_runner_for_repo" /> | `DELETE` | <CopyableCode code="owner, repo, runner_id" /> | Remove all custom labels from a self-hosted runner configured in a<br />repository. Returns the remaining read-only labels from the runner.<br /><br />You must authenticate using an access token with the `repo` scope to use this endpoint.<br />If the repository is private, you must use an access token with the `repo` scope.<br />GitHub Apps must have the `administration` permission for repositories and the `organization_self_hosted_runners` permission for organizations.<br />Authenticated users must have admin access to repositories or organizations, or the `manage_runners:enterprise` scope for enterprises, to use these endpoints. |
| <CopyableCode code="remove_custom_label_from_self_hosted_runner_for_org" /> | `DELETE` | <CopyableCode code="name, org, runner_id" /> | Remove a custom label from a self-hosted runner configured<br />in an organization. Returns the remaining labels from the runner.<br /><br />This endpoint returns a `404 Not Found` status if the custom label is not<br />present on the runner.<br /><br />You must authenticate using an access token with the `admin:org` scope to use this endpoint.<br />If the repository is private, you must use an access token with the `repo` scope.<br />GitHub Apps must have the `administration` permission for repositories and the `organization_self_hosted_runners` permission for organizations.<br />Authenticated users must have admin access to repositories or organizations, or the `manage_runners:enterprise` scope for enterprises, to use these endpoints. |
| <CopyableCode code="remove_custom_label_from_self_hosted_runner_for_repo" /> | `DELETE` | <CopyableCode code="name, owner, repo, runner_id" /> | Remove a custom label from a self-hosted runner configured<br />in a repository. Returns the remaining labels from the runner.<br /><br />This endpoint returns a `404 Not Found` status if the custom label is not<br />present on the runner.<br /><br />You must authenticate using an access token with the `repo` scope to use this endpoint.<br />If the repository is private, you must use an access token with the `repo` scope.<br />GitHub Apps must have the `administration` permission for repositories and the `organization_self_hosted_runners` permission for organizations.<br />Authenticated users must have admin access to repositories or organizations, or the `manage_runners:enterprise` scope for enterprises, to use these endpoints. |
| <CopyableCode code="set_custom_labels_for_self_hosted_runner_for_org" /> | `EXEC` | <CopyableCode code="org, runner_id, data__labels" /> | Remove all previous custom labels and set the new custom labels for a specific<br />self-hosted runner configured in an organization.<br /><br />You must authenticate using an access token with the `admin:org` scope to use this endpoint.<br />If the repository is private, you must use an access token with the `repo` scope.<br />GitHub Apps must have the `administration` permission for repositories and the `organization_self_hosted_runners` permission for organizations.<br />Authenticated users must have admin access to repositories or organizations, or the `manage_runners:enterprise` scope for enterprises, to use these endpoints. |
| <CopyableCode code="set_custom_labels_for_self_hosted_runner_for_repo" /> | `EXEC` | <CopyableCode code="owner, repo, runner_id, data__labels" /> | Remove all previous custom labels and set the new custom labels for a specific<br />self-hosted runner configured in a repository.<br /><br />You must authenticate using an access token with the `repo` scope to use this endpoint.<br />If the repository is private, you must use an access token with the `repo` scope.<br />GitHub Apps must have the `administration` permission for repositories and the `organization_self_hosted_runners` permission for organizations.<br />Authenticated users must have admin access to repositories or organizations, or the `manage_runners:enterprise` scope for enterprises, to use these endpoints. |
