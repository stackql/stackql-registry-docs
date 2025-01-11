---
title: log_streams
hide_title: false
hide_table_of_contents: false
keywords:
  - log_streams
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

Represents a log stream, which is a sequence of log events from a single emitter of logs.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>log_streams</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Represents a log stream, which is a sequence of log events from a single emitter of logs.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cloudwatch.log_streams" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="log_stream_name" /></td><td><code>string</code></td><td>The name of the log stream.</td></tr>
<tr><td><CopyableCode code="creation_time" /></td><td><code>integer</code></td><td>The creation time of the stream, expressed as the number of milliseconds after <code>Jan 1, 1970 00:00:00 UTC</code>.</td></tr>
<tr><td><CopyableCode code="first_event_timestamp" /></td><td><code>integer</code></td><td>The time of the first event, expressed as the number of milliseconds after <code>Jan 1, 1970 00:00:00 UTC</code>.</td></tr>
<tr><td><CopyableCode code="last_event_timestamp" /></td><td><code>integer</code></td><td>The time of the most recent log event in the log stream in CloudWatch Logs. This number is expressed as the number of milliseconds after <code>Jan 1, 1970 00:00:00 UTC</code>. The <code>lastEventTime</code> value updates on an eventual consistency basis. It typically updates in less than an hour from ingestion, but in rare situations might take longer.</td></tr>
<tr><td><CopyableCode code="last_ingestion_time" /></td><td><code>integer</code></td><td>The ingestion time, expressed as the number of milliseconds after <code>Jan 1, 1970 00:00:00 UTC</code> The <code>lastIngestionTime</code> value updates on an eventual consistency basis. It typically updates in less than an hour after ingestion, but in rare situations might take longer.</td></tr>
<tr><td><CopyableCode code="upload_sequence_token" /></td><td><code>string</code></td><td><p>The sequence token.</p> <important> <p>The sequence token is now ignored in <code>PutLogEvents</code> actions. <code>PutLogEvents</code> actions are always accepted regardless of receiving an invalid sequence token. You don't need to obtain <code>uploadSequenceToken</code> to use a <code>PutLogEvents</code> action.</p> </important></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the log stream.</td></tr>
<tr><td><CopyableCode code="stored_bytes" /></td><td><code>integer</code></td><td><p>The number of bytes stored.</p> <p> <b>Important:</b> As of June 17, 2019, this parameter is no longer supported for log streams, and is always reported as zero. This change applies only to log streams. The <code>storedBytes</code> parameter for log groups is not affected.</p>Starting on June 17, 2019, this parameter will be deprecated for log streams, and will be reported as zero. This change applies only to log streams. The storedBytes parameter for log groups is not affected.</td></tr>
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
    <td><CopyableCode code="DescribeLogGroups" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="CreateLogGroup" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="data__logGroupName, data__logStreamName, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="DeleteLogGroup" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__logGroupName, data__logStreamName, region" /></td>
  </tr>
</tbody></table>






