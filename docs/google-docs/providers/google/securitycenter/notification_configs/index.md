---
title: notification_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - notification_configs
  - securitycenter
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
<tr><td><b>Name</b></td><td><code>notification_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.securitycenter.notification_configs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The relative resource name of this notification config. See: https://cloud.google.com/apis/design/resource_names#relative_resource_name Example: "organizations/{organization_id}/notificationConfigs/notify_public_bucket". |
| `description` | `string` | The description of the notification config (max of 1024 characters). |
| `pubsubTopic` | `string` | The Pub/Sub topic to send notifications to. Its format is "projects/[project_id]/topics/[topic]". |
| `serviceAccount` | `string` | Output only. The service account that needs "pubsub.topics.publish" permission to publish to the Pub/Sub topic. |
| `streamingConfig` | `object` | The config for streaming-based notifications, which send each event as soon as it is detected. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `organizations_notificationConfigs_get` | `SELECT` | `notificationConfigsId, organizationsId` | Gets a notification config. |
| `organizations_notificationConfigs_list` | `SELECT` | `organizationsId` | Lists notification configs. |
| `organizations_notificationConfigs_create` | `INSERT` | `organizationsId` | Creates a notification config. |
| `organizations_notificationConfigs_delete` | `DELETE` | `notificationConfigsId, organizationsId` | Deletes a notification config. |
| `organizations_notificationConfigs_patch` | `EXEC` | `notificationConfigsId, organizationsId` |  Updates a notification config. The following update fields are allowed: description, pubsub_topic, streaming_config.filter |
