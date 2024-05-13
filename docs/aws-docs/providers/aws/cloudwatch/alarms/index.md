---
title: alarms
hide_title: false
hide_table_of_contents: false
keywords:
  - alarms
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


Used to retrieve a list of <code>alarms</code> in a region or to create or delete a <code>alarms</code> resource, use <code>alarm</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>alarms</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::CloudWatch::Alarm</code> type specifies an alarm and associates it with the specified metric or metric math expression.&lt;br&#x2F;&gt; When this operation creates an alarm, the alarm state is immediately set to <code>INSUFFICIENT_DATA</code>. The alarm is then evaluated and its state is set appropriately. Any actions associated with the new state are then executed.&lt;br&#x2F;&gt; When you update an existing alarm, its state is left unchanged, but the update completely overwrites the previous configuration of the alarm.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cloudwatch.alarms" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="alarm_name" /></td><td><code>string</code></td><td>The name of the alarm. If you don't specify a name, CFN generates a unique physical ID and uses that ID for the alarm name. &lt;br&#x2F;&gt;  If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name.</td></tr>
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
    <td><CopyableCode code="ComparisonOperator, EvaluationPeriods, region" /></td>
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
FROM aws.cloudwatch.alarms
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>alarm</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.cloudwatch.alarms (
 ComparisonOperator,
 EvaluationPeriods,
 region
)
SELECT 
'{{ ComparisonOperator }}',
 '{{ EvaluationPeriods }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.cloudwatch.alarms (
 ThresholdMetricId,
 EvaluateLowSampleCountPercentile,
 ExtendedStatistic,
 ComparisonOperator,
 TreatMissingData,
 Dimensions,
 Period,
 EvaluationPeriods,
 Unit,
 Namespace,
 OKActions,
 AlarmActions,
 MetricName,
 ActionsEnabled,
 Metrics,
 AlarmDescription,
 AlarmName,
 Statistic,
 InsufficientDataActions,
 DatapointsToAlarm,
 Threshold,
 Tags,
 region
)
SELECT 
 '{{ ThresholdMetricId }}',
 '{{ EvaluateLowSampleCountPercentile }}',
 '{{ ExtendedStatistic }}',
 '{{ ComparisonOperator }}',
 '{{ TreatMissingData }}',
 '{{ Dimensions }}',
 '{{ Period }}',
 '{{ EvaluationPeriods }}',
 '{{ Unit }}',
 '{{ Namespace }}',
 '{{ OKActions }}',
 '{{ AlarmActions }}',
 '{{ MetricName }}',
 '{{ ActionsEnabled }}',
 '{{ Metrics }}',
 '{{ AlarmDescription }}',
 '{{ AlarmName }}',
 '{{ Statistic }}',
 '{{ InsufficientDataActions }}',
 '{{ DatapointsToAlarm }}',
 '{{ Threshold }}',
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
  - name: alarm
    props:
      - name: ThresholdMetricId
        value: '{{ ThresholdMetricId }}'
      - name: EvaluateLowSampleCountPercentile
        value: '{{ EvaluateLowSampleCountPercentile }}'
      - name: ExtendedStatistic
        value: '{{ ExtendedStatistic }}'
      - name: ComparisonOperator
        value: '{{ ComparisonOperator }}'
      - name: TreatMissingData
        value: '{{ TreatMissingData }}'
      - name: Dimensions
        value:
          - Value: '{{ Value }}'
            Name: '{{ Name }}'
      - name: Period
        value: '{{ Period }}'
      - name: EvaluationPeriods
        value: '{{ EvaluationPeriods }}'
      - name: Unit
        value: '{{ Unit }}'
      - name: Namespace
        value: '{{ Namespace }}'
      - name: OKActions
        value:
          - '{{ OKActions[0] }}'
      - name: AlarmActions
        value:
          - '{{ AlarmActions[0] }}'
      - name: MetricName
        value: '{{ MetricName }}'
      - name: ActionsEnabled
        value: '{{ ActionsEnabled }}'
      - name: Metrics
        value:
          - Label: '{{ Label }}'
            MetricStat:
              Period: '{{ Period }}'
              Metric:
                MetricName: '{{ MetricName }}'
                Dimensions:
                  - null
                Namespace: '{{ Namespace }}'
              Stat: '{{ Stat }}'
              Unit: '{{ Unit }}'
            Id: '{{ Id }}'
            ReturnData: '{{ ReturnData }}'
            Expression: '{{ Expression }}'
            Period: '{{ Period }}'
            AccountId: '{{ AccountId }}'
      - name: AlarmDescription
        value: '{{ AlarmDescription }}'
      - name: AlarmName
        value: '{{ AlarmName }}'
      - name: Statistic
        value: '{{ Statistic }}'
      - name: InsufficientDataActions
        value:
          - '{{ InsufficientDataActions[0] }}'
      - name: DatapointsToAlarm
        value: '{{ DatapointsToAlarm }}'
      - name: Threshold
        value: null
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
/*+ delete */
DELETE FROM aws.cloudwatch.alarms
WHERE data__Identifier = '<AlarmName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>alarms</code> resource, the following permissions are required:

### Create
```json
cloudwatch:PutMetricAlarm,
cloudwatch:DescribeAlarms,
cloudwatch:TagResource
```

### Delete
```json
cloudwatch:DeleteAlarms,
cloudwatch:DescribeAlarms
```

### List
```json
cloudwatch:DescribeAlarms
```

