---
title: revisions
hide_title: false
hide_table_of_contents: false
keywords:
  - revisions
  - gists
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
<tr><td><b>Name</b></td><td><code>revisions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.gists.revisions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` |  |
| <CopyableCode code="description" /> | `string` |  |
| <CopyableCode code="comments" /> | `integer` |  |
| <CopyableCode code="comments_url" /> | `string` |  |
| <CopyableCode code="commits_url" /> | `string` |  |
| <CopyableCode code="created_at" /> | `string` |  |
| <CopyableCode code="files" /> | `object` |  |
| <CopyableCode code="fork_of" /> | `object` | Gist |
| <CopyableCode code="forks" /> | `array` |  |
| <CopyableCode code="forks_url" /> | `string` |  |
| <CopyableCode code="git_pull_url" /> | `string` |  |
| <CopyableCode code="git_push_url" /> | `string` |  |
| <CopyableCode code="history" /> | `array` |  |
| <CopyableCode code="html_url" /> | `string` |  |
| <CopyableCode code="node_id" /> | `string` |  |
| <CopyableCode code="owner" /> | `object` | A GitHub user. |
| <CopyableCode code="public" /> | `boolean` |  |
| <CopyableCode code="truncated" /> | `boolean` |  |
| <CopyableCode code="updated_at" /> | `string` |  |
| <CopyableCode code="url" /> | `string` |  |
| <CopyableCode code="user" /> | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get_revision" /> | `SELECT` | <CopyableCode code="gist_id, sha" /> |
