---
title: standard_patterns
hide_title: false
hide_table_of_contents: false
keywords:
  - standard_patterns
  - sensitive_data_scanner
  - datadog    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, monitor, and manage Datadog resources using SQL
custom_edit_url: null
image: /img/providers/datadog/stackql-datadog-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>standard_patterns</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="datadog.sensitive_data_scanner.standard_patterns" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | ID of the standard pattern. |
| <CopyableCode code="attributes" /> | `object` | Attributes of the Sensitive Data Scanner standard pattern. |
| <CopyableCode code="type" /> | `string` | Sensitive Data Scanner standard pattern type. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list_standard_patterns" /> | `SELECT` | <CopyableCode code="dd_site" /> |
| <CopyableCode code="_list_standard_patterns" /> | `EXEC` | <CopyableCode code="dd_site" /> |
