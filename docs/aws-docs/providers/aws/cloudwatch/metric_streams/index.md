---
title: metric_streams
hide_title: false
hide_table_of_contents: false
keywords:
  - metric_streams
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

Creates, updates, deletes or gets a <code>metric_stream</code> resource or lists <code>metric_streams</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>metric_streams</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for Metric Stream</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cloudwatch.metric_streams" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Amazon Resource Name of the metric stream.</td></tr>
<tr><td><CopyableCode code="creation_date" /></td><td><code>string</code></td><td>The date of creation of the metric stream.</td></tr>
<tr><td><CopyableCode code="exclude_filters" /></td><td><code>array</code></td><td>Define which metrics will be not streamed. Metrics matched by multiple instances of MetricStreamFilter are joined with an OR operation by default. If both IncludeFilters and ExcludeFilters are omitted, all metrics in the account will be streamed. IncludeFilters and ExcludeFilters are mutually exclusive. Default to null.</td></tr>
<tr><td><CopyableCode code="firehose_arn" /></td><td><code>string</code></td><td>The ARN of the Kinesis Firehose where to stream the data.</td></tr>
<tr><td><CopyableCode code="include_filters" /></td><td><code>array</code></td><td>Define which metrics will be streamed. Metrics matched by multiple instances of MetricStreamFilter are joined with an OR operation by default. If both IncludeFilters and ExcludeFilters are omitted, all metrics in the account will be streamed. IncludeFilters and ExcludeFilters are mutually exclusive. Default to null.</td></tr>
<tr><td><CopyableCode code="last_update_date" /></td><td><code>string</code></td><td>The date of the last update of the metric stream.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Name of the metric stream.</td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td>The ARN of the role that provides access to the Kinesis Firehose.</td></tr>
<tr><td><CopyableCode code="state" /></td><td><code>string</code></td><td>Displays the state of the Metric Stream.</td></tr>
<tr><td><CopyableCode code="output_format" /></td><td><code>string</code></td><td>The output format of the data streamed to the Kinesis Firehose.</td></tr>
<tr><td><CopyableCode code="statistics_configurations" /></td><td><code>array</code></td><td>By default, a metric stream always sends the MAX, MIN, SUM, and SAMPLECOUNT statistics for each metric that is streamed. You can use this parameter to have the metric stream also send additional statistics in the stream. This array can have up to 100 members.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A set of tags to assign to the delivery stream.</td></tr>
<tr><td><CopyableCode code="include_linked_accounts_metrics" /></td><td><code>boolean</code></td><td>If you are creating a metric stream in a monitoring account, specify true to include metrics from source accounts that are linked to this monitoring account, in the metric stream. The default is false.</td></tr>
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
    <td><CopyableCode code="FirehoseArn, RoleArn, OutputFormat, region" /></td>
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
Gets all <code>metric_streams</code> in a region.
```sql
SELECT
region,
arn,
creation_date,
exclude_filters,
firehose_arn,
include_filters,
last_update_date,
name,
role_arn,
state,
output_format,
statistics_configurations,
tags,
include_linked_accounts_metrics
FROM aws.cloudwatch.metric_streams
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>metric_stream</code>.
```sql
SELECT
region,
arn,
creation_date,
exclude_filters,
firehose_arn,
include_filters,
last_update_date,
name,
role_arn,
state,
output_format,
statistics_configurations,
tags,
include_linked_accounts_metrics
FROM aws.cloudwatch.metric_streams
WHERE region = 'us-east-1' AND data__Identifier = '<Name>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>metric_stream</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.cloudwatch.metric_streams (
 FirehoseArn,
 RoleArn,
 OutputFormat,
 region
)
SELECT 
'{{ FirehoseArn }}',
 '{{ RoleArn }}',
 '{{ OutputFormat }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.cloudwatch.metric_streams (
 ExcludeFilters,
 FirehoseArn,
 IncludeFilters,
 Name,
 RoleArn,
 OutputFormat,
 StatisticsConfigurations,
 Tags,
 IncludeLinkedAccountsMetrics,
 region
)
SELECT 
 '{{ ExcludeFilters }}',
 '{{ FirehoseArn }}',
 '{{ IncludeFilters }}',
 '{{ Name }}',
 '{{ RoleArn }}',
 '{{ OutputFormat }}',
 '{{ StatisticsConfigurations }}',
 '{{ Tags }}',
 '{{ IncludeLinkedAccountsMetrics }}',
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
  - name: metric_stream
    props:
      - name: ExcludeFilters
        value:
          - Namespace: '{{ Namespace }}'
            MetricNames:
              - '{{ MetricNames[0] }}'
      - name: FirehoseArn
        value: '{{ FirehoseArn }}'
      - name: IncludeFilters
        value:
          - null
      - name: Name
        value: '{{ Name }}'
      - name: RoleArn
        value: '{{ RoleArn }}'
      - name: OutputFormat
        value: '{{ OutputFormat }}'
      - name: StatisticsConfigurations
        value:
          - AdditionalStatistics:
              - '{{ AdditionalStatistics[0] }}'
            IncludeMetrics:
              - MetricName: '{{ MetricName }}'
                Namespace: '{{ Namespace }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: IncludeLinkedAccountsMetrics
        value: '{{ IncludeLinkedAccountsMetrics }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.cloudwatch.metric_streams
WHERE data__Identifier = '<Name>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>metric_streams</code> resource, the following permissions are required:

### Create
```json
cloudwatch:PutMetricStream,
cloudwatch:GetMetricStream,
cloudwatch:TagResource,
iam:PassRole
```

### Update
```json
cloudwatch:PutMetricStream,
cloudwatch:GetMetricStream,
cloudwatch:TagResource,
cloudwatch:UntagResource,
iam:PassRole
```

### Delete
```json
cloudwatch:DeleteMetricStream,
cloudwatch:GetMetricStream
```

### List
```json
cloudwatch:ListMetricStreams
```

### Read
```json
cloudwatch:GetMetricStream
```

