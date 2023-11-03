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
Gets an individual <code>metric_stream</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>metric_stream</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.cloudwatch.metric_stream</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td>Amazon Resource Name of the metric stream.</td></tr><tr><td><code>CreationDate</code></td><td><code>string</code></td><td>The date of creation of the metric stream.</td></tr><tr><td><code>ExcludeFilters</code></td><td><code>array</code></td><td>Define which metrics will be not streamed. Metrics matched by multiple instances of MetricStreamFilter are joined with an OR operation by default. If both IncludeFilters and ExcludeFilters are omitted, all metrics in the account will be streamed. IncludeFilters and ExcludeFilters are mutually exclusive. Default to null.</td></tr><tr><td><code>FirehoseArn</code></td><td><code>string</code></td><td>The ARN of the Kinesis Firehose where to stream the data.</td></tr><tr><td><code>IncludeFilters</code></td><td><code>array</code></td><td>Define which metrics will be streamed. Metrics matched by multiple instances of MetricStreamFilter are joined with an OR operation by default. If both IncludeFilters and ExcludeFilters are omitted, all metrics in the account will be streamed. IncludeFilters and ExcludeFilters are mutually exclusive. Default to null.</td></tr><tr><td><code>LastUpdateDate</code></td><td><code>string</code></td><td>The date of the last update of the metric stream.</td></tr><tr><td><code>Name</code></td><td><code>string</code></td><td>Name of the metric stream.</td></tr><tr><td><code>RoleArn</code></td><td><code>string</code></td><td>The ARN of the role that provides access to the Kinesis Firehose.</td></tr><tr><td><code>State</code></td><td><code>string</code></td><td>Displays the state of the Metric Stream.</td></tr><tr><td><code>OutputFormat</code></td><td><code>string</code></td><td>The output format of the data streamed to the Kinesis Firehose.</td></tr><tr><td><code>StatisticsConfigurations</code></td><td><code>array</code></td><td>By default, a metric stream always sends the MAX, MIN, SUM, and SAMPLECOUNT statistics for each metric that is streamed. You can use this parameter to have the metric stream also send additional statistics in the stream. This array can have up to 100 members.</td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td>A set of tags to assign to the delivery stream.</td></tr><tr><td><code>IncludeLinkedAccountsMetrics</code></td><td><code>boolean</code></td><td>If you are creating a metric stream in a monitoring account, specify true to include metrics from source accounts that are linked to this monitoring account, in the metric stream. The default is false.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.cloudwatch.metric_stream
WHERE region = 'us-east-1' AND data__Identifier = '{Name}'
</pre>
