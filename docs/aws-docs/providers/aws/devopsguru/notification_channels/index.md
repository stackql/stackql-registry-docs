---
title: notification_channels
hide_title: false
hide_table_of_contents: false
keywords:
  - notification_channels
  - devopsguru
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Used to retrieve a list of <code>notification_channels</code> in a region or to create or delete a <code>notification_channels</code> resource, use <code>notification_channel</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>notification_channels</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>This resource schema represents the NotificationChannel resource in the Amazon DevOps Guru.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.devopsguru.notification_channels" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The ID of a notification channel.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
id
FROM aws.devopsguru.notification_channels
WHERE region = 'us-east-1';
```

## `INSERT` Example

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
    ]
}>
<TabItem value="required">

```sql
<<<json
{
 "Config": {
  "Sns": {
   "TopicArn": "{{ TopicArn }}"
  },
  "Filters": {
   "Severities": [
    "{{ Severities[0] }}"
   ],
   "MessageTypes": [
    "{{ MessageTypes[0] }}"
   ]
  }
 }
}
>>>
--required properties only
INSERT INTO aws.devopsguru.notification_channels (
 Config,
 region
)
SELECT 
{{ .Config }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Config": {
  "Sns": {
   "TopicArn": "{{ TopicArn }}"
  },
  "Filters": {
   "Severities": [
    "{{ Severities[0] }}"
   ],
   "MessageTypes": [
    "{{ MessageTypes[0] }}"
   ]
  }
 }
}
>>>
--all properties
INSERT INTO aws.devopsguru.notification_channels (
 Config,
 region
)
SELECT 
 {{ .Config }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.devopsguru.notification_channels
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>notification_channels</code> resource, the following permissions are required:

### Create
```json
devops-guru:AddNotificationChannel,
devops-guru:ListNotificationChannels,
sns:Publish,
sns:GetTopicAttributes,
sns:SetTopicAttributes
```

### List
```json
devops-guru:ListNotificationChannels
```

### Delete
```json
devops-guru:RemoveNotificationChannel,
devops-guru:ListNotificationChannels
```

