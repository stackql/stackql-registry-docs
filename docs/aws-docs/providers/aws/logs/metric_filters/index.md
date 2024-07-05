---
title: metric_filters
hide_title: false
hide_table_of_contents: false
keywords:
  - metric_filters
  - logs
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

Creates, updates, deletes or gets a <code>metric_filter</code> resource or lists <code>metric_filters</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>metric_filters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::Logs::MetricFilter</code> resource specifies a metric filter that describes how CWL extracts information from logs and transforms it into Amazon CloudWatch metrics. If you have multiple metric filters that are associated with a log group, all the filters are applied to the log streams in that group.<br />The maximum number of metric filters that can be associated with a log group is 100.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.logs.metric_filters" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="metric_transformations" /></td><td><code>array</code></td><td>The metric transformations.</td></tr>
<tr><td><CopyableCode code="filter_pattern" /></td><td><code>string</code></td><td>A filter pattern for extracting metric data out of ingested log events. For more information, see &#91;Filter and Pattern Syntax&#93;(https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.html).</td></tr>
<tr><td><CopyableCode code="log_group_name" /></td><td><code>string</code></td><td>The name of an existing log group that you want to associate with this metric filter.</td></tr>
<tr><td><CopyableCode code="filter_name" /></td><td><code>string</code></td><td>The name of the metric filter.</td></tr>
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
    <td><CopyableCode code="FilterPattern, LogGroupName, MetricTransformations, region" /></td>
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
Gets all <code>metric_filters</code> in a region.
```sql
SELECT
region,
metric_transformations,
filter_pattern,
log_group_name,
filter_name
FROM aws.logs.metric_filters
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>metric_filter</code>.
```sql
SELECT
region,
metric_transformations,
filter_pattern,
log_group_name,
filter_name
FROM aws.logs.metric_filters
WHERE region = 'us-east-1' AND data__Identifier = '<LogGroupName>|<FilterName>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>metric_filter</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.logs.metric_filters (
 MetricTransformations,
 FilterPattern,
 LogGroupName,
 region
)
SELECT 
'{{ MetricTransformations }}',
 '{{ FilterPattern }}',
 '{{ LogGroupName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.logs.metric_filters (
 MetricTransformations,
 FilterPattern,
 LogGroupName,
 FilterName,
 region
)
SELECT 
 '{{ MetricTransformations }}',
 '{{ FilterPattern }}',
 '{{ LogGroupName }}',
 '{{ FilterName }}',
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
  - name: metric_filter
    props:
      - name: MetricTransformations
        value:
          - DefaultValue: null
            MetricName: '{{ MetricName }}'
            MetricValue: '{{ MetricValue }}'
            MetricNamespace: '{{ MetricNamespace }}'
            Dimensions:
              - Value: '{{ Value }}'
                Key: '{{ Key }}'
            Unit: '{{ Unit }}'
      - name: FilterPattern
        value: '{{ FilterPattern }}'
      - name: LogGroupName
        value: '{{ LogGroupName }}'
      - name: FilterName
        value: '{{ FilterName }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.logs.metric_filters
WHERE data__Identifier = '<LogGroupName|FilterName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>metric_filters</code> resource, the following permissions are required:

### Read
```json
logs:DescribeMetricFilters
```

### Create
```json
logs:PutMetricFilter,
logs:DescribeMetricFilters
```

### Update
```json
logs:PutMetricFilter,
logs:DescribeMetricFilters
```

### List
```json
logs:DescribeMetricFilters
```

### Delete
```json
logs:DeleteMetricFilter
```

