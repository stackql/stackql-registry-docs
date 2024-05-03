---
title: comments_for_review
hide_title: false
hide_table_of_contents: false
keywords:
  - comments_for_review
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
<tr><td><b>Name</b></td><td><code>comments_for_review</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.pulls.comments_for_review" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `integer` |  |
| <CopyableCode code="_links" /> | `object` |  |
| <CopyableCode code="author_association" /> | `string` | How the author is associated with the repository. |
| <CopyableCode code="body" /> | `string` |  |
| <CopyableCode code="body_html" /> | `string` |  |
| <CopyableCode code="body_text" /> | `string` |  |
| <CopyableCode code="commit_id" /> | `string` |  |
| <CopyableCode code="created_at" /> | `string` |  |
| <CopyableCode code="diff_hunk" /> | `string` |  |
| <CopyableCode code="html_url" /> | `string` |  |
| <CopyableCode code="in_reply_to_id" /> | `integer` |  |
| <CopyableCode code="line" /> | `integer` | The line of the blob to which the comment applies. The last line of the range for a multi-line comment |
| <CopyableCode code="node_id" /> | `string` |  |
| <CopyableCode code="original_commit_id" /> | `string` |  |
| <CopyableCode code="original_line" /> | `integer` | The original line of the blob to which the comment applies. The last line of the range for a multi-line comment |
| <CopyableCode code="original_position" /> | `integer` |  |
| <CopyableCode code="original_start_line" /> | `integer` | The original first line of the range for a multi-line comment. |
| <CopyableCode code="path" /> | `string` |  |
| <CopyableCode code="position" /> | `integer` |  |
| <CopyableCode code="pull_request_review_id" /> | `integer` |  |
| <CopyableCode code="pull_request_url" /> | `string` |  |
| <CopyableCode code="reactions" /> | `object` |  |
| <CopyableCode code="side" /> | `string` | The side of the first line of the range for a multi-line comment. |
| <CopyableCode code="start_line" /> | `integer` | The first line of the range for a multi-line comment. |
| <CopyableCode code="start_side" /> | `string` | The side of the first line of the range for a multi-line comment. |
| <CopyableCode code="updated_at" /> | `string` |  |
| <CopyableCode code="url" /> | `string` |  |
| <CopyableCode code="user" /> | `object` | A GitHub user. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list_comments_for_review" /> | `SELECT` | <CopyableCode code="owner, pull_number, repo, review_id" /> |
