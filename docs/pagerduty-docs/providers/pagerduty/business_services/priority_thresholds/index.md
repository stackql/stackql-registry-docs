---
title: priority_thresholds
hide_title: false
hide_table_of_contents: false
keywords:
  - priority_thresholds
  - business_services
  - pagerduty    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, manage, and integrate PagerDuty resources using SQL
custom_edit_url: null
image: /img/providers/pagerduty/stackql-pagerduty-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>priority_thresholds</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>pagerduty.business_services.priority_thresholds</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `order` | `integer` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_business_service_priority_thresholds` | `SELECT` | `X-EARLY-ACCESS` | Retrieves the priority threshold information for an account.  Currently, there is a `global_threshold` that can be set for the account.  Incidents that have a priority meeting or exceeding this threshold will be considered impacting on any Business Service that depends on the Service to which the Incident belongs.<br /><br />&lt;!-- theme: warning --&gt;<br />&gt; ### Early Access<br />&gt; This endpoint is in Early Access and may change at any time. You must pass in the X-EARLY-ACCESS header to access it. |
| `delete_business_service_priority_thresholds` | `DELETE` | `X-EARLY-ACCESS` | Clears the Priority Threshold for the account.  If the priority threshold is cleared, any Incident with a Priority set will be able to impact Business Services.<br /><br />&lt;!-- theme: warning --&gt;<br />&gt; ### Early Access<br />&gt; This endpoint is in Early Access and may change at any time. You must pass in the X-EARLY-ACCESS header to access it. |
| `_get_business_service_priority_thresholds` | `EXEC` | `X-EARLY-ACCESS` | Retrieves the priority threshold information for an account.  Currently, there is a `global_threshold` that can be set for the account.  Incidents that have a priority meeting or exceeding this threshold will be considered impacting on any Business Service that depends on the Service to which the Incident belongs.<br /><br />&lt;!-- theme: warning --&gt;<br />&gt; ### Early Access<br />&gt; This endpoint is in Early Access and may change at any time. You must pass in the X-EARLY-ACCESS header to access it. |
| `put_business_service_priority_thresholds` | `EXEC` | `X-EARLY-ACCESS, data__global_threshold` | Set the Account-level priority threshold for Business Service.<br /><br />&lt;!-- theme: warning --&gt;<br />&gt; ### Early Access<br />&gt; This endpoint is in Early Access and may change at any time. You must pass in the X-EARLY-ACCESS header to access it. |
