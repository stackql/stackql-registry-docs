---
title: notification_channel_descriptors
hide_title: false
hide_table_of_contents: false
keywords:
  - notification_channel_descriptors
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
<tr><td><b>Name</b></td><td><code>notification_channel_descriptors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.monitoring.notification_channel_descriptors</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The full REST resource name for this descriptor. The format is: projects/[PROJECT_ID_OR_NUMBER]/notificationChannelDescriptors/[TYPE] In the above, [TYPE] is the value of the type field. |
| `description` | `string` | A human-readable description of the notification channel type. The description may include a description of the properties of the channel and pointers to external documentation. |
| `displayName` | `string` | A human-readable name for the notification channel type. This form of the name is suitable for a user interface. |
| `labels` | `array` | The set of labels that must be defined to identify a particular channel of the corresponding type. Each label includes a description for how that field should be populated. |
| `launchStage` | `string` | The product launch stage for channels of this type. |
| `supportedTiers` | `array` | The tiers that support this notification channel; the project service tier must be one of the supported_tiers. |
| `type` | `string` | The type of notification channel, such as "email" and "sms". To view the full list of channels, see Channel descriptors (https://cloud.google.com/monitoring/alerts/using-channels-api#ncd). Notification channel types are globally unique. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_notificationChannelDescriptors_get` | `SELECT` | `notificationChannelDescriptorsId, projectsId` | Gets a single channel descriptor. The descriptor indicates which fields are expected / permitted for a notification channel of the given type. |
| `projects_notificationChannelDescriptors_list` | `SELECT` | `projectsId` | Lists the descriptors for supported channel types. The use of descriptors makes it possible for new channel types to be dynamically added. |
