---
title: cache
hide_title: false
hide_table_of_contents: false
keywords:
  - cache
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
<tr><td><b>Name</b></td><td><code>cache</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.actions.cache" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="actions_caches" /> | `array` | Array of caches |
| <CopyableCode code="total_count" /> | `integer` | Total number of caches |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_actions_cache_list" /> | `SELECT` | <CopyableCode code="owner, repo" /> | Lists the GitHub Actions caches for a repository.<br />You must authenticate using an access token with the `repo` scope to use this endpoint.<br />GitHub Apps must have the `actions:read` permission to use this endpoint. |
| <CopyableCode code="delete_actions_cache_by_id" /> | `DELETE` | <CopyableCode code="cache_id, owner, repo" /> | Deletes a GitHub Actions cache for a repository, using a cache ID.<br /><br />You must authenticate using an access token with the `repo` scope to use this endpoint.<br /><br />GitHub Apps must have the `actions:write` permission to use this endpoint. |
| <CopyableCode code="delete_actions_cache_by_key" /> | `DELETE` | <CopyableCode code="key, owner, repo" /> | Deletes one or more GitHub Actions caches for a repository, using a complete cache key. By default, all caches that match the provided key are deleted, but you can optionally provide a Git ref to restrict deletions to caches that match both the provided key and the Git ref.<br /><br />You must authenticate using an access token with the `repo` scope to use this endpoint.<br /><br />GitHub Apps must have the `actions:write` permission to use this endpoint. |
