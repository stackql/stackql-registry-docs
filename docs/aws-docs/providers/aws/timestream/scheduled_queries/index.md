---
title: scheduled_queries
hide_title: false
hide_table_of_contents: false
keywords:
  - scheduled_queries
  - timestream
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>scheduled_queries</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>scheduled_queries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.timestream.scheduled_queries</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Arn</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>ScheduledQueryName</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>QueryString</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>ScheduleConfiguration</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>NotificationConfiguration</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>ClientToken</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>ScheduledQueryExecutionRoleArn</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>TargetConfiguration</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>ErrorReportConfiguration</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>KmsKeyId</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>SQName</code></td><td><code>string</code></td><td>The name of the scheduled query. Scheduled query names must be unique within each Region.</td></tr><tr><td><code>SQQueryString</code></td><td><code>string</code></td><td>The query string to run. Parameter names can be specified in the query string @ character followed by an identifier. The named Parameter @scheduled_runtime is reserved and can be used in the query to get the time at which the query is scheduled to run. The timestamp calculated according to the ScheduleConfiguration parameter, will be the value of @scheduled_runtime paramater for each query run. For example, consider an instance of a scheduled query executing on 2021-12-01 00:00:00. For this instance, the @scheduled_runtime parameter is initialized to the timestamp 2021-12-01 00:00:00 when invoking the query.</td></tr><tr><td><code>SQScheduleConfiguration</code></td><td><code>string</code></td><td>Configuration for when the scheduled query is executed.</td></tr><tr><td><code>SQNotificationConfiguration</code></td><td><code>string</code></td><td>Notification configuration for the scheduled query. A notification is sent by Timestream when a query run finishes, when the state is updated or when you delete it.</td></tr><tr><td><code>SQScheduledQueryExecutionRoleArn</code></td><td><code>string</code></td><td>The ARN for the IAM role that Timestream will assume when running the scheduled query.</td></tr><tr><td><code>SQTargetConfiguration</code></td><td><code>string</code></td><td>Configuration of target store where scheduled query results are written to.</td></tr><tr><td><code>SQErrorReportConfiguration</code></td><td><code>string</code></td><td>Configuration for error reporting. Error reports will be generated when a problem is encountered when writing the query results.</td></tr><tr><td><code>SQKmsKeyId</code></td><td><code>string</code></td><td>The Amazon KMS key used to encrypt the scheduled query resource, at-rest. If the Amazon KMS key is not specified, the scheduled query resource will be encrypted with a Timestream owned Amazon KMS key. To specify a KMS key, use the key ID, key ARN, alias name, or alias ARN. When using an alias name, prefix the name with alias/. If ErrorReportConfiguration uses SSE_KMS as encryption type, the same KmsKeyId is used to encrypt the error report at rest.</td></tr><tr><td><code>Tags</code></td><td><code>undefined</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.timestream.scheduled_queries
WHERE region = 'us-east-1'
</pre>
