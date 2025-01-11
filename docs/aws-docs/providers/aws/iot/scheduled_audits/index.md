---
title: scheduled_audits
hide_title: false
hide_table_of_contents: false
keywords:
  - scheduled_audits
  - iot
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

Creates, updates, deletes or gets a <code>scheduled_audit</code> resource or lists <code>scheduled_audits</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>scheduled_audits</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Scheduled audits can be used to specify the checks you want to perform during an audit and how often the audit should be run.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iot.scheduled_audits" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="scheduled_audit_name" /></td><td><code>string</code></td><td>The name you want to give to the scheduled audit.</td></tr>
<tr><td><CopyableCode code="frequency" /></td><td><code>string</code></td><td>How often the scheduled audit takes place. Can be one of DAILY, WEEKLY, BIWEEKLY, or MONTHLY.</td></tr>
<tr><td><CopyableCode code="day_of_month" /></td><td><code>string</code></td><td>The day of the month on which the scheduled audit takes place. Can be 1 through 31 or LAST. This field is required if the frequency parameter is set to MONTHLY.</td></tr>
<tr><td><CopyableCode code="day_of_week" /></td><td><code>string</code></td><td>The day of the week on which the scheduled audit takes place. Can be one of SUN, MON, TUE,WED, THU, FRI, or SAT. This field is required if the frequency parameter is set to WEEKLY or BIWEEKLY.</td></tr>
<tr><td><CopyableCode code="target_check_names" /></td><td><code>array</code></td><td>Which checks are performed during the scheduled audit. Checks must be enabled for your account.</td></tr>
<tr><td><CopyableCode code="scheduled_audit_arn" /></td><td><code>string</code></td><td>The ARN (Amazon resource name) of the scheduled audit.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-scheduledaudit.html"><code>AWS::IoT::ScheduledAudit</code></a>.

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
    <td><CopyableCode code="Frequency, TargetCheckNames, region" /></td>
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
Gets all <code>scheduled_audits</code> in a region.
```sql
SELECT
region,
scheduled_audit_name,
frequency,
day_of_month,
day_of_week,
target_check_names,
scheduled_audit_arn,
tags
FROM aws.iot.scheduled_audits
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>scheduled_audit</code>.
```sql
SELECT
region,
scheduled_audit_name,
frequency,
day_of_month,
day_of_week,
target_check_names,
scheduled_audit_arn,
tags
FROM aws.iot.scheduled_audits
WHERE region = 'us-east-1' AND data__Identifier = '<ScheduledAuditName>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>scheduled_audit</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.iot.scheduled_audits (
 Frequency,
 TargetCheckNames,
 region
)
SELECT 
'{{ Frequency }}',
 '{{ TargetCheckNames }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.iot.scheduled_audits (
 ScheduledAuditName,
 Frequency,
 DayOfMonth,
 DayOfWeek,
 TargetCheckNames,
 Tags,
 region
)
SELECT 
 '{{ ScheduledAuditName }}',
 '{{ Frequency }}',
 '{{ DayOfMonth }}',
 '{{ DayOfWeek }}',
 '{{ TargetCheckNames }}',
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
  - name: scheduled_audit
    props:
      - name: ScheduledAuditName
        value: '{{ ScheduledAuditName }}'
      - name: Frequency
        value: '{{ Frequency }}'
      - name: DayOfMonth
        value: '{{ DayOfMonth }}'
      - name: DayOfWeek
        value: '{{ DayOfWeek }}'
      - name: TargetCheckNames
        value:
          - '{{ TargetCheckNames[0] }}'
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
DELETE FROM aws.iot.scheduled_audits
WHERE data__Identifier = '<ScheduledAuditName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>scheduled_audits</code> resource, the following permissions are required:

### Create
```json
iot:CreateScheduledAudit,
iot:DescribeScheduledAudit,
iot:TagResource
```

### Read
```json
iot:DescribeScheduledAudit,
iot:ListTagsForResource
```

### Update
```json
iot:UpdateScheduledAudit,
iot:ListTagsForResource,
iot:UntagResource,
iot:TagResource
```

### Delete
```json
iot:DescribeScheduledAudit,
iot:DeleteScheduledAudit
```

### List
```json
iot:ListScheduledAudits
```
