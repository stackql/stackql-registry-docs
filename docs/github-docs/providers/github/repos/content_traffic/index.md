---
title: content_traffic
hide_title: false
hide_table_of_contents: false
keywords:
  - content_traffic
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
<tr><td><b>Name</b></td><td><code>content_traffic</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.repos.content_traffic" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="count" /> | `integer` |
| <CopyableCode code="path" /> | `string` |
| <CopyableCode code="title" /> | `string` |
| <CopyableCode code="uniques" /> | `integer` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get_top_paths" /> | `SELECT` | <CopyableCode code="owner, repo" /> |
