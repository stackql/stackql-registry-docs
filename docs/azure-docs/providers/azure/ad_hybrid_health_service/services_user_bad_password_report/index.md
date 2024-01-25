---
title: services_user_bad_password_report
hide_title: false
hide_table_of_contents: false
keywords:
  - services_user_bad_password_report
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
<tr><td><b>Name</b></td><td><code>services_user_bad_password_report</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.ad_hybrid_health_service.services_user_bad_password_report</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `ipAddress` | `string` | The IP address corresponding to the last error event. |
| `lastUpdated` | `string` | The date and time when the last error event was logged. |
| `totalErrorAttempts` | `integer` | The total count of specific error events. |
| `uniqueIpAddresses` | `string` | The list of unique IP addresses. |
| `userId` | `string` | The user ID value. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `serviceName` |
| `_list` | `EXEC` | `serviceName` |
