---
title: subscribers
hide_title: false
hide_table_of_contents: false
keywords:
  - subscribers
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
<tr><td><b>Name</b></td><td><code>subscribers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>pagerduty.business_services.subscribers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `subscriber_id` | `string` | The ID of the entity being subscribed |
| `subscriber_type` | `string` | The type of the entity being subscribed |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_business_service_subscribers` | `SELECT` | `id` | Retrieve a list of Notification Subscribers on the Business Service.<br /><br />&lt;!-- theme: warning --&gt;<br />&gt; Users must be added through `POST /business_services/&#123;id&#125;/subscribers` to be returned from this endpoint.<br />Scoped OAuth requires: `subscribers.read`<br /> |
| `create_business_service_notification_subscribers` | `INSERT` | `id, data__subscribers` | Subscribe the given entities to the given Business Service.<br /><br />Scoped OAuth requires: `subscribers.write`<br /> |
| `_get_business_service_subscribers` | `EXEC` | `id` | Retrieve a list of Notification Subscribers on the Business Service.<br /><br />&lt;!-- theme: warning --&gt;<br />&gt; Users must be added through `POST /business_services/&#123;id&#125;/subscribers` to be returned from this endpoint.<br />Scoped OAuth requires: `subscribers.read`<br /> |
