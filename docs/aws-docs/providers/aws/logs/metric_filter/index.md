---
title: metric_filter
hide_title: false
hide_table_of_contents: false
keywords:
  - metric_filter
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


Gets or updates an individual <code>metric_filter</code> resource, use <code>metric_filters</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>metric_filter</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::Logs::MetricFilter</code> resource specifies a metric filter that describes how CWL extracts information from logs and transforms it into Amazon CloudWatch metrics. If you have multiple metric filters that are associated with a log group, all the filters are applied to the log streams in that group.&lt;br&#x2F;&gt; The maximum number of metric filters that can be associated with a log group is 100.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.logs.metric_filter" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="metric_transformations" /></td><td><code>array</code></td><td>The metric transformations.</td></tr>
<tr><td><CopyableCode code="filter_pattern" /></td><td><code>string</code></td><td>A filter pattern for extracting metric data out of ingested log events. For more information, see &#91;Filter and Pattern Syntax&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonCloudWatch&#x2F;latest&#x2F;logs&#x2F;FilterAndPatternSyntax.html).</td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
metric_transformations,
filter_pattern,
log_group_name,
filter_name
FROM aws.logs.metric_filter
WHERE region = 'us-east-1' AND data__Identifier = '<LogGroupName>|<FilterName>';
```


## Permissions

To operate on the <code>metric_filter</code> resource, the following permissions are required:

### Read
```json
logs:DescribeMetricFilters
```

### Update
```json
logs:PutMetricFilter,
logs:DescribeMetricFilters
```

