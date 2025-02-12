---
title: schedules
hide_title: false
hide_table_of_contents: false
keywords:
  - schedules
  - databrew
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

Creates, updates, deletes or gets a <code>schedule</code> resource or lists <code>schedules</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>schedules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::DataBrew::Schedule.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.databrew.schedules" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="job_names" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="cron_expression" /></td><td><code>string</code></td><td>Schedule cron</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Schedule Name</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-schedule.html"><code>AWS::DataBrew::Schedule</code></a>.

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
    <td><CopyableCode code="Name, CronExpression, region" /></td>
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
    <td><CopyableCode code="list_resources" /></td>
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
Gets all <code>schedules</code> in a region.
```sql
SELECT
region,
job_names,
cron_expression,
name,
tags
FROM aws.databrew.schedules
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>schedule</code>.
```sql
SELECT
region,
job_names,
cron_expression,
name,
tags
FROM aws.databrew.schedules
WHERE region = 'us-east-1' AND data__Identifier = '<Name>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>schedule</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.databrew.schedules (
 CronExpression,
 Name,
 region
)
SELECT 
'{{ CronExpression }}',
 '{{ Name }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.databrew.schedules (
 JobNames,
 CronExpression,
 Name,
 Tags,
 region
)
SELECT 
 '{{ JobNames }}',
 '{{ CronExpression }}',
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
  - name: schedule
    props:
      - name: JobNames
        value:
          - '{{ JobNames[0] }}'
      - name: CronExpression
        value: '{{ CronExpression }}'
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
DELETE FROM aws.databrew.schedules
WHERE data__Identifier = '<Name>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>schedules</code> resource, the following permissions are required:

### Create
```json
databrew:CreateSchedule,
databrew:TagResource,
databrew:UntagResource,
iam:PassRole
```

### Read
```json
databrew:DescribeSchedule,
databrew:ListTagsForResource,
iam:ListRoles
```

### Update
```json
databrew:UpdateSchedule
```

### Delete
```json
databrew:DeleteSchedule
```

### List
```json
databrew:ListSchedules,
databrew:ListTagsForResource,
iam:ListRoles
```
