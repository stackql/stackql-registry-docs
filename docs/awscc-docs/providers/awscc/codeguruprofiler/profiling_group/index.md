---
title: profiling_group
hide_title: false
hide_table_of_contents: false
keywords:
  - profiling_group
  - codeguruprofiler
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>profiling_group</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>profiling_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>profiling_group</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.codeguruprofiler.profiling_group</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>profiling_group_name</code></td><td><code>string</code></td><td>The name of the profiling group.</td></tr>
<tr><td><code>compute_platform</code></td><td><code>string</code></td><td>The compute platform of the profiling group.</td></tr>
<tr><td><code>agent_permissions</code></td><td><code>object</code></td><td>The agent permissions attached to this profiling group.</td></tr>
<tr><td><code>anomaly_detection_notification_configuration</code></td><td><code>array</code></td><td>Configuration for Notification Channels for Anomaly Detection feature in CodeGuru Profiler which enables customers to detect anomalies in the application profile for those methods that represent the highest proportion of CPU time or latency</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the specified profiling group.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>The tags associated with a profiling group.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
profiling_group_name,
compute_platform,
agent_permissions,
anomaly_detection_notification_configuration,
arn,
tags
FROM awscc.codeguruprofiler.profiling_group
WHERE data__Identifier = '<ProfilingGroupName>';
```

## Permissions

To operate on the <code>profiling_group</code> resource, the following permissions are required:

### Read
```json
codeguru-profiler:DescribeProfilingGroup,
codeguru-profiler:ListTagsForResource
```

### Update
```json
sns:Publish,
codeguru-profiler:AddNotificationChannels,
codeguru-profiler:GetNotificationConfiguration,
codeguru-profiler:RemoveNotificationChannel,
codeguru-profiler:PutPermission,
codeguru-profiler:RemovePermission,
codeguru-profiler:GetPolicy,
codeguru-profiler:TagResource,
codeguru-profiler:UntagResource,
codeguru-profiler:ListTagsForResource
```

### Delete
```json
codeguru-profiler:DeleteProfilingGroup
```

