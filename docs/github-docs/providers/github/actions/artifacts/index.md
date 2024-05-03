---
title: artifacts
hide_title: false
hide_table_of_contents: false
keywords:
  - artifacts
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
<tr><td><b>Name</b></td><td><code>artifacts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.actions.artifacts" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `integer` |  |
| <CopyableCode code="name" /> | `string` | The name of the artifact. |
| <CopyableCode code="archive_download_url" /> | `string` |  |
| <CopyableCode code="created_at" /> | `string` |  |
| <CopyableCode code="expired" /> | `boolean` | Whether or not the artifact has expired. |
| <CopyableCode code="expires_at" /> | `string` |  |
| <CopyableCode code="node_id" /> | `string` |  |
| <CopyableCode code="size_in_bytes" /> | `integer` | The size in bytes of the artifact. |
| <CopyableCode code="updated_at" /> | `string` |  |
| <CopyableCode code="url" /> | `string` |  |
| <CopyableCode code="workflow_run" /> | `object` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_artifact" /> | `SELECT` | <CopyableCode code="artifact_id, owner, repo" /> | Gets a specific artifact for a workflow run. Anyone with read access to the repository can use this endpoint. If the repository is private you must use an access token with the `repo` scope. GitHub Apps must have the `actions:read` permission to use this endpoint. |
| <CopyableCode code="list_artifacts_for_repo" /> | `SELECT` | <CopyableCode code="owner, repo" /> | Lists all artifacts for a repository. Anyone with read access to the repository can use this endpoint. If the repository is private you must use an access token with the `repo` scope. GitHub Apps must have the `actions:read` permission to use this endpoint. |
| <CopyableCode code="list_workflow_run_artifacts" /> | `SELECT` | <CopyableCode code="owner, repo, run_id" /> | Lists artifacts for a workflow run. Anyone with read access to the repository can use this endpoint. If the repository is private you must use an access token with the `repo` scope. GitHub Apps must have the `actions:read` permission to use this endpoint. |
| <CopyableCode code="delete_artifact" /> | `DELETE` | <CopyableCode code="artifact_id, owner, repo" /> | Deletes an artifact for a workflow run. You must authenticate using an access token with the `repo` scope to use this endpoint. GitHub Apps must have the `actions:write` permission to use this endpoint. |
| <CopyableCode code="download_artifact" /> | `EXEC` | <CopyableCode code="archive_format, artifact_id, owner, repo" /> | Gets a redirect URL to download an archive for a repository. This URL expires after 1 minute. Look for `Location:` in<br />the response header to find the URL for the download. The `:archive_format` must be `zip`.<br /><br />You must authenticate using an access token with the `repo` scope to use this endpoint.<br />GitHub Apps must have the `actions:read` permission to use this endpoint. |
