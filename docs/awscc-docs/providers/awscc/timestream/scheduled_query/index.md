---
title: scheduled_query
hide_title: false
hide_table_of_contents: false
keywords:
  - scheduled_query
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
Gets an individual <code>scheduled_query</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>scheduled_query</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>scheduled_query</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.timestream.scheduled_query</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>scheduled_query_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>query_string</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>schedule_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>notification_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>client_token</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>scheduled_query_execution_role_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>target_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>error_report_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>kms_key_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>sq_name</code></td><td><code>string</code></td><td>The name of the scheduled query. Scheduled query names must be unique within each Region.</td></tr>
<tr><td><code>sq_query_string</code></td><td><code>string</code></td><td>The query string to run. Parameter names can be specified in the query string @ character followed by an identifier. The named Parameter @scheduled_runtime is reserved and can be used in the query to get the time at which the query is scheduled to run. The timestamp calculated according to the ScheduleConfiguration parameter, will be the value of @scheduled_runtime paramater for each query run. For example, consider an instance of a scheduled query executing on 2021-12-01 00:00:00. For this instance, the @scheduled_runtime parameter is initialized to the timestamp 2021-12-01 00:00:00 when invoking the query.</td></tr>
<tr><td><code>sq_schedule_configuration</code></td><td><code>string</code></td><td>Configuration for when the scheduled query is executed.</td></tr>
<tr><td><code>sq_notification_configuration</code></td><td><code>string</code></td><td>Notification configuration for the scheduled query. A notification is sent by Timestream when a query run finishes, when the state is updated or when you delete it.</td></tr>
<tr><td><code>sq_scheduled_query_execution_role_arn</code></td><td><code>string</code></td><td>The ARN for the IAM role that Timestream will assume when running the scheduled query.</td></tr>
<tr><td><code>sq_target_configuration</code></td><td><code>string</code></td><td>Configuration of target store where scheduled query results are written to.</td></tr>
<tr><td><code>sq_error_report_configuration</code></td><td><code>string</code></td><td>Configuration for error reporting. Error reports will be generated when a problem is encountered when writing the query results.</td></tr>
<tr><td><code>sq_kms_key_id</code></td><td><code>string</code></td><td>The Amazon KMS key used to encrypt the scheduled query resource, at-rest. If the Amazon KMS key is not specified, the scheduled query resource will be encrypted with a Timestream owned Amazon KMS key. To specify a KMS key, use the key ID, key ARN, alias name, or alias ARN. When using an alias name, prefix the name with alias&#x2F;. If ErrorReportConfiguration uses SSE_KMS as encryption type, the same KmsKeyId is used to encrypt the error report at rest.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
arn,
scheduled_query_name,
query_string,
schedule_configuration,
notification_configuration,
client_token,
scheduled_query_execution_role_arn,
target_configuration,
error_report_configuration,
kms_key_id,
sq_name,
sq_query_string,
sq_schedule_configuration,
sq_notification_configuration,
sq_scheduled_query_execution_role_arn,
sq_target_configuration,
sq_error_report_configuration,
sq_kms_key_id,
tags
FROM awscc.timestream.scheduled_query
WHERE region = 'us-east-1'
AND data__Identifier = '{Arn}';
```

## Permissions

To operate on the <code>scheduled_query</code> resource, the following permissions are required:

### Read
```json
timestream:DescribeScheduledQuery,
timestream:ListTagsForResource,
timestream:DescribeEndpoints
```

### Update
```json
timestream:UpdateScheduledQuery,
timestream:TagResource,
timestream:UntagResource,
timestream:DescribeEndpoints
```

### Delete
```json
timestream:DeleteScheduledQuery,
timestream:DescribeEndpoints
```

