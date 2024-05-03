---
title: past_incidents
hide_title: false
hide_table_of_contents: false
keywords:
  - past_incidents
  - incidents
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
<tr><td><b>Name</b></td><td><code>past_incidents</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="pagerduty.incidents.past_incidents" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="incident" /> | `object` | Incident model reference |
| <CopyableCode code="score" /> | `number` | The computed similarity score associated with the incident and parent incident  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get_past_incidents" /> | `SELECT` | <CopyableCode code="id" /> |
| <CopyableCode code="_get_past_incidents" /> | `EXEC` | <CopyableCode code="id" /> |
