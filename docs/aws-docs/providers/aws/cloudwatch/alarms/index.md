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

Creates, updates, deletes or gets an <code>alarm</code> resource or lists <code>alarms</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>alarms</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::CloudWatch::Alarm</code> type specifies an alarm and associates it with the specified metric or metric math expression.<br />When this operation creates an alarm, the alarm state is immediately set to <code>INSUFFICIENT_DATA</code>. The alarm is then evaluated and its state is set appropriately. Any actions associated with the new state are then executed.<br />When you update an existing alarm, its state is left unchanged, but the update completely overwrites the previous configuration of the alarm.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cloudwatch.alarms" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="threshold_metric_id" /></td><td><code>string</code></td><td>In an alarm based on an anomaly detection model, this is the ID of the <code>ANOMALY_DETECTION_BAND</code> function used as the threshold for the alarm.</td></tr>
<tr><td><CopyableCode code="evaluate_low_sample_count_percentile" /></td><td><code>string</code></td><td>Used only for alarms based on percentiles. If <code>ignore</code>, the alarm state does not change during periods with too few data points to be statistically significant. If <code>evaluate</code> or this parameter is not used, the alarm is always evaluated and possibly changes state no matter how many data points are available.</td></tr>
<tr><td><CopyableCode code="extended_statistic" /></td><td><code>string</code></td><td>The percentile statistic for the metric associated with the alarm. Specify a value between p0.0 and p100.<br />For an alarm based on a metric, you must specify either <code>Statistic</code> or <code>ExtendedStatistic</code> but not both.<br />For an alarm based on a math expression, you can't specify <code>ExtendedStatistic</code>. Instead, you use <code>Metrics</code>.</td></tr>
<tr><td><CopyableCode code="comparison_operator" /></td><td><code>string</code></td><td>The arithmetic operation to use when comparing the specified statistic and threshold. The specified statistic value is used as the first operand.</td></tr>
<tr><td><CopyableCode code="treat_missing_data" /></td><td><code>string</code></td><td>Sets how this alarm is to handle missing data points. Valid values are <code>breaching</code>, <code>notBreaching</code>, <code>ignore</code>, and <code>missing</code>. For more information, see &#91;Configuring How Alarms Treat Missing Data&#93;(https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html#alarms-and-missing-data) in the *Amazon User Guide*.<br />If you omit this parameter, the default behavior of <code>missing</code> is used.</td></tr>
<tr><td><CopyableCode code="dimensions" /></td><td><code>array</code></td><td>The dimensions for the metric associated with the alarm. For an alarm based on a math expression, you can't specify <code>Dimensions</code>. Instead, you use <code>Metrics</code>.</td></tr>
<tr><td><CopyableCode code="period" /></td><td><code>integer</code></td><td>The period, in seconds, over which the statistic is applied. This is required for an alarm based on a metric. Valid values are 10, 30, 60, and any multiple of 60.<br />For an alarm based on a math expression, you can't specify <code>Period</code>, and instead you use the <code>Metrics</code> parameter.<br />*Minimum:* 10</td></tr>
<tr><td><CopyableCode code="evaluation_periods" /></td><td><code>integer</code></td><td>The number of periods over which data is compared to the specified threshold. If you are setting an alarm that requires that a number of consecutive data points be breaching to trigger the alarm, this value specifies that number. If you are setting an "M out of N" alarm, this value is the N, and <code>DatapointsToAlarm</code> is the M.<br />For more information, see &#91;Evaluating an Alarm&#93;(https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html#alarm-evaluation) in the *User Guide*.</td></tr>
<tr><td><CopyableCode code="unit" /></td><td><code>string</code></td><td>The unit of the metric associated with the alarm. Specify this only if you are creating an alarm based on a single metric. Do not specify this if you are specifying a <code>Metrics</code> array.<br />You can specify the following values: Seconds, Microseconds, Milliseconds, Bytes, Kilobytes, Megabytes, Gigabytes, Terabytes, Bits, Kilobits, Megabits, Gigabits, Terabits, Percent, Count, Bytes/Second, Kilobytes/Second, Megabytes/Second, Gigabytes/Second, Terabytes/Second, Bits/Second, Kilobits/Second, Megabits/Second, Gigabits/Second, Terabits/Second, Count/Second, or None.</td></tr>
<tr><td><CopyableCode code="namespace" /></td><td><code>string</code></td><td>The namespace of the metric associated with the alarm. This is required for an alarm based on a metric. For an alarm based on a math expression, you can't specify <code>Namespace</code> and you use <code>Metrics</code> instead.<br />For a list of namespaces for metrics from AWS services, see &#91;Services That Publish Metrics.&#93;(https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/aws-services-cloudwatch-metrics.html)</td></tr>
<tr><td><CopyableCode code="ok_actions" /></td><td><code>array</code></td><td>The actions to execute when this alarm transitions to the <code>OK</code> state from any other state. Each action is specified as an Amazon Resource Name (ARN).</td></tr>
<tr><td><CopyableCode code="alarm_actions" /></td><td><code>array</code></td><td>The list of actions to execute when this alarm transitions into an ALARM state from any other state. Specify each action as an Amazon Resource Name (ARN). For more information about creating alarms and the actions that you can specify, see &#91;PutMetricAlarm&#93;(https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutMetricAlarm.html) in the *API Reference*.</td></tr>
<tr><td><CopyableCode code="metric_name" /></td><td><code>string</code></td><td>The name of the metric associated with the alarm. This is required for an alarm based on a metric. For an alarm based on a math expression, you use <code>Metrics</code> instead and you can't specify <code>MetricName</code>.</td></tr>
<tr><td><CopyableCode code="actions_enabled" /></td><td><code>boolean</code></td><td>Indicates whether actions should be executed during any changes to the alarm state. The default is TRUE.</td></tr>
<tr><td><CopyableCode code="metrics" /></td><td><code>array</code></td><td>An array that enables you to create an alarm based on the result of a metric math expression. Each item in the array either retrieves a metric or performs a math expression.<br />If you specify the <code>Metrics</code> parameter, you cannot specify <code>MetricName</code>, <code>Dimensions</code>, <code>Period</code>, <code>Namespace</code>, <code>Statistic</code>, <code>ExtendedStatistic</code>, or <code>Unit</code>.</td></tr>
<tr><td><CopyableCode code="alarm_description" /></td><td><code>string</code></td><td>The description of the alarm.</td></tr>
<tr><td><CopyableCode code="alarm_name" /></td><td><code>string</code></td><td>The name of the alarm. If you don't specify a name, CFN generates a unique physical ID and uses that ID for the alarm name. <br />If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name.</td></tr>
<tr><td><CopyableCode code="statistic" /></td><td><code>string</code></td><td>The statistic for the metric associated with the alarm, other than percentile. For percentile statistics, use <code>ExtendedStatistic</code>.<br />For an alarm based on a metric, you must specify either <code>Statistic</code> or <code>ExtendedStatistic</code> but not both.<br />For an alarm based on a math expression, you can't specify <code>Statistic</code>. Instead, you use <code>Metrics</code>.</td></tr>
<tr><td><CopyableCode code="insufficient_data_actions" /></td><td><code>array</code></td><td>The actions to execute when this alarm transitions to the <code>INSUFFICIENT_DATA</code> state from any other state. Each action is specified as an Amazon Resource Name (ARN).</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="datapoints_to_alarm" /></td><td><code>integer</code></td><td>The number of datapoints that must be breaching to trigger the alarm. This is used only if you are setting an "M out of N" alarm. In that case, this value is the M, and the value that you set for <code>EvaluationPeriods</code> is the N value. For more information, see &#91;Evaluating an Alarm&#93;(https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html#alarm-evaluation) in the *User Guide*.<br />If you omit this parameter, CW uses the same value here that you set for <code>EvaluationPeriods</code>, and the alarm goes to alarm state if that many consecutive periods are breaching.</td></tr>
<tr><td><CopyableCode code="threshold" /></td><td><code>number</code></td><td>The value to compare with the specified statistic.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A list of key-value pairs to associate with the alarm. You can associate as many as 50 tags with an alarm. To be able to associate tags with the alarm when you create the alarm, you must have the <code>cloudwatch:TagResource</code> permission.<br />Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-alarm.html"><code>AWS::CloudWatch::Alarm</code></a>.

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
Gets all <code>alarms</code> in a region.
```sql
SELECT
region,
threshold_metric_id,
evaluate_low_sample_count_percentile,
extended_statistic,
comparison_operator,
treat_missing_data,
dimensions,
period,
evaluation_periods,
unit,
namespace,
ok_actions,
alarm_actions,
metric_name,
actions_enabled,
metrics,
alarm_description,
alarm_name,
statistic,
insufficient_data_actions,
arn,
datapoints_to_alarm,
threshold,
tags
FROM aws.cloudwatch.alarms
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>alarm</code>.
```sql
SELECT
region,
threshold_metric_id,
evaluate_low_sample_count_percentile,
extended_statistic,
comparison_operator,
treat_missing_data,
dimensions,
period,
evaluation_periods,
unit,
namespace,
ok_actions,
alarm_actions,
metric_name,
actions_enabled,
metrics,
alarm_description,
alarm_name,
statistic,
insufficient_data_actions,
arn,
datapoints_to_alarm,
threshold,
tags
FROM aws.cloudwatch.alarms
WHERE region = 'us-east-1' AND data__Identifier = '<AlarmName>';
```

## `INSERT` example

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

## `DELETE` example

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

### Update
```json
cloudwatch:PutMetricAlarm,
cloudwatch:DescribeAlarms,
cloudwatch:TagResource,
cloudwatch:UntagResource
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

### Read
```json
cloudwatch:DescribeAlarms,
cloudwatch:ListTagsForResource
```
