---
title: annotations
hide_title: false
hide_table_of_contents: false
keywords:
  - annotations
  - checks
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
<tr><td><b>Name</b></td><td><code>annotations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.checks.annotations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="annotation_level" /> | `string` |
| <CopyableCode code="blob_href" /> | `string` |
| <CopyableCode code="end_column" /> | `integer` |
| <CopyableCode code="end_line" /> | `integer` |
| <CopyableCode code="message" /> | `string` |
| <CopyableCode code="path" /> | `string` |
| <CopyableCode code="raw_details" /> | `string` |
| <CopyableCode code="start_column" /> | `integer` |
| <CopyableCode code="start_line" /> | `integer` |
| <CopyableCode code="title" /> | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list_annotations" /> | `SELECT` | <CopyableCode code="check_run_id, owner, repo" /> |
