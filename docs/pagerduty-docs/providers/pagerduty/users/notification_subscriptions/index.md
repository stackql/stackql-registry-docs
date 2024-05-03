---
title: notification_subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - notification_subscriptions
  - users
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
<tr><td><b>Name</b></td><td><code>notification_subscriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="pagerduty.users.notification_subscriptions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="subscribable_name" /> | `string` | The name of the subscribable |
| <CopyableCode code="subscription" /> | `object` | An object describing the relationship of a NotificationSubscriber and a NotificationSubscribable. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_user_notification_subscriptions" /> | `SELECT` | <CopyableCode code="id" /> | Retrieve a list of Notification Subscriptions the given User has.<br /><br />&lt;!-- theme: warning --&gt;<br />&gt; Users must be added through `POST /users/&#123;id&#125;/notification_subscriptions` to be returned from this endpoint.<br /><br />Scoped OAuth requires: `subscribers.read`<br /> |
| <CopyableCode code="create_user_notification_subscriptions" /> | `INSERT` | <CopyableCode code="id, data__subscribables" /> | Create new Notification Subscriptions for the given User.<br /><br />Scoped OAuth requires: `subscribers.write`<br /> |
| <CopyableCode code="_get_user_notification_subscriptions" /> | `EXEC` | <CopyableCode code="id" /> | Retrieve a list of Notification Subscriptions the given User has.<br /><br />&lt;!-- theme: warning --&gt;<br />&gt; Users must be added through `POST /users/&#123;id&#125;/notification_subscriptions` to be returned from this endpoint.<br /><br />Scoped OAuth requires: `subscribers.read`<br /> |
| <CopyableCode code="unsubscribe_user_notification_subscriptions" /> | `EXEC` | <CopyableCode code="id, data__subscribables" /> | Unsubscribe the given User from Notifications on the matching Subscribable entities.<br /><br />Scoped OAuth requires: `subscribers.write`<br /> |
