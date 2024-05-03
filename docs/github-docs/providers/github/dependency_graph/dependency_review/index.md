---
title: dependency_review
hide_title: false
hide_table_of_contents: false
keywords:
  - dependency_review
  - dependency_graph
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
<tr><td><b>Name</b></td><td><code>dependency_review</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.dependency_graph.dependency_review" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` |  |
| <CopyableCode code="change_type" /> | `string` |  |
| <CopyableCode code="ecosystem" /> | `string` |  |
| <CopyableCode code="license" /> | `string` |  |
| <CopyableCode code="manifest" /> | `string` |  |
| <CopyableCode code="package_url" /> | `string` |  |
| <CopyableCode code="scope" /> | `string` | Where the dependency is utilized. `development` means that the dependency is only utilized in the development environment. `runtime` means that the dependency is utilized at runtime and in the development environment. |
| <CopyableCode code="source_repository_url" /> | `string` |  |
| <CopyableCode code="version" /> | `string` |  |
| <CopyableCode code="vulnerabilities" /> | `array` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="diff_range" /> | `SELECT` | <CopyableCode code="basehead, owner, repo" /> |
