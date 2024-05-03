---
title: status_dashboards
hide_title: false
hide_table_of_contents: false
keywords:
  - status_dashboards
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
<tr><td><b>Name</b></td><td><code>status_dashboards</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="pagerduty.status_dashboards.status_dashboards" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="name" /> | `string` |
| <CopyableCode code="url_slug" /> | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_status_dashboard_by_id" /> | `SELECT` | <CopyableCode code="X-EARLY-ACCESS, id" /> | Get a Status Dashboard by its PagerDuty `id`.<br /><br />&lt;!-- theme: warning --&gt;<br />&gt; ### Early Access<br />&gt; This endpoint is in Early Access and may change at any time. You must pass in the X-EARLY-ACCESS header to access it. |
| <CopyableCode code="list_status_dashboards" /> | `SELECT` | <CopyableCode code="X-EARLY-ACCESS" /> | Get all your account's custom Status Dashboard views<br /><br />&lt;!-- theme: warning --&gt;<br />&gt; ### Early Access<br />&gt; This endpoint is in Early Access and may change at any time. You must pass in the X-EARLY-ACCESS header to access it. |
| <CopyableCode code="_get_status_dashboard_by_id" /> | `EXEC` | <CopyableCode code="X-EARLY-ACCESS, id" /> | Get a Status Dashboard by its PagerDuty `id`.<br /><br />&lt;!-- theme: warning --&gt;<br />&gt; ### Early Access<br />&gt; This endpoint is in Early Access and may change at any time. You must pass in the X-EARLY-ACCESS header to access it. |
| <CopyableCode code="_list_status_dashboards" /> | `EXEC` | <CopyableCode code="X-EARLY-ACCESS" /> | Get all your account's custom Status Dashboard views<br /><br />&lt;!-- theme: warning --&gt;<br />&gt; ### Early Access<br />&gt; This endpoint is in Early Access and may change at any time. You must pass in the X-EARLY-ACCESS header to access it. |
