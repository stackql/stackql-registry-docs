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
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
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
| `name` | `string` | The full REST resource name for this channel. The format is: projects/[PROJECT_ID_OR_NUMBER]/notificationChannels/[CHANNEL_ID] The [CHANNEL_ID] is automatically assigned by the server on creation. |
| `description` | `string` | An optional human-readable description of this notification channel. This description may provide additional details, beyond the display name, for the channel. This may not exceed 1024 Unicode characters. |
| `labels` | `object` | Configuration fields that define the channel and its behavior. The permissible and required labels are specified in the NotificationChannelDescriptor.labels of the NotificationChannelDescriptor corresponding to the type field. |
| `mutationRecords` | `array` | Records of the modification of this channel. |
| `userLabels` | `object` | User-supplied key/value data that does not need to conform to the corresponding NotificationChannelDescriptor's schema, unlike the labels field. This field is intended to be used for organizing and identifying the NotificationChannel objects.The field can contain up to 64 entries. Each key and value is limited to 63 Unicode characters or 128 bytes, whichever is smaller. Labels and values can contain only lowercase letters, numerals, underscores, and dashes. Keys must begin with a letter. |
| `enabled` | `boolean` | Whether notifications are forwarded to the described channel. This makes it possible to disable delivery of notifications to a particular channel without removing the channel from all alerting policies that reference the channel. This is a more convenient approach when the change is temporary and you want to receive notifications from the same set of alerting policies on the channel at some point in the future. |
| `verificationStatus` | `string` | Indicates whether this channel has been verified or not. On a ListNotificationChannels or GetNotificationChannel operation, this field is expected to be populated.If the value is UNVERIFIED, then it indicates that the channel is non-functioning (it both requires verification and lacks verification); otherwise, it is assumed that the channel works.If the channel is neither VERIFIED nor UNVERIFIED, it implies that the channel is of a type that does not require verification or that this specific channel has been exempted from verification because it was created prior to verification being required for channels of this type.This field cannot be modified using a standard UpdateNotificationChannel operation. To change the value of this field, you must call VerifyNotificationChannel. |
| `displayName` | `string` | An optional human-readable name for this notification channel. It is recommended that you specify a non-empty and unique name in order to make it easier to identify the channels in your project, though this is not enforced. The display name is limited to 512 Unicode characters. |
| `type` | `string` | The type of the notification channel. This field matches the value of the NotificationChannelDescriptor.type field. |
| `creationRecord` | `object` | Describes a change made to a configuration. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_notificationChannels_get` | `SELECT` | `notificationChannelsId, projectsId` | Gets a single notification channel. The channel includes the relevant configuration details with which the channel was created. However, the response may truncate or omit passwords, API keys, or other private key matter and thus the response may not be 100% identical to the information that was supplied in the call to the create method. |
| `projects_notificationChannels_list` | `SELECT` | `projectsId` | Lists the notification channels that have been created for the project. |
| `projects_notificationChannels_create` | `INSERT` | `projectsId` | Creates a new notification channel, representing a single notification endpoint such as an email address, SMS number, or PagerDuty service. |
| `projects_notificationChannels_delete` | `DELETE` | `notificationChannelsId, projectsId` | Deletes a notification channel. |
| `projects_notificationChannels_patch` | `EXEC` | `notificationChannelsId, projectsId` | Updates a notification channel. Fields not specified in the field mask remain unchanged. |
| `projects_notificationChannels_sendVerificationCode` | `EXEC` | `notificationChannelsId, projectsId` | Causes a verification code to be delivered to the channel. The code can then be supplied in VerifyNotificationChannel to verify the channel. |
| `projects_notificationChannels_verify` | `EXEC` | `notificationChannelsId, projectsId` | Verifies a NotificationChannel by proving receipt of the code delivered to the channel as a result of calling SendNotificationChannelVerificationCode. |
