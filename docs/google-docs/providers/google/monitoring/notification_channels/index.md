---
title: notification_channels
hide_title: false
hide_table_of_contents: false
keywords:
  - notification_channels
  - monitoring
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>notification_channels</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.monitoring.notification_channels</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `notificationChannels` | `array` | The notification channels defined for the specified project. |
| `totalSize` | `integer` | The total number of notification channels in all pages. This number is only an estimate, and may change in subsequent pages. https://aip.dev/158 |
| `nextPageToken` | `string` | If not empty, indicates that there may be more results that match the request. Use the value in the page_token field in a subsequent request to fetch the next set of results. If empty, all results have been returned. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_notification_channels_list` | `SELECT` | `projectsId` | Lists the notification channels that have been created for the project. To list the types of notification channels that are supported, use the ListNotificationChannelDescriptors method. |
| `projects_notification_channels_create` | `INSERT` | `projectsId` | Creates a new notification channel, representing a single notification endpoint such as an email address, SMS number, or PagerDuty service.Design your application to single-thread API calls that modify the state of notification channels in a single project. This includes calls to CreateNotificationChannel, DeleteNotificationChannel and UpdateNotificationChannel. |
| `projects_notification_channels_delete` | `DELETE` | `notificationChannelsId, projectsId` | Deletes a notification channel.Design your application to single-thread API calls that modify the state of notification channels in a single project. This includes calls to CreateNotificationChannel, DeleteNotificationChannel and UpdateNotificationChannel. |
| `projects_notification_channels_get` | `EXEC` | `notificationChannelsId, projectsId` | Gets a single notification channel. The channel includes the relevant configuration details with which the channel was created. However, the response may truncate or omit passwords, API keys, or other private key matter and thus the response may not be 100% identical to the information that was supplied in the call to the create method. |
| `projects_notification_channels_patch` | `EXEC` | `notificationChannelsId, projectsId` | Updates a notification channel. Fields not specified in the field mask remain unchanged.Design your application to single-thread API calls that modify the state of notification channels in a single project. This includes calls to CreateNotificationChannel, DeleteNotificationChannel and UpdateNotificationChannel. |
| `projects_notification_channels_send_verification_code` | `EXEC` | `notificationChannelsId, projectsId` | Causes a verification code to be delivered to the channel. The code can then be supplied in VerifyNotificationChannel to verify the channel. |
| `projects_notification_channels_verify` | `EXEC` | `notificationChannelsId, projectsId` | Verifies a NotificationChannel by proving receipt of the code delivered to the channel as a result of calling SendNotificationChannelVerificationCode. |
