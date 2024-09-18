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
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>notification_configs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>notification_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.securitycenter.notification_configs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The relative resource name of this notification config. See: https://cloud.google.com/apis/design/resource_names#relative_resource_name Example: "organizations/{organization_id}/notificationConfigs/notify_public_bucket", "folders/{folder_id}/notificationConfigs/notify_public_bucket", or "projects/{project_id}/notificationConfigs/notify_public_bucket". |
| <CopyableCode code="description" /> | `string` | The description of the notification config (max of 1024 characters). |
| <CopyableCode code="pubsubTopic" /> | `string` | The Pub/Sub topic to send notifications to. Its format is "projects/[project_id]/topics/[topic]". |
| <CopyableCode code="serviceAccount" /> | `string` | Output only. The service account that needs "pubsub.topics.publish" permission to publish to the Pub/Sub topic. |
| <CopyableCode code="streamingConfig" /> | `object` | The config for streaming-based notifications, which send each event as soon as it is detected. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="folders_notification_configs_get" /> | `SELECT` | <CopyableCode code="foldersId, notificationConfigsId" /> | Gets a notification config. |
| <CopyableCode code="folders_notification_configs_list" /> | `SELECT` | <CopyableCode code="foldersId" /> | Lists notification configs. |
| <CopyableCode code="organizations_notification_configs_get" /> | `SELECT` | <CopyableCode code="notificationConfigsId, organizationsId" /> | Gets a notification config. |
| <CopyableCode code="organizations_notification_configs_list" /> | `SELECT` | <CopyableCode code="organizationsId" /> | Lists notification configs. |
| <CopyableCode code="projects_notification_configs_get" /> | `SELECT` | <CopyableCode code="notificationConfigsId, projectsId" /> | Gets a notification config. |
| <CopyableCode code="projects_notification_configs_list" /> | `SELECT` | <CopyableCode code="projectsId" /> | Lists notification configs. |
| <CopyableCode code="folders_notification_configs_create" /> | `INSERT` | <CopyableCode code="foldersId" /> | Creates a notification config. |
| <CopyableCode code="organizations_notification_configs_create" /> | `INSERT` | <CopyableCode code="organizationsId" /> | Creates a notification config. |
| <CopyableCode code="projects_notification_configs_create" /> | `INSERT` | <CopyableCode code="projectsId" /> | Creates a notification config. |
| <CopyableCode code="folders_notification_configs_delete" /> | `DELETE` | <CopyableCode code="foldersId, notificationConfigsId" /> | Deletes a notification config. |
| <CopyableCode code="organizations_notification_configs_delete" /> | `DELETE` | <CopyableCode code="notificationConfigsId, organizationsId" /> | Deletes a notification config. |
| <CopyableCode code="projects_notification_configs_delete" /> | `DELETE` | <CopyableCode code="notificationConfigsId, projectsId" /> | Deletes a notification config. |
| <CopyableCode code="folders_notification_configs_patch" /> | `UPDATE` | <CopyableCode code="foldersId, notificationConfigsId" /> |  Updates a notification config. The following update fields are allowed: description, pubsub_topic, streaming_config.filter |
| <CopyableCode code="organizations_notification_configs_patch" /> | `UPDATE` | <CopyableCode code="notificationConfigsId, organizationsId" /> |  Updates a notification config. The following update fields are allowed: description, pubsub_topic, streaming_config.filter |
| <CopyableCode code="projects_notification_configs_patch" /> | `UPDATE` | <CopyableCode code="notificationConfigsId, projectsId" /> |  Updates a notification config. The following update fields are allowed: description, pubsub_topic, streaming_config.filter |

## `SELECT` examples

Lists notification configs.

```sql
SELECT
name,
description,
pubsubTopic,
serviceAccount,
streamingConfig
FROM google.securitycenter.notification_configs
WHERE foldersId = '{{ foldersId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>notification_configs</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO google.securitycenter.notification_configs (
foldersId,
name,
description,
pubsubTopic,
streamingConfig
)
SELECT 
'{{ foldersId }}',
'{{ name }}',
'{{ description }}',
'{{ pubsubTopic }}',
'{{ streamingConfig }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
name: string
description: string
pubsubTopic: string
serviceAccount: string
streamingConfig:
  filter: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>notification_configs</code> resource.

```sql
/*+ update */
UPDATE google.securitycenter.notification_configs
SET 
name = '{{ name }}',
description = '{{ description }}',
pubsubTopic = '{{ pubsubTopic }}',
streamingConfig = '{{ streamingConfig }}'
WHERE 
foldersId = '{{ foldersId }}'
AND notificationConfigsId = '{{ notificationConfigsId }}';
```

## `DELETE` example

Deletes the specified <code>notification_configs</code> resource.

```sql
/*+ delete */
DELETE FROM google.securitycenter.notification_configs
WHERE foldersId = '{{ foldersId }}'
AND notificationConfigsId = '{{ notificationConfigsId }}';
```
