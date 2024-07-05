---
title: metric_streams_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - metric_streams_list_only
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

Lists <code>metric_streams</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/metric_streams/"><code>metric_streams</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>metric_streams_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for Metric Stream</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cloudwatch.metric_streams_list_only" /></td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Lists all <code>metric_streams</code> in a region.
```sql
SELECT
region,
name
FROM aws.cloudwatch.metric_streams_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>metric_streams_list_only</code> resource, see <a href="/providers/aws/cloudwatch/metric_streams/#permissions"><code>metric_streams</code></a>


