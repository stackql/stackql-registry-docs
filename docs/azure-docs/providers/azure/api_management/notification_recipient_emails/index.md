---
title: notification_recipient_emails
hide_title: false
hide_table_of_contents: false
keywords:
  - notification_recipient_emails
  - api_management
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

Creates, updates, deletes, gets or lists a <code>notification_recipient_emails</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>notification_recipient_emails</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.notification_recipient_emails" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Recipient Email Contract Properties. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_by_notification" /> | `SELECT` | <CopyableCode code="notificationName, resourceGroupName, serviceName, subscriptionId" /> | Gets the list of the Notification Recipient Emails subscribed to a notification. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="email, notificationName, resourceGroupName, serviceName, subscriptionId" /> | Adds the Email address to the list of Recipients for the Notification. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="email, notificationName, resourceGroupName, serviceName, subscriptionId" /> | Removes the email from the list of Notification. |

## `SELECT` examples

Gets the list of the Notification Recipient Emails subscribed to a notification.


```sql
SELECT
properties
FROM azure.api_management.notification_recipient_emails
WHERE notificationName = '{{ notificationName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>notification_recipient_emails</code> resource.

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
INSERT INTO azure.api_management.notification_recipient_emails (
email,
notificationName,
resourceGroupName,
serviceName,
subscriptionId
)
SELECT 
'{{ email }}',
'{{ notificationName }}',
'{{ resourceGroupName }}',
'{{ serviceName }}',
'{{ subscriptionId }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props: []

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>notification_recipient_emails</code> resource.

```sql
/*+ delete */
DELETE FROM azure.api_management.notification_recipient_emails
WHERE email = '{{ email }}'
AND notificationName = '{{ notificationName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```