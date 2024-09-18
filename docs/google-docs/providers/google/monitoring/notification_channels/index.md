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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>notification_channels</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>notification_channels</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.monitoring.notification_channels" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. The full REST resource name for this channel. The format is: projects/[PROJECT_ID_OR_NUMBER]/notificationChannels/[CHANNEL_ID] The [CHANNEL_ID] is automatically assigned by the server on creation. |
| <CopyableCode code="description" /> | `string` | An optional human-readable description of this notification channel. This description may provide additional details, beyond the display name, for the channel. This may not exceed 1024 Unicode characters. |
| <CopyableCode code="creationRecord" /> | `object` | Describes a change made to a configuration. |
| <CopyableCode code="displayName" /> | `string` | An optional human-readable name for this notification channel. It is recommended that you specify a non-empty and unique name in order to make it easier to identify the channels in your project, though this is not enforced. The display name is limited to 512 Unicode characters. |
| <CopyableCode code="enabled" /> | `boolean` | Whether notifications are forwarded to the described channel. This makes it possible to disable delivery of notifications to a particular channel without removing the channel from all alerting policies that reference the channel. This is a more convenient approach when the change is temporary and you want to receive notifications from the same set of alerting policies on the channel at some point in the future. |
| <CopyableCode code="labels" /> | `object` | Configuration fields that define the channel and its behavior. The permissible and required labels are specified in the NotificationChannelDescriptor.labels of the NotificationChannelDescriptor corresponding to the type field. |
| <CopyableCode code="mutationRecords" /> | `array` | Records of the modification of this channel. |
| <CopyableCode code="type" /> | `string` | The type of the notification channel. This field matches the value of the NotificationChannelDescriptor.type field. |
| <CopyableCode code="userLabels" /> | `object` | User-supplied key/value data that does not need to conform to the corresponding NotificationChannelDescriptor's schema, unlike the labels field. This field is intended to be used for organizing and identifying the NotificationChannel objects.The field can contain up to 64 entries. Each key and value is limited to 63 Unicode characters or 128 bytes, whichever is smaller. Labels and values can contain only lowercase letters, numerals, underscores, and dashes. Keys must begin with a letter. |
| <CopyableCode code="verificationStatus" /> | `string` | Indicates whether this channel has been verified or not. On a ListNotificationChannels or GetNotificationChannel operation, this field is expected to be populated.If the value is UNVERIFIED, then it indicates that the channel is non-functioning (it both requires verification and lacks verification); otherwise, it is assumed that the channel works.If the channel is neither VERIFIED nor UNVERIFIED, it implies that the channel is of a type that does not require verification or that this specific channel has been exempted from verification because it was created prior to verification being required for channels of this type.This field cannot be modified using a standard UpdateNotificationChannel operation. To change the value of this field, you must call VerifyNotificationChannel. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_notification_channels_get" /> | `SELECT` | <CopyableCode code="notificationChannelsId, projectsId" /> | Gets a single notification channel. The channel includes the relevant configuration details with which the channel was created. However, the response may truncate or omit passwords, API keys, or other private key matter and thus the response may not be 100% identical to the information that was supplied in the call to the create method. |
| <CopyableCode code="projects_notification_channels_list" /> | `SELECT` | <CopyableCode code="projectsId" /> | Lists the notification channels that have been created for the project. To list the types of notification channels that are supported, use the ListNotificationChannelDescriptors method. |
| <CopyableCode code="projects_notification_channels_create" /> | `INSERT` | <CopyableCode code="projectsId" /> | Creates a new notification channel, representing a single notification endpoint such as an email address, SMS number, or PagerDuty service.Design your application to single-thread API calls that modify the state of notification channels in a single project. This includes calls to CreateNotificationChannel, DeleteNotificationChannel and UpdateNotificationChannel. |
| <CopyableCode code="projects_notification_channels_delete" /> | `DELETE` | <CopyableCode code="notificationChannelsId, projectsId" /> | Deletes a notification channel.Design your application to single-thread API calls that modify the state of notification channels in a single project. This includes calls to CreateNotificationChannel, DeleteNotificationChannel and UpdateNotificationChannel. |
| <CopyableCode code="projects_notification_channels_patch" /> | `UPDATE` | <CopyableCode code="notificationChannelsId, projectsId" /> | Updates a notification channel. Fields not specified in the field mask remain unchanged.Design your application to single-thread API calls that modify the state of notification channels in a single project. This includes calls to CreateNotificationChannel, DeleteNotificationChannel and UpdateNotificationChannel. |
| <CopyableCode code="projects_notification_channels_send_verification_code" /> | `EXEC` | <CopyableCode code="notificationChannelsId, projectsId" /> | Causes a verification code to be delivered to the channel. The code can then be supplied in VerifyNotificationChannel to verify the channel. |
| <CopyableCode code="projects_notification_channels_verify" /> | `EXEC` | <CopyableCode code="notificationChannelsId, projectsId" /> | Verifies a NotificationChannel by proving receipt of the code delivered to the channel as a result of calling SendNotificationChannelVerificationCode. |

## `SELECT` examples

Lists the notification channels that have been created for the project. To list the types of notification channels that are supported, use the ListNotificationChannelDescriptors method.

```sql
SELECT
name,
description,
creationRecord,
displayName,
enabled,
labels,
mutationRecords,
type,
userLabels,
verificationStatus
FROM google.monitoring.notification_channels
WHERE projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>notification_channels</code> resource.

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
INSERT INTO google.monitoring.notification_channels (
projectsId,
type,
name,
displayName,
description,
labels,
userLabels,
verificationStatus,
enabled,
creationRecord,
mutationRecords
)
SELECT 
'{{ projectsId }}',
'{{ type }}',
'{{ name }}',
'{{ displayName }}',
'{{ description }}',
'{{ labels }}',
'{{ userLabels }}',
'{{ verificationStatus }}',
true|false,
'{{ creationRecord }}',
'{{ mutationRecords }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
type: string
name: string
displayName: string
description: string
labels: object
userLabels: object
verificationStatus: string
enabled: boolean
creationRecord:
  mutateTime: string
  mutatedBy: string
mutationRecords:
  - mutateTime: string
    mutatedBy: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>notification_channels</code> resource.

```sql
/*+ update */
UPDATE google.monitoring.notification_channels
SET 
type = '{{ type }}',
name = '{{ name }}',
displayName = '{{ displayName }}',
description = '{{ description }}',
labels = '{{ labels }}',
userLabels = '{{ userLabels }}',
verificationStatus = '{{ verificationStatus }}',
enabled = true|false,
creationRecord = '{{ creationRecord }}',
mutationRecords = '{{ mutationRecords }}'
WHERE 
notificationChannelsId = '{{ notificationChannelsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>notification_channels</code> resource.

```sql
/*+ delete */
DELETE FROM google.monitoring.notification_channels
WHERE notificationChannelsId = '{{ notificationChannelsId }}'
AND projectsId = '{{ projectsId }}';
```
