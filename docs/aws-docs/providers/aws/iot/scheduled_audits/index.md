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


Used to retrieve a list of <code>scheduled_audits</code> in a region or to create or delete a <code>scheduled_audits</code> resource, use <code>scheduled_audit</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>scheduled_audits</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Scheduled audits can be used to specify the checks you want to perform during an audit and how often the audit should be run.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iot.scheduled_audits" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="scheduled_audit_name" /></td><td><code>string</code></td><td>The name you want to give to the scheduled audit.</td></tr>
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
scheduled_audit_name
FROM aws.iot.scheduled_audits
WHERE region = 'us-east-1';
```

## `INSERT` Example

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
-- scheduled_audit.iql (required properties only)
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
-- scheduled_audit.iql (all properties)
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

## `DELETE` Example

```sql
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

### Delete
```json
iot:DescribeScheduledAudit,
iot:DeleteScheduledAudit
```

### List
```json
iot:ListScheduledAudits
```

