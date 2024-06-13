---
title: rotations
hide_title: false
hide_table_of_contents: false
keywords:
  - rotations
  - ssmcontacts
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

Creates, updates, deletes or gets a <code>rotation</code> resource or lists <code>rotations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>rotations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SSMContacts::Rotation.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ssmcontacts.rotations" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Name of the Rotation</td></tr>
<tr><td><CopyableCode code="contact_ids" /></td><td><code>array</code></td><td>Members of the rotation</td></tr>
<tr><td><CopyableCode code="start_time" /></td><td><code>string</code></td><td>Start time of the first shift of Oncall Schedule</td></tr>
<tr><td><CopyableCode code="time_zone_id" /></td><td><code>string</code></td><td>TimeZone Identifier for the Oncall Schedule</td></tr>
<tr><td><CopyableCode code="recurrence" /></td><td><code>object</code></td><td>Information about when an on-call rotation is in effect and how long the rotation period lasts.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the rotation.</td></tr>
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
    <td><CopyableCode code="Name, ContactIds, StartTime, TimeZoneId, Recurrence, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
List all <code>rotations</code> in a region.
```sql
SELECT
region,
arn
FROM aws.ssmcontacts.rotations
WHERE region = 'us-east-1';
```
Gets all properties from a <code>rotation</code>.
```sql
SELECT
region,
name,
contact_ids,
start_time,
time_zone_id,
recurrence,
tags,
arn
FROM aws.ssmcontacts.rotations
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>rotation</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
/*+ create */
INSERT INTO aws.ssmcontacts.rotations (
 Name,
 ContactIds,
 StartTime,
 TimeZoneId,
 Recurrence,
 region
)
SELECT 
'{{ Name }}',
 '{{ ContactIds }}',
 '{{ StartTime }}',
 '{{ TimeZoneId }}',
 '{{ Recurrence }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.ssmcontacts.rotations (
 Name,
 ContactIds,
 StartTime,
 TimeZoneId,
 Recurrence,
 Tags,
 region
)
SELECT 
 '{{ Name }}',
 '{{ ContactIds }}',
 '{{ StartTime }}',
 '{{ TimeZoneId }}',
 '{{ Recurrence }}',
 '{{ Tags }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: rotation
    props:
      - name: Name
        value: '{{ Name }}'
      - name: ContactIds
        value:
          - '{{ ContactIds[0] }}'
      - name: StartTime
        value: '{{ StartTime }}'
      - name: TimeZoneId
        value: '{{ TimeZoneId }}'
      - name: Recurrence
        value:
          MonthlySettings:
            - DayOfMonth: '{{ DayOfMonth }}'
              HandOffTime: '{{ HandOffTime }}'
          WeeklySettings:
            - DayOfWeek: '{{ DayOfWeek }}'
              HandOffTime: null
          DailySettings:
            - null
          NumberOfOnCalls: '{{ NumberOfOnCalls }}'
          RecurrenceMultiplier: '{{ RecurrenceMultiplier }}'
          ShiftCoverages:
            - DayOfWeek: null
              CoverageTimes:
                - StartTime: null
                  EndTime: null
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.ssmcontacts.rotations
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>rotations</code> resource, the following permissions are required:

### Create
```json
ssm-contacts:CreateRotation,
ssm-contacts:GetRotation,
ssm-contacts:TagResource,
ssm-contacts:ListTagsForResource,
ssm-contacts:UntagResource
```

### Read
```json
ssm-contacts:GetRotation,
ssm-contacts:TagResource,
ssm-contacts:ListTagsForResource,
ssm-contacts:UntagResource
```

### Update
```json
ssm-contacts:UpdateRotation,
ssm-contacts:GetRotation,
ssm-contacts:TagResource,
ssm-contacts:ListTagsForResource,
ssm-contacts:UntagResource
```

### Delete
```json
ssm-contacts:DeleteRotation,
ssm-contacts:GetRotation,
ssm-contacts:ListTagsForResource,
ssm-contacts:UntagResource
```

### List
```json
ssm-contacts:ListRotations,
ssm-contacts:GetRotation,
ssm-contacts:ListTagsForResource
```

