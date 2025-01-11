---
title: job_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - job_tags
  - glue
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

Expands all tag keys and values for <code>jobs</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>job_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Glue::Job</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.glue.job_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="connections" /></td><td><code>object</code></td><td>Specifies the connections used by a job</td></tr>
<tr><td><CopyableCode code="max_retries" /></td><td><code>number</code></td><td>The maximum number of times to retry this job after a JobRun fails</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A description of the job.</td></tr>
<tr><td><CopyableCode code="timeout" /></td><td><code>integer</code></td><td>The maximum time that a job run can consume resources before it is terminated and enters TIMEOUT status.</td></tr>
<tr><td><CopyableCode code="allocated_capacity" /></td><td><code>number</code></td><td>The number of capacity units that are allocated to this job.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name you assign to the job definition</td></tr>
<tr><td><CopyableCode code="role" /></td><td><code>string</code></td><td>The name or Amazon Resource Name (ARN) of the IAM role associated with this job.</td></tr>
<tr><td><CopyableCode code="default_arguments" /></td><td><code>object</code></td><td>The default arguments for this job, specified as name-value pairs.</td></tr>
<tr><td><CopyableCode code="notification_property" /></td><td><code>object</code></td><td>Specifies configuration properties of a notification.</td></tr>
<tr><td><CopyableCode code="worker_type" /></td><td><code>string</code></td><td>TThe type of predefined worker that is allocated when a job runs.</td></tr>
<tr><td><CopyableCode code="execution_class" /></td><td><code>string</code></td><td>Indicates whether the job is run with a standard or flexible execution class.</td></tr>
<tr><td><CopyableCode code="log_uri" /></td><td><code>string</code></td><td>This field is reserved for future use.</td></tr>
<tr><td><CopyableCode code="command" /></td><td><code>object</code></td><td>The code that executes a job.</td></tr>
<tr><td><CopyableCode code="glue_version" /></td><td><code>string</code></td><td>Glue version determines the versions of Apache Spark and Python that AWS Glue supports.</td></tr>
<tr><td><CopyableCode code="execution_property" /></td><td><code>object</code></td><td>The maximum number of concurrent runs that are allowed for this job.</td></tr>
<tr><td><CopyableCode code="security_configuration" /></td><td><code>string</code></td><td>The name of the SecurityConfiguration structure to be used with this job.</td></tr>
<tr><td><CopyableCode code="number_of_workers" /></td><td><code>integer</code></td><td>The number of workers of a defined workerType that are allocated when a job runs.</td></tr>
<tr><td><CopyableCode code="max_capacity" /></td><td><code>number</code></td><td>The number of AWS Glue data processing units (DPUs) that can be allocated when this job runs.</td></tr>
<tr><td><CopyableCode code="non_overridable_arguments" /></td><td><code>object</code></td><td>Non-overridable arguments for this job, specified as name-value pairs.</td></tr>
<tr><td><CopyableCode code="maintenance_window" /></td><td><code>string</code></td><td>Property description not available.</td></tr>
<tr><td><CopyableCode code="job_mode" /></td><td><code>string</code></td><td>Property description not available.</td></tr>
<tr><td><CopyableCode code="job_run_queuing_enabled" /></td><td><code>boolean</code></td><td>Property description not available.</td></tr>
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
Expands tags for all <code>jobs</code> in a region.
```sql
SELECT
region,
connections,
max_retries,
description,
timeout,
allocated_capacity,
name,
role,
default_arguments,
notification_property,
worker_type,
execution_class,
log_uri,
command,
glue_version,
execution_property,
security_configuration,
number_of_workers,
max_capacity,
non_overridable_arguments,
maintenance_window,
job_mode,
job_run_queuing_enabled,
tag_key,
tag_value
FROM aws.glue.job_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>job_tags</code> resource, see <a href="/providers/aws/glue/jobs/#permissions"><code>jobs</code></a>

