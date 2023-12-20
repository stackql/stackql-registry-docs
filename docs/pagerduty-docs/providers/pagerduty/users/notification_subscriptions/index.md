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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>notification_subscriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>pagerduty.users.notification_subscriptions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `subscribable_name` | `string` | The name of the subscribable |
| `subscription` | `object` | An object describing the relationship of a NotificationSubscriber and a NotificationSubscribable. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_user_notification_subscriptions` | `SELECT` | `id` | Retrieve a list of Notification Subscriptions the given User has.<br /><br />&lt;!-- theme: warning --&gt;<br />&gt; Users must be added through `POST /users/&#123;id&#125;/notification_subscriptions` to be returned from this endpoint.<br /><br />Scoped OAuth requires: `subscribers.read`<br /> |
| `create_user_notification_subscriptions` | `INSERT` | `id, data__subscribables` | Create new Notification Subscriptions for the given User.<br /><br />Scoped OAuth requires: `subscribers.write`<br /> |
| `_get_user_notification_subscriptions` | `EXEC` | `id` | Retrieve a list of Notification Subscriptions the given User has.<br /><br />&lt;!-- theme: warning --&gt;<br />&gt; Users must be added through `POST /users/&#123;id&#125;/notification_subscriptions` to be returned from this endpoint.<br /><br />Scoped OAuth requires: `subscribers.read`<br /> |
| `unsubscribe_user_notification_subscriptions` | `EXEC` | `id, data__subscribables` | Unsubscribe the given User from Notifications on the matching Subscribable entities.<br /><br />Scoped OAuth requires: `subscribers.write`<br /> |
