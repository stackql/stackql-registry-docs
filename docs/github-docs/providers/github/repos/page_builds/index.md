---
title: page_builds
hide_title: false
hide_table_of_contents: false
keywords:
  - page_builds
  - repos
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
<tr><td><b>Name</b></td><td><code>page_builds</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.repos.page_builds" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="commit" /> | `string` |  |
| <CopyableCode code="created_at" /> | `string` |  |
| <CopyableCode code="duration" /> | `integer` |  |
| <CopyableCode code="error" /> | `object` |  |
| <CopyableCode code="pusher" /> | `object` | A GitHub user. |
| <CopyableCode code="status" /> | `string` |  |
| <CopyableCode code="updated_at" /> | `string` |  |
| <CopyableCode code="url" /> | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_pages_build" /> | `SELECT` | <CopyableCode code="build_id, owner, repo" /> | Gets information about a GitHub Pages build.<br /><br />A token with the `repo` scope is required. GitHub Apps must have the `pages:read` permission. |
| <CopyableCode code="list_pages_builds" /> | `SELECT` | <CopyableCode code="owner, repo" /> | Lists builts of a GitHub Pages site.<br /><br />A token with the `repo` scope is required. GitHub Apps must have the `pages:read` permission. |
| <CopyableCode code="create_pages_deployment" /> | `EXEC` | <CopyableCode code="owner, repo, data__artifact_url, data__oidc_token, data__pages_build_version" /> | Create a GitHub Pages deployment for a repository.<br /><br />Users must have write permissions. GitHub Apps must have the `pages:write` permission to use this endpoint. |
| <CopyableCode code="request_pages_build" /> | `EXEC` | <CopyableCode code="owner, repo" /> | You can request that your site be built from the latest revision on the default branch. This has the same effect as pushing a commit to your default branch, but does not require an additional commit. Manually triggering page builds can be helpful when diagnosing build warnings and failures.<br /><br />Build requests are limited to one concurrent build per repository and one concurrent build per requester. If you request a build while another is still in progress, the second request will be queued until the first completes. |
