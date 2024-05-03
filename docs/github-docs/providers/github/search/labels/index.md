---
title: labels
hide_title: false
hide_table_of_contents: false
keywords:
  - labels
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
<tr><td><b>Name</b></td><td><code>labels</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.search.labels" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `integer` |
| <CopyableCode code="name" /> | `string` |
| <CopyableCode code="description" /> | `string` |
| <CopyableCode code="color" /> | `string` |
| <CopyableCode code="default" /> | `boolean` |
| <CopyableCode code="node_id" /> | `string` |
| <CopyableCode code="score" /> | `number` |
| <CopyableCode code="text_matches" /> | `array` |
| <CopyableCode code="url" /> | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="labels" /> | `SELECT` | <CopyableCode code="q, repository_id" /> |
