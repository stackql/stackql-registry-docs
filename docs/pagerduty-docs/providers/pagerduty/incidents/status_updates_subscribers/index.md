---
title: status_updates_subscribers
hide_title: false
hide_table_of_contents: false
keywords:
  - status_updates_subscribers
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
<tr><td><b>Name</b></td><td><code>status_updates_subscribers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="pagerduty.incidents.status_updates_subscribers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="has_indirect_subscription" /> | `boolean` | If this subcriber has an indirect subscription to this incident via another object |
| <CopyableCode code="subscribed_via" /> | `array` |  |
| <CopyableCode code="subscriber_id" /> | `string` | The ID of the entity being subscribed |
| <CopyableCode code="subscriber_type" /> | `string` | The type of the entity being subscribed |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_incident_notification_subscribers" /> | `SELECT` | <CopyableCode code="id" /> | Retrieve a list of Notification Subscribers on the Incident.<br /><br />&lt;!-- theme: warning --&gt;<br />&gt; Users must be added through `POST /incident/&#123;id&#125;/status_updates/subscribers` to be returned from this endpoint.<br />Scoped OAuth requires: `subscribers.read`<br /> |
| <CopyableCode code="create_incident_notification_subscribers" /> | `INSERT` | <CopyableCode code="id, data__subscribers" /> | Subscribe the given entities to Incident Status Update Notifications.<br /><br />Scoped OAuth requires: `subscribers.write`<br /> |
| <CopyableCode code="_get_incident_notification_subscribers" /> | `EXEC` | <CopyableCode code="id" /> | Retrieve a list of Notification Subscribers on the Incident.<br /><br />&lt;!-- theme: warning --&gt;<br />&gt; Users must be added through `POST /incident/&#123;id&#125;/status_updates/subscribers` to be returned from this endpoint.<br />Scoped OAuth requires: `subscribers.read`<br /> |
