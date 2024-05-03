---
title: status_combined
hide_title: false
hide_table_of_contents: false
keywords:
  - status_combined
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
<tr><td><b>Name</b></td><td><code>status_combined</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.repos.status_combined" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="commit_url" /> | `string` |  |
| <CopyableCode code="repository" /> | `object` | Minimal Repository |
| <CopyableCode code="sha" /> | `string` |  |
| <CopyableCode code="state" /> | `string` |  |
| <CopyableCode code="statuses" /> | `array` |  |
| <CopyableCode code="total_count" /> | `integer` |  |
| <CopyableCode code="url" /> | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get_combined_status_for_ref" /> | `SELECT` | <CopyableCode code="owner, ref, repo" /> |
