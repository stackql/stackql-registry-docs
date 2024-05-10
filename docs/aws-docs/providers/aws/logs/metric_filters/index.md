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


Used to retrieve a list of <code>metric_filters</code> in a region or to create or delete a <code>metric_filters</code> resource, use <code>metric_filter</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>metric_filters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The ``AWS::Logs::MetricFilter`` resource specifies a metric filter that describes how CWL extracts information from logs and transforms it into Amazon CloudWatch metrics. If you have multiple metric filters that are associated with a log group, all the filters are applied to the log streams in that group.&lt;br&#x2F;&gt; The maximum number of metric filters that can be associated with a log group is 100.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.logs.metric_filters" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
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
log_group_name,
filter_name
FROM aws.logs.metric_filters
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>metric_filter</code> resource, using <a ref="https://pypi.org/project/stack-deploy/" target="_blank"><code><b>stack-deploy</b></code></a>.

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
-- metric_filter.iql (required properties only)
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
-- metric_filter.iql (all properties)
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

## `DELETE` Example

```sql
DELETE FROM aws.logs.metric_filters
WHERE data__Identifier = '<LogGroupName|FilterName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>metric_filters</code> resource, the following permissions are required:

### Create
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

