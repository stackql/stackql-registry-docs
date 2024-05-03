---
title: ref
hide_title: false
hide_table_of_contents: false
keywords:
  - ref
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
<tr><td><b>Name</b></td><td><code>ref</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.git.ref" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="node_id" /> | `string` |
| <CopyableCode code="object" /> | `object` |
| <CopyableCode code="ref" /> | `string` |
| <CopyableCode code="url" /> | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get_ref" /> | `SELECT` | <CopyableCode code="owner, ref, repo" /> |
