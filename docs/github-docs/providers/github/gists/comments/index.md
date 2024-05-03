---
title: comments
hide_title: false
hide_table_of_contents: false
keywords:
  - comments
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
<tr><td><b>Name</b></td><td><code>comments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.gists.comments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `integer` |  |
| <CopyableCode code="author_association" /> | `string` | How the author is associated with the repository. |
| <CopyableCode code="body" /> | `string` | The comment text. |
| <CopyableCode code="created_at" /> | `string` |  |
| <CopyableCode code="node_id" /> | `string` |  |
| <CopyableCode code="updated_at" /> | `string` |  |
| <CopyableCode code="url" /> | `string` |  |
| <CopyableCode code="user" /> | `object` | A GitHub user. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get_comment" /> | `SELECT` | <CopyableCode code="comment_id, gist_id" /> |
| <CopyableCode code="list_comments" /> | `SELECT` | <CopyableCode code="gist_id" /> |
| <CopyableCode code="create_comment" /> | `INSERT` | <CopyableCode code="gist_id, data__body" /> |
| <CopyableCode code="delete_comment" /> | `DELETE` | <CopyableCode code="comment_id, gist_id" /> |
| <CopyableCode code="update_comment" /> | `EXEC` | <CopyableCode code="comment_id, gist_id, data__body" /> |
