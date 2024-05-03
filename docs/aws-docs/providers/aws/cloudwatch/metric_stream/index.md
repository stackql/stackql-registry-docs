---
title: metric_stream
hide_title: false
hide_table_of_contents: false
keywords:
  - metric_stream
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

Gets or operates on an individual <code>metric_stream</code> resource, use <code>metric_streams</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>metric_stream</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for Metric Stream</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cloudwatch.metric_stream" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Amazon Resource Name of the metric stream.</td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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
FROM aws.cloudwatch.metric_stream
WHERE data__Identifier = '<Name>';
```

## Permissions

To operate on the <code>metric_stream</code> resource, the following permissions are required:

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

### Read
```json
cloudwatch:GetMetricStream
```

