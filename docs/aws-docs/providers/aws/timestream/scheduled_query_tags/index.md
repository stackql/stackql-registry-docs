---
title: scheduled_query_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - scheduled_query_tags
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Expands all tag keys and values for <code>scheduled_queries</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>scheduled_query_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::Timestream::ScheduledQuery resource creates a Timestream Scheduled Query.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.timestream.scheduled_query_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Amazon Resource Name of the scheduled query that is generated upon creation.</td></tr>
<tr><td><CopyableCode code="scheduled_query_name" /></td><td><code>string</code></td><td>The name of the scheduled query. Scheduled query names must be unique within each Region.</td></tr>
<tr><td><CopyableCode code="query_string" /></td><td><code>string</code></td><td>The query string to run. Parameter names can be specified in the query string @ character followed by an identifier. The named Parameter @scheduled_runtime is reserved and can be used in the query to get the time at which the query is scheduled to run. The timestamp calculated according to the ScheduleConfiguration parameter, will be the value of @scheduled_runtime paramater for each query run. For example, consider an instance of a scheduled query executing on 2021-12-01 00:00:00. For this instance, the @scheduled_runtime parameter is initialized to the timestamp 2021-12-01 00:00:00 when invoking the query.</td></tr>
<tr><td><CopyableCode code="schedule_configuration" /></td><td><code>object</code></td><td>Configuration for when the scheduled query is executed.</td></tr>
<tr><td><CopyableCode code="notification_configuration" /></td><td><code>object</code></td><td>Notification configuration for the scheduled query. A notification is sent by Timestream when a query run finishes, when the state is updated or when you delete it.</td></tr>
<tr><td><CopyableCode code="client_token" /></td><td><code>string</code></td><td>Using a ClientToken makes the call to CreateScheduledQuery idempotent, in other words, making the same request repeatedly will produce the same result. Making multiple identical CreateScheduledQuery requests has the same effect as making a single request. If CreateScheduledQuery is called without a ClientToken, the Query SDK generates a ClientToken on your behalf. After 8 hours, any request with the same ClientToken is treated as a new request.</td></tr>
<tr><td><CopyableCode code="scheduled_query_execution_role_arn" /></td><td><code>string</code></td><td>The ARN for the IAM role that Timestream will assume when running the scheduled query.</td></tr>
<tr><td><CopyableCode code="target_configuration" /></td><td><code>object</code></td><td>Configuration of target store where scheduled query results are written to.</td></tr>
<tr><td><CopyableCode code="error_report_configuration" /></td><td><code>object</code></td><td>Configuration for error reporting. Error reports will be generated when a problem is encountered when writing the query results.</td></tr>
<tr><td><CopyableCode code="kms_key_id" /></td><td><code>string</code></td><td>The Amazon KMS key used to encrypt the scheduled query resource, at-rest. If the Amazon KMS key is not specified, the scheduled query resource will be encrypted with a Timestream owned Amazon KMS key. To specify a KMS key, use the key ID, key ARN, alias name, or alias ARN. When using an alias name, prefix the name with alias/. If ErrorReportConfiguration uses SSE_KMS as encryption type, the same KmsKeyId is used to encrypt the error report at rest.</td></tr>
<tr><td><CopyableCode code="sq_name" /></td><td><code>string</code></td><td>The name of the scheduled query. Scheduled query names must be unique within each Region.</td></tr>
<tr><td><CopyableCode code="sq_query_string" /></td><td><code>string</code></td><td>The query string to run. Parameter names can be specified in the query string @ character followed by an identifier. The named Parameter @scheduled_runtime is reserved and can be used in the query to get the time at which the query is scheduled to run. The timestamp calculated according to the ScheduleConfiguration parameter, will be the value of @scheduled_runtime paramater for each query run. For example, consider an instance of a scheduled query executing on 2021-12-01 00:00:00. For this instance, the @scheduled_runtime parameter is initialized to the timestamp 2021-12-01 00:00:00 when invoking the query.</td></tr>
<tr><td><CopyableCode code="sq_schedule_configuration" /></td><td><code>string</code></td><td>Configuration for when the scheduled query is executed.</td></tr>
<tr><td><CopyableCode code="sq_notification_configuration" /></td><td><code>string</code></td><td>Notification configuration for the scheduled query. A notification is sent by Timestream when a query run finishes, when the state is updated or when you delete it.</td></tr>
<tr><td><CopyableCode code="sq_scheduled_query_execution_role_arn" /></td><td><code>string</code></td><td>The ARN for the IAM role that Timestream will assume when running the scheduled query.</td></tr>
<tr><td><CopyableCode code="sq_target_configuration" /></td><td><code>string</code></td><td>Configuration of target store where scheduled query results are written to.</td></tr>
<tr><td><CopyableCode code="sq_error_report_configuration" /></td><td><code>string</code></td><td>Configuration for error reporting. Error reports will be generated when a problem is encountered when writing the query results.</td></tr>
<tr><td><CopyableCode code="sq_kms_key_id" /></td><td><code>string</code></td><td>The Amazon KMS key used to encrypt the scheduled query resource, at-rest. If the Amazon KMS key is not specified, the scheduled query resource will be encrypted with a Timestream owned Amazon KMS key. To specify a KMS key, use the key ID, key ARN, alias name, or alias ARN. When using an alias name, prefix the name with alias/. If ErrorReportConfiguration uses SSE_KMS as encryption type, the same KmsKeyId is used to encrypt the error report at rest.</td></tr>
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
Expands tags for all <code>scheduled_queries</code> in a region.
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
tag_key,
tag_value
FROM aws.timestream.scheduled_query_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>scheduled_query_tags</code> resource, see <a href="/providers/aws/timestream/scheduled_queries/#permissions"><code>scheduled_queries</code></a>

