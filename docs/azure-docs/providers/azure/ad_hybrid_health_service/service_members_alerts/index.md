---
title: service_members_alerts
hide_title: false
hide_table_of_contents: false
keywords:
  - service_members_alerts
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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service_members_alerts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.ad_hybrid_health_service.service_members_alerts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `description` | `string` | The alert description. |
| `activeAlertProperties` | `array` | The active alert properties. |
| `additionalInformation` | `array` | Additional information related to the alert. |
| `alertId` | `string` | The alert Id. |
| `createdDate` | `string` | The date and time,in UTC,when the alert was created. |
| `displayName` | `string` | The display name for the alert. |
| `lastUpdated` | `string` | The date and time, in UTC, when the alert was last updated. |
| `level` | `string` | The alert level which indicates the severity of the alert. |
| `monitorRoleType` | `string` | The monitoring role type for which the alert was raised. |
| `relatedLinks` | `array` | The help links to get more information related to the alert. |
| `remediation` | `string` | The alert remediation. |
| `resolvedAlertProperties` | `array` | The resolved alert properties. |
| `resolvedDate` | `string` | The date and time, in UTC, when the alert was resolved. |
| `scope` | `string` | The scope of the alert. Indicates if it is a service or a server related alert. |
| `serviceId` | `string` | The service Id. |
| `serviceMemberId` | `string` | The server Id. |
| `shortName` | `string` | The alert short name. |
| `state` | `string` | The alert state which can be either active or resolved with multiple resolution types. |
| `tenantId` | `string` | The tenant Id. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `serviceMemberId, serviceName` |
| `_list` | `EXEC` | `serviceMemberId, serviceName` |
