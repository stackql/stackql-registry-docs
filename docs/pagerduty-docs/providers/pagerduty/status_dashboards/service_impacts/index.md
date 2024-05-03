---
title: service_impacts
hide_title: false
hide_table_of_contents: false
keywords:
  - service_impacts
  - status_dashboards
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
<tr><td><b>Name</b></td><td><code>service_impacts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="pagerduty.status_dashboards.service_impacts" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` |  |
| <CopyableCode code="name" /> | `string` |  |
| <CopyableCode code="additional_fields" /> | `object` |  |
| <CopyableCode code="status" /> | `string` | The current impact status of the object |
| <CopyableCode code="type" /> | `string` | The kind of object that has been impacted |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get_status_dashboard_service_impacts_by_id" /> | `SELECT` | <CopyableCode code="X-EARLY-ACCESS, id" /> |
| <CopyableCode code="_get_status_dashboard_service_impacts_by_id" /> | `EXEC` | <CopyableCode code="X-EARLY-ACCESS, id" /> |
