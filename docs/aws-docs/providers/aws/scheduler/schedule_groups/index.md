---
title: schedule_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - schedule_groups
  - scheduler
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

Creates, updates, deletes or gets a <code>schedule_group</code> resource or lists <code>schedule_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>schedule_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Scheduler::ScheduleGroup Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.scheduler.schedule_groups" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the schedule group.</td></tr>
<tr><td><CopyableCode code="creation_date" /></td><td><code>string</code></td><td>The time at which the schedule group was created.</td></tr>
<tr><td><CopyableCode code="last_modification_date" /></td><td><code>string</code></td><td>The time at which the schedule group was last modified.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="state" /></td><td><code>string</code></td><td>Specifies the state of the schedule group.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The list of tags to associate with the schedule group.</td></tr>
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
    <td><CopyableCode code="region" /></td>
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
List all <code>schedule_groups</code> in a region.
```sql
SELECT
region,
name
FROM aws.scheduler.schedule_groups
WHERE region = 'us-east-1';
```
Gets all properties from a <code>schedule_group</code>.
```sql
SELECT
region,
arn,
creation_date,
last_modification_date,
name,
state,
tags
FROM aws.scheduler.schedule_groups
WHERE region = 'us-east-1' AND data__Identifier = '<Name>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>schedule_group</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.scheduler.schedule_groups (
 Name,
 Tags,
 region
)
SELECT 
'{{ Name }}',
 '{{ Tags }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.scheduler.schedule_groups (
 Name,
 Tags,
 region
)
SELECT 
 '{{ Name }}',
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
  - name: schedule_group
    props:
      - name: Name
        value: '{{ Name }}'
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
DELETE FROM aws.scheduler.schedule_groups
WHERE data__Identifier = '<Name>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>schedule_groups</code> resource, the following permissions are required:

### Create
```json
scheduler:TagResource,
scheduler:CreateScheduleGroup,
scheduler:GetScheduleGroup,
scheduler:ListTagsForResource
```

### Read
```json
scheduler:GetScheduleGroup,
scheduler:ListTagsForResource
```

### Update
```json
scheduler:TagResource,
scheduler:UntagResource,
scheduler:ListTagsForResource,
scheduler:GetScheduleGroup
```

### Delete
```json
scheduler:DeleteScheduleGroup,
scheduler:GetScheduleGroup,
scheduler:DeleteSchedule
```

### List
```json
scheduler:ListScheduleGroups
```

