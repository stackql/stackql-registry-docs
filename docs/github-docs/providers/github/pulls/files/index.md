---
title: files
hide_title: false
hide_table_of_contents: false
keywords:
  - files
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
<tr><td><b>Name</b></td><td><code>files</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.pulls.files" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="additions" /> | `integer` |
| <CopyableCode code="blob_url" /> | `string` |
| <CopyableCode code="changes" /> | `integer` |
| <CopyableCode code="contents_url" /> | `string` |
| <CopyableCode code="deletions" /> | `integer` |
| <CopyableCode code="filename" /> | `string` |
| <CopyableCode code="patch" /> | `string` |
| <CopyableCode code="previous_filename" /> | `string` |
| <CopyableCode code="raw_url" /> | `string` |
| <CopyableCode code="sha" /> | `string` |
| <CopyableCode code="status" /> | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list_files" /> | `SELECT` | <CopyableCode code="owner, pull_number, repo" /> |
