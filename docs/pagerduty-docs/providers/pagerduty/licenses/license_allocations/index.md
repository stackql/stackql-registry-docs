---
title: license_allocations
hide_title: false
hide_table_of_contents: false
keywords:
  - license_allocations
  - licenses
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
<tr><td><b>Name</b></td><td><code>license_allocations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="pagerduty.licenses.license_allocations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="allocated_at" /> | `string` | Indicates the date and time the License was allocated to the User |
| <CopyableCode code="license" /> | `object` |  |
| <CopyableCode code="user" /> | `object` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list_license_allocations" /> | `SELECT` |  |
| <CopyableCode code="_list_license_allocations" /> | `EXEC` |  |
