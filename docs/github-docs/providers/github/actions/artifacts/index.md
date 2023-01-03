---
title: artifacts
hide_title: false
hide_table_of_contents: false
keywords:
  - stackql
  - github
  - actions
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GitHub resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>artifacts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.actions.artifacts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `name` | `string` | The name of the artifact. |
| `node_id` | `string` |  |
| `archive_download_url` | `string` |  |
| `created_at` | `string` |  |
| `size_in_bytes` | `integer` | The size in bytes of the artifact. |
| `expired` | `boolean` | Whether or not the artifact has expired. |
| `url` | `string` |  |
| `expires_at` | `string` |  |
| `updated_at` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_artifact` | `SELECT` | `artifact_id, owner, repo` | Gets a specific artifact for a workflow run. Anyone with read access to the repository can use this endpoint. If the repository is private you must use an access token with the `repo` scope. GitHub Apps must have the `actions:read` permission to use this endpoint. |
| `list_artifacts_for_repo` | `SELECT` | `owner, repo` | Lists all artifacts for a repository. Anyone with read access to the repository can use this endpoint. If the repository is private you must use an access token with the `repo` scope. GitHub Apps must have the `actions:read` permission to use this endpoint. |
| `list_workflow_run_artifacts` | `SELECT` | `owner, repo, run_id` | Lists artifacts for a workflow run. Anyone with read access to the repository can use this endpoint. If the repository is private you must use an access token with the `repo` scope. GitHub Apps must have the `actions:read` permission to use this endpoint. |
| `delete_artifact` | `DELETE` | `artifact_id, owner, repo` | Deletes an artifact for a workflow run. You must authenticate using an access token with the `repo` scope to use this endpoint. GitHub Apps must have the `actions:write` permission to use this endpoint. |
| `download_artifact` | `EXEC` | `archive_format, artifact_id, owner, repo` | Gets a redirect URL to download an archive for a repository. This URL expires after 1 minute. Look for `Location:` in<br />the response header to find the URL for the download. The `:archive_format` must be `zip`. Anyone with read access to<br />the repository can use this endpoint. If the repository is private you must use an access token with the `repo` scope.<br />GitHub Apps must have the `actions:read` permission to use this endpoint. |
