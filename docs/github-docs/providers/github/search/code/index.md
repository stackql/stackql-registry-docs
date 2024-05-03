---
title: code
hide_title: false
hide_table_of_contents: false
keywords:
  - code
  - search
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
<tr><td><b>Name</b></td><td><code>code</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.search.code" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` |  |
| <CopyableCode code="file_size" /> | `integer` |  |
| <CopyableCode code="git_url" /> | `string` |  |
| <CopyableCode code="html_url" /> | `string` |  |
| <CopyableCode code="language" /> | `string` |  |
| <CopyableCode code="last_modified_at" /> | `string` |  |
| <CopyableCode code="line_numbers" /> | `array` |  |
| <CopyableCode code="path" /> | `string` |  |
| <CopyableCode code="repository" /> | `object` | Minimal Repository |
| <CopyableCode code="score" /> | `number` |  |
| <CopyableCode code="sha" /> | `string` |  |
| <CopyableCode code="text_matches" /> | `array` |  |
| <CopyableCode code="url" /> | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="code" /> | `SELECT` | <CopyableCode code="q" /> |
