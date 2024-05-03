---
title: related_incidents
hide_title: false
hide_table_of_contents: false
keywords:
  - related_incidents
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
<tr><td><b>Name</b></td><td><code>related_incidents</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="pagerduty.incidents.related_incidents" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="incident_details" /> | `object` |  |
| <CopyableCode code="relationship_details" /> | `array` | A list of reasons for why the Incident is considered related. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get_related_incidents" /> | `SELECT` | <CopyableCode code="id" /> |
| <CopyableCode code="_get_related_incidents" /> | `EXEC` | <CopyableCode code="id" /> |
