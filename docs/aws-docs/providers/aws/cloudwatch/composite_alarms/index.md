---
title: composite_alarms
hide_title: false
hide_table_of_contents: false
keywords:
  - composite_alarms
  - cloudwatch
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


Used to retrieve a list of <code>composite_alarms</code> in a region or to create or delete a <code>composite_alarms</code> resource, use <code>composite_alarm</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>composite_alarms</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::CloudWatch::CompositeAlarm type specifies an alarm which aggregates the states of other Alarms (Metric or Composite Alarms) as defined by the AlarmRule expression</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cloudwatch.composite_alarms" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="alarm_name" /></td><td><code>string</code></td><td>The name of the Composite Alarm</td></tr>
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
alarm_name
FROM aws.cloudwatch.composite_alarms
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>composite_alarm</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
-- composite_alarm.iql (required properties only)
INSERT INTO aws.cloudwatch.composite_alarms (
 AlarmRule,
 region
)
SELECT 
'{{ AlarmRule }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- composite_alarm.iql (all properties)
INSERT INTO aws.cloudwatch.composite_alarms (
 AlarmName,
 AlarmRule,
 AlarmDescription,
 ActionsEnabled,
 OKActions,
 AlarmActions,
 InsufficientDataActions,
 ActionsSuppressor,
 ActionsSuppressorWaitPeriod,
 ActionsSuppressorExtensionPeriod,
 Tags,
 region
)
SELECT 
 '{{ AlarmName }}',
 '{{ AlarmRule }}',
 '{{ AlarmDescription }}',
 '{{ ActionsEnabled }}',
 '{{ OKActions }}',
 '{{ AlarmActions }}',
 '{{ InsufficientDataActions }}',
 '{{ ActionsSuppressor }}',
 '{{ ActionsSuppressorWaitPeriod }}',
 '{{ ActionsSuppressorExtensionPeriod }}',
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
  - name: composite_alarm
    props:
      - name: AlarmName
        value: '{{ AlarmName }}'
      - name: AlarmRule
        value: '{{ AlarmRule }}'
      - name: AlarmDescription
        value: '{{ AlarmDescription }}'
      - name: ActionsEnabled
        value: '{{ ActionsEnabled }}'
      - name: OKActions
        value:
          - '{{ OKActions[0] }}'
      - name: AlarmActions
        value:
          - '{{ AlarmActions[0] }}'
      - name: InsufficientDataActions
        value:
          - '{{ InsufficientDataActions[0] }}'
      - name: ActionsSuppressor
        value: '{{ ActionsSuppressor }}'
      - name: ActionsSuppressorWaitPeriod
        value: '{{ ActionsSuppressorWaitPeriod }}'
      - name: ActionsSuppressorExtensionPeriod
        value: '{{ ActionsSuppressorExtensionPeriod }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.cloudwatch.composite_alarms
WHERE data__Identifier = '<AlarmName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>composite_alarms</code> resource, the following permissions are required:

### Create
```json
cloudwatch:DescribeAlarms,
cloudwatch:PutCompositeAlarm,
cloudwatch:TagResource
```

### Delete
```json
cloudwatch:DescribeAlarms,
cloudwatch:DeleteAlarms
```

### List
```json
cloudwatch:DescribeAlarms
```

