---
title: notifications
hide_title: false
hide_table_of_contents: false
keywords:
  - notifications
  - advisorynotifications
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
<tr><td><b>Name</b></td><td><code>notifications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.advisorynotifications.notifications</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The resource name of the notification. Format: organizations/&#123;organization&#125;/locations/&#123;location&#125;/notifications/&#123;notification&#125;. |
| `subject` | `object` | A subject line of a notification. |
| `createTime` | `string` | Output only. Time the notification was created. |
| `messages` | `array` | A list of messages in the notification. |
| `notificationType` | `string` | Type of notification |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, notificationsId, organizationsId` | Gets a notification. |
| `list` | `SELECT` | `locationsId, organizationsId` | Lists notifications under a given parent. |
| `_list` | `EXEC` | `locationsId, organizationsId` | Lists notifications under a given parent. |
