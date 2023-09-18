---
title: notifications_thread_subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - notifications_thread_subscriptions
  - activity
  - github    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GitHub resources using SQL
custom_edit_url: null
image: /img/providers/github/stackql-github-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>notifications_thread_subscriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.activity.notifications_thread_subscriptions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `created_at` | `string` |
| `ignored` | `boolean` |
| `reason` | `string` |
| `repository_url` | `string` |
| `subscribed` | `boolean` |
| `thread_url` | `string` |
| `url` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_thread_subscription_for_authenticated_user` | `SELECT` | `thread_id` | This checks to see if the current user is subscribed to a thread. You can also [get a repository subscription](https://docs.github.com/rest/activity/watching#get-a-repository-subscription).<br /><br />Note that subscriptions are only generated if a user is participating in a conversation--for example, they've replied to the thread, were **@mentioned**, or manually subscribe to a thread. |
| `delete_thread_subscription` | `DELETE` | `thread_id` | Mutes all future notifications for a conversation until you comment on the thread or get an **@mention**. If you are watching the repository of the thread, you will still receive notifications. To ignore future notifications for a repository you are watching, use the [Set a thread subscription](https://docs.github.com/rest/activity/notifications#set-a-thread-subscription) endpoint and set `ignore` to `true`. |
| `set_thread_subscription` | `EXEC` | `thread_id` | If you are watching a repository, you receive notifications for all threads by default. Use this endpoint to ignore future notifications for threads until you comment on the thread or get an **@mention**.<br /><br />You can also use this endpoint to subscribe to threads that you are currently not receiving notifications for or to subscribed to threads that you have previously ignored.<br /><br />Unsubscribing from a conversation in a repository that you are not watching is functionally equivalent to the [Delete a thread subscription](https://docs.github.com/rest/activity/notifications#delete-a-thread-subscription) endpoint. |
