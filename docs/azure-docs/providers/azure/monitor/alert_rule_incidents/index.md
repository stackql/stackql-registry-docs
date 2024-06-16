---
title: alert_rule_incidents
hide_title: false
hide_table_of_contents: false
keywords:
  - alert_rule_incidents
  - monitor
  - azure    
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
<tr><td><b>Name</b></td><td><code>alert_rule_incidents</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.monitor.alert_rule_incidents" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Incident name. |
| <CopyableCode code="activatedTime" /> | `string` | The time at which the incident was activated in ISO8601 format. |
| <CopyableCode code="isActive" /> | `boolean` | A boolean to indicate whether the incident is active or resolved. |
| <CopyableCode code="resolvedTime" /> | `string` | The time at which the incident was resolved in ISO8601 format. If null, it means the incident is still active. |
| <CopyableCode code="ruleName" /> | `string` | Rule name that is associated with the incident. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="incidentName, resourceGroupName, ruleName, subscriptionId" /> | Gets an incident associated to an alert rule |
| <CopyableCode code="list_by_alert_rule" /> | `SELECT` | <CopyableCode code="resourceGroupName, ruleName, subscriptionId" /> | Gets a list of incidents associated to an alert rule |
