
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets an <code>notification_channel_descriptor</code> resource or lists <code>notification_channel_descriptors</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>notification_channel_descriptors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.monitoring.notification_channel_descriptors" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The full REST resource name for this descriptor. The format is: projects/[PROJECT_ID_OR_NUMBER]/notificationChannelDescriptors/[TYPE] In the above, [TYPE] is the value of the type field. |
| <CopyableCode code="description" /> | `string` | A human-readable description of the notification channel type. The description may include a description of the properties of the channel and pointers to external documentation. |
| <CopyableCode code="displayName" /> | `string` | A human-readable name for the notification channel type. This form of the name is suitable for a user interface. |
| <CopyableCode code="labels" /> | `array` | The set of labels that must be defined to identify a particular channel of the corresponding type. Each label includes a description for how that field should be populated. |
| <CopyableCode code="launchStage" /> | `string` | The product launch stage for channels of this type. |
| <CopyableCode code="supportedTiers" /> | `array` | The tiers that support this notification channel; the project service tier must be one of the supported_tiers. |
| <CopyableCode code="type" /> | `string` | The type of notification channel, such as "email" and "sms". To view the full list of channels, see Channel descriptors (https://cloud.google.com/monitoring/alerts/using-channels-api#ncd). Notification channel types are globally unique. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_notification_channel_descriptors_get" /> | `SELECT` | <CopyableCode code="notificationChannelDescriptorsId, projectsId" /> | Gets a single channel descriptor. The descriptor indicates which fields are expected / permitted for a notification channel of the given type. |
| <CopyableCode code="projects_notification_channel_descriptors_list" /> | `SELECT` | <CopyableCode code="projectsId" /> | Lists the descriptors for supported channel types. The use of descriptors makes it possible for new channel types to be dynamically added. |

## `SELECT` examples

Lists the descriptors for supported channel types. The use of descriptors makes it possible for new channel types to be dynamically added.

```sql
SELECT
name,
description,
displayName,
labels,
launchStage,
supportedTiers,
type
FROM google.monitoring.notification_channel_descriptors
WHERE projectsId = '{{ projectsId }}'; 
```
