---
title: cloud_watch_alarm_template_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - cloud_watch_alarm_template_tags
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

Expands all tag keys and values for <code>cloud_watch_alarm_templates</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cloud_watch_alarm_template_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::MediaLive::CloudWatchAlarmTemplate Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.medialive.cloud_watch_alarm_template_tags" /></td></tr>
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
<tr><td><CopyableCode code="target_resource_type" /></td><td><code>string</code></td><td>The resource type this template should dynamically generate cloudwatch metric alarms for.</td></tr>
<tr><td><CopyableCode code="threshold" /></td><td><code>number</code></td><td>The threshold value to compare with the specified statistic.</td></tr>
<tr><td><CopyableCode code="treat_missing_data" /></td><td><code>string</code></td><td>Specifies how missing data points are treated when evaluating the alarm's condition.</td></tr>
<tr><td><CopyableCode code="tag_key" /></td><td><code>string</code></td><td>Tag key.</td></tr>
<tr><td><CopyableCode code="tag_value" /></td><td><code>string</code></td><td>Tag value.</td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Expands tags for all <code>cloud_watch_alarm_templates</code> in a region.
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
target_resource_type,
threshold,
treat_missing_data,
tag_key,
tag_value
FROM aws.medialive.cloud_watch_alarm_template_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>cloud_watch_alarm_template_tags</code> resource, see <a href="/providers/aws/medialive/cloud_watch_alarm_templates/#permissions"><code>cloud_watch_alarm_templates</code></a>

