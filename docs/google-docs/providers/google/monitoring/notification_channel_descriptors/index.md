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
image: /img/providers/google/stackql-google-provider-featured-image.png
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
| `channelDescriptors` | `array` | The monitored resource descriptors supported for the specified project, optionally filtered. |
| `nextPageToken` | `string` | If not empty, indicates that there may be more results that match the request. Use the value in the page_token field in a subsequent request to fetch the next set of results. If empty, all results have been returned. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_notification_channel_descriptors_get` | `SELECT` | `notificationChannelDescriptorsId, projectsId` | Gets a single channel descriptor. The descriptor indicates which fields are expected / permitted for a notification channel of the given type. |
| `projects_notification_channel_descriptors_list` | `SELECT` | `projectsId` | Lists the descriptors for supported channel types. The use of descriptors makes it possible for new channel types to be dynamically added. |
