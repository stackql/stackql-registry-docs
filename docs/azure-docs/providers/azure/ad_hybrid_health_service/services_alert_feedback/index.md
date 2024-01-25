---
title: services_alert_feedback
hide_title: false
hide_table_of_contents: false
keywords:
  - services_alert_feedback
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
<tr><td><b>Name</b></td><td><code>services_alert_feedback</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.ad_hybrid_health_service.services_alert_feedback</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `comment` | `string` | Additional comments related to the alert. |
| `consentedToShare` | `boolean` | Indicates if the alert feedback can be shared from product team. |
| `createdDate` | `string` | The date and time,in UTC,when the alert was created. |
| `feedback` | `string` | The feedback for the alert which indicates if the customer likes or dislikes the alert. |
| `level` | `string` | The alert level which indicates the severity of the alert. |
| `serviceMemberId` | `string` | The server Id of the alert. |
| `shortName` | `string` | The alert short name. |
| `state` | `string` | The alert state which can be either active or resolved with multiple resolution types. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `serviceName, shortName` |
| `_list` | `EXEC` | `serviceName, shortName` |
