---
title: cloud_watch_alarm_templates
hide_title: false
hide_table_of_contents: false
keywords:
  - cloud_watch_alarm_templates
  - medialive
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

Creates, updates, deletes or gets a <code>cloud_watch_alarm_template</code> resource or lists <code>cloud_watch_alarm_templates</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cloud_watch_alarm_templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::MediaLive::CloudWatchAlarmTemplate Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.medialive.cloud_watch_alarm_templates" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>A cloudwatch alarm template's ARN (Amazon Resource Name)</td></tr>
<tr><td><CopyableCode code="comparison_operator" /></td><td><code>string</code></td><td>The comparison operator used to compare the specified statistic and the threshold.</td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="datapoints_to_alarm" /></td><td><code>number</code></td><td>The number of datapoints within the evaluation period that must be breaching to trigger the alarm.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A resource's optional description.</td></tr>
<tr><td><CopyableCode code="evaluation_periods" /></td><td><code>number</code></td><td>The number of periods over which data is compared to the specified threshold.</td></tr>
<tr><td><CopyableCode code="group_id" /></td><td><code>string</code></td><td>A cloudwatch alarm template group's id. AWS provided template groups have ids that start with `aws-`</td></tr>
<tr><td><CopyableCode code="group_identifier" /></td><td><code>string</code></td><td>A cloudwatch alarm template group's identifier. Can be either be its id or current name.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>A cloudwatch alarm template's id. AWS provided templates have ids that start with `aws-`</td></tr>
<tr><td><CopyableCode code="identifier" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="metric_name" /></td><td><code>string</code></td><td>The name of the metric associated with the alarm. Must be compatible with targetResourceType.</td></tr>
<tr><td><CopyableCode code="modified_at" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>A resource's name. Names must be unique within the scope of a resource type in a specific region.</td></tr>
<tr><td><CopyableCode code="period" /></td><td><code>number</code></td><td>The period, in seconds, over which the specified statistic is applied.</td></tr>
<tr><td><CopyableCode code="statistic" /></td><td><code>string</code></td><td>The statistic to apply to the alarm's metric data.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td>Represents the tags associated with a resource.</td></tr>
<tr><td><CopyableCode code="target_resource_type" /></td><td><code>string</code></td><td>The resource type this template should dynamically generate cloudwatch metric alarms for.</td></tr>
<tr><td><CopyableCode code="threshold" /></td><td><code>number</code></td><td>The threshold value to compare with the specified statistic.</td></tr>
<tr><td><CopyableCode code="treat_missing_data" /></td><td><code>string</code></td><td>Specifies how missing data points are treated when evaluating the alarm's condition.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-cloudwatchalarmtemplate.html"><code>AWS::MediaLive::CloudWatchAlarmTemplate</code></a>.

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
    <td><CopyableCode code="ComparisonOperator, EvaluationPeriods, GroupIdentifier, MetricName, Name, Period, Statistic, TargetResourceType, Threshold, TreatMissingData, region" /></td>
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
Gets all <code>cloud_watch_alarm_templates</code> in a region.
```sql
SELECT
region,
arn,
comparison_operator,
created_at,
datapoints_to_alarm,
description,
evaluation_periods,
group_id,
group_identifier,
id,
identifier,
metric_name,
modified_at,
name,
period,
statistic,
tags,
target_resource_type,
threshold,
treat_missing_data
FROM aws.medialive.cloud_watch_alarm_templates
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>cloud_watch_alarm_template</code>.
```sql
SELECT
region,
arn,
comparison_operator,
created_at,
datapoints_to_alarm,
description,
evaluation_periods,
group_id,
group_identifier,
id,
identifier,
metric_name,
modified_at,
name,
period,
statistic,
tags,
target_resource_type,
threshold,
treat_missing_data
FROM aws.medialive.cloud_watch_alarm_templates
WHERE region = 'us-east-1' AND data__Identifier = '<Identifier>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>cloud_watch_alarm_template</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.medialive.cloud_watch_alarm_templates (
 ComparisonOperator,
 EvaluationPeriods,
 GroupIdentifier,
 MetricName,
 Name,
 Period,
 Statistic,
 TargetResourceType,
 Threshold,
 TreatMissingData,
 region
)
SELECT 
'{{ ComparisonOperator }}',
 '{{ EvaluationPeriods }}',
 '{{ GroupIdentifier }}',
 '{{ MetricName }}',
 '{{ Name }}',
 '{{ Period }}',
 '{{ Statistic }}',
 '{{ TargetResourceType }}',
 '{{ Threshold }}',
 '{{ TreatMissingData }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.medialive.cloud_watch_alarm_templates (
 ComparisonOperator,
 DatapointsToAlarm,
 Description,
 EvaluationPeriods,
 GroupIdentifier,
 MetricName,
 Name,
 Period,
 Statistic,
 Tags,
 TargetResourceType,
 Threshold,
 TreatMissingData,
 region
)
SELECT 
 '{{ ComparisonOperator }}',
 '{{ DatapointsToAlarm }}',
 '{{ Description }}',
 '{{ EvaluationPeriods }}',
 '{{ GroupIdentifier }}',
 '{{ MetricName }}',
 '{{ Name }}',
 '{{ Period }}',
 '{{ Statistic }}',
 '{{ Tags }}',
 '{{ TargetResourceType }}',
 '{{ Threshold }}',
 '{{ TreatMissingData }}',
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
  - name: cloud_watch_alarm_template
    props:
      - name: ComparisonOperator
        value: '{{ ComparisonOperator }}'
      - name: DatapointsToAlarm
        value: null
      - name: Description
        value: '{{ Description }}'
      - name: EvaluationPeriods
        value: null
      - name: GroupIdentifier
        value: '{{ GroupIdentifier }}'
      - name: MetricName
        value: '{{ MetricName }}'
      - name: Name
        value: '{{ Name }}'
      - name: Period
        value: null
      - name: Statistic
        value: '{{ Statistic }}'
      - name: Tags
        value: {}
      - name: TargetResourceType
        value: '{{ TargetResourceType }}'
      - name: Threshold
        value: null
      - name: TreatMissingData
        value: '{{ TreatMissingData }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.medialive.cloud_watch_alarm_templates
WHERE data__Identifier = '<Identifier>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>cloud_watch_alarm_templates</code> resource, the following permissions are required:

### Create
```json
medialive:CreateCloudWatchAlarmTemplate,
medialive:GetCloudWatchAlarmTemplate,
medialive:CreateTags
```

### Read
```json
medialive:GetCloudWatchAlarmTemplate
```

### Update
```json
medialive:UpdateCloudWatchAlarmTemplate,
medialive:GetCloudWatchAlarmTemplate,
medialive:CreateTags,
medialive:DeleteTags
```

### Delete
```json
medialive:DeleteCloudWatchAlarmTemplate
```

### List
```json
medialive:ListCloudWatchAlarmTemplates
```
