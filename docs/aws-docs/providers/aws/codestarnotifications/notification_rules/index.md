---
title: notification_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - notification_rules
  - codestarnotifications
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


Used to retrieve a list of <code>notification_rules</code> in a region or to create or delete a <code>notification_rules</code> resource, use <code>notification_rule</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>notification_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::CodeStarNotifications::NotificationRule</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.codestarnotifications.notification_rules" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
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
arn
FROM aws.codestarnotifications.notification_rules
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
 "EventTypeIds": [
  "{{ EventTypeIds[0] }}"
 ],
 "DetailType": "{{ DetailType }}",
 "Resource": "{{ Resource }}",
 "Targets": [
  {
   "TargetType": "{{ TargetType }}",
   "TargetAddress": "{{ TargetAddress }}"
  }
 ],
 "Name": "{{ Name }}"
}
>>>
--required properties only
INSERT INTO aws.codestarnotifications.notification_rules (
 EventTypeIds,
 DetailType,
 Resource,
 Targets,
 Name,
 region
)
SELECT 
{{ EventTypeIds }},
 {{ DetailType }},
 {{ Resource }},
 {{ Targets }},
 {{ Name }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "EventTypeId": "{{ EventTypeId }}",
 "CreatedBy": "{{ CreatedBy }}",
 "TargetAddress": "{{ TargetAddress }}",
 "EventTypeIds": [
  "{{ EventTypeIds[0] }}"
 ],
 "Status": "{{ Status }}",
 "DetailType": "{{ DetailType }}",
 "Resource": "{{ Resource }}",
 "Targets": [
  {
   "TargetType": "{{ TargetType }}",
   "TargetAddress": "{{ TargetAddress }}"
  }
 ],
 "Tags": {},
 "Name": "{{ Name }}"
}
>>>
--all properties
INSERT INTO aws.codestarnotifications.notification_rules (
 EventTypeId,
 CreatedBy,
 TargetAddress,
 EventTypeIds,
 Status,
 DetailType,
 Resource,
 Targets,
 Tags,
 Name,
 region
)
SELECT 
 {{ EventTypeId }},
 {{ CreatedBy }},
 {{ TargetAddress }},
 {{ EventTypeIds }},
 {{ Status }},
 {{ DetailType }},
 {{ Resource }},
 {{ Targets }},
 {{ Tags }},
 {{ Name }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.codestarnotifications.notification_rules
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>notification_rules</code> resource, the following permissions are required:

### Create
```json
codestar-notifications:createNotificationRule
```

### List
```json
codestar-notifications:listNotificationRules
```

### Delete
```json
codestar-notifications:deleteNotificationRule,
codestar-notifications:describeNotificationRule
```

