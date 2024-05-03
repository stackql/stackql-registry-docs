---
title: blobs
hide_title: false
hide_table_of_contents: false
keywords:
  - blobs
  - git
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
<tr><td><b>Name</b></td><td><code>blobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.git.blobs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="content" /> | `string` |
| <CopyableCode code="encoding" /> | `string` |
| <CopyableCode code="highlighted_content" /> | `string` |
| <CopyableCode code="node_id" /> | `string` |
| <CopyableCode code="sha" /> | `string` |
| <CopyableCode code="size" /> | `integer` |
| <CopyableCode code="url" /> | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_blob" /> | `SELECT` | <CopyableCode code="file_sha, owner, repo" /> | The `content` in the response will always be Base64 encoded.<br /><br />_Note_: This API supports blobs up to 100 megabytes in size. |
| <CopyableCode code="create_blob" /> | `INSERT` | <CopyableCode code="owner, repo, data__content" /> |  |
