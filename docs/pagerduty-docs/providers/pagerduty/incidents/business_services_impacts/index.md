---
title: business_services_impacts
hide_title: false
hide_table_of_contents: false
keywords:
  - business_services_impacts
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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>business_services_impacts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>pagerduty.incidents.business_services_impacts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` |  |
| `name` | `string` |  |
| `additional_fields` | `object` |  |
| `status` | `string` | The current impact status of the object |
| `type` | `string` | The kind of object that has been impacted |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_incident_impacted_business_services` | `SELECT` | `X-EARLY-ACCESS, id` | Retrieve a list of Business Services that are being impacted by the given Incident.<br /><br />&lt;!-- theme: warning --&gt;<br />&gt; ### Early Access<br />&gt; This endpoint is in Early Access and may change at any time. You must pass in the X-EARLY-ACCESS header to access it. |
| `_get_incident_impacted_business_services` | `EXEC` | `X-EARLY-ACCESS, id` | Retrieve a list of Business Services that are being impacted by the given Incident.<br /><br />&lt;!-- theme: warning --&gt;<br />&gt; ### Early Access<br />&gt; This endpoint is in Early Access and may change at any time. You must pass in the X-EARLY-ACCESS header to access it. |
| `put_incident_manual_business_service_association` | `EXEC` | `X-EARLY-ACCESS, business_service_id, id, data__relation` | Change Impact of an Incident on a Business Service.<br /><br />&lt;!-- theme: warning --&gt;<br />&gt; ### Early Access<br />&gt; This endpoint is in Early Access and may change at any time. You must pass in the X-EARLY-ACCESS header to access it. |
