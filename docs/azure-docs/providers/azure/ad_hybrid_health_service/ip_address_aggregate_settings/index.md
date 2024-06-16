---
title: ip_address_aggregate_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - ip_address_aggregate_settings
  - ad_hybrid_health_service
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
<tr><td><b>Name</b></td><td><code>ip_address_aggregate_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ad_hybrid_health_service.ip_address_aggregate_settings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Unique ID for the entree |
| <CopyableCode code="badPasswordAndExtranetLockoutCombinedDailyThreshold" /> | `integer` | This threshold setting defines the per day trigger for a new event to be generated in the report. |
| <CopyableCode code="badPasswordAndExtranetLockoutCombinedHourlyThreshold" /> | `integer` | This threshold setting defines the per hour trigger for a new event to be generated in the report. |
| <CopyableCode code="emailNotificationEnabled" /> | `boolean` | A value indicating whether email notification has been enabled. |
| <CopyableCode code="extranetLockoutDailyThreshold" /> | `integer` | This threshold setting defines the per hour trigger for a new event to be generated in the report. |
| <CopyableCode code="extranetLockoutHourlyThreshold" /> | `integer` | This threshold setting defines the per hour trigger for a new event to be generated in the report. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="serviceName" /> | Gets the IP address aggregate settings. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="serviceName" /> | Updates the IP address aggregate settings alert thresholds. |
