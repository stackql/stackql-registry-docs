---
title: commits
hide_title: false
hide_table_of_contents: false
keywords:
  - commits
  - pulls
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
<tr><td><b>Name</b></td><td><code>commits</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.pulls.commits" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="author" /> | `object` | A GitHub user. |
| <CopyableCode code="comments_url" /> | `string` |  |
| <CopyableCode code="commit" /> | `object` |  |
| <CopyableCode code="committer" /> | `object` | A GitHub user. |
| <CopyableCode code="files" /> | `array` |  |
| <CopyableCode code="html_url" /> | `string` |  |
| <CopyableCode code="node_id" /> | `string` |  |
| <CopyableCode code="parents" /> | `array` |  |
| <CopyableCode code="sha" /> | `string` |  |
| <CopyableCode code="stats" /> | `object` |  |
| <CopyableCode code="url" /> | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list_commits" /> | `SELECT` | <CopyableCode code="owner, pull_number, repo" /> |
