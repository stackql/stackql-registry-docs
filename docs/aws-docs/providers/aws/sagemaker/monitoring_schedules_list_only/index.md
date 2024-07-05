---
title: monitoring_schedules_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - monitoring_schedules_list_only
  - sagemaker
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

Lists <code>monitoring_schedules</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/monitoring_schedules/"><code>monitoring_schedules</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>monitoring_schedules_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SageMaker::MonitoringSchedule</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.sagemaker.monitoring_schedules_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="monitoring_schedule_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the monitoring schedule.</td></tr>
<tr><td><CopyableCode code="monitoring_schedule_name" /></td><td><code>string</code></td><td>The name of the monitoring schedule.</td></tr>
<tr><td><CopyableCode code="monitoring_schedule_config" /></td><td><code>object</code></td><td>The configuration object that specifies the monitoring schedule and defines the monitoring job.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="creation_time" /></td><td><code>string</code></td><td>The time at which the schedule was created.</td></tr>
<tr><td><CopyableCode code="endpoint_name" /></td><td><code>string</code></td><td>The name of the endpoint used to run the monitoring job.</td></tr>
<tr><td><CopyableCode code="failure_reason" /></td><td><code>string</code></td><td>Contains the reason a monitoring job failed, if it failed.</td></tr>
<tr><td><CopyableCode code="last_modified_time" /></td><td><code>string</code></td><td>A timestamp that indicates the last time the monitoring job was modified.</td></tr>
<tr><td><CopyableCode code="last_monitoring_execution_summary" /></td><td><code>object</code></td><td>Describes metadata on the last execution to run, if there was one.</td></tr>
<tr><td><CopyableCode code="monitoring_schedule_status" /></td><td><code>string</code></td><td>The status of a schedule job.</td></tr>
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
Lists all <code>monitoring_schedules</code> in a region.
```sql
SELECT
region,
monitoring_schedule_arn
FROM aws.sagemaker.monitoring_schedules_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>monitoring_schedules_list_only</code> resource, see <a href="/providers/aws/sagemaker/monitoring_schedules/#permissions"><code>monitoring_schedules</code></a>


