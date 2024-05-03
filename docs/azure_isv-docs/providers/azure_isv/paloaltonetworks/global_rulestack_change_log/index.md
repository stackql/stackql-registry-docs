---
title: global_rulestack_change_log
hide_title: false
hide_table_of_contents: false
keywords:
  - global_rulestack_change_log
  - paloaltonetworks
  - azure_isv    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>global_rulestack_change_log</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.paloaltonetworks.global_rulestack_change_log" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="changes" /> | `array` | list of changes |
| <CopyableCode code="lastCommitted" /> | `string` | lastCommitted timestamp |
| <CopyableCode code="lastModified" /> | `string` | lastModified timestamp |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="globalRulestackName" /> |
