---
title: records
hide_title: false
hide_table_of_contents: false
keywords:
  - records
  - audit
  - pagerduty    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, manage, and integrate PagerDuty resources using SQL
custom_edit_url: null
image: /img/providers/pagerduty/stackql-pagerduty-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>records</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="pagerduty.audit.records" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` |  |
| <CopyableCode code="action" /> | `string` |  |
| <CopyableCode code="actors" /> | `array` |  |
| <CopyableCode code="details" /> | `object` | Additional details to provide further information about the action or<br />the resource that has been audited.<br /> |
| <CopyableCode code="execution_context" /> | `object` | Action execution context |
| <CopyableCode code="execution_time" /> | `string` | The date/time the action executed, in ISO8601 format and millisecond precision. |
| <CopyableCode code="method" /> | `object` | The method information |
| <CopyableCode code="root_resource" /> | `object` |  |
| <CopyableCode code="self" /> | `string` | Record URL. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list_audit_records" /> | `SELECT` |  |
| <CopyableCode code="_list_audit_records" /> | `EXEC` |  |
