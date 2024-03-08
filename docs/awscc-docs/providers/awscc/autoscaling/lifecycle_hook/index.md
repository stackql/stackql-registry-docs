---
title: lifecycle_hook
hide_title: false
hide_table_of_contents: false
keywords:
  - lifecycle_hook
  - autoscaling
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>lifecycle_hook</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>lifecycle_hook</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>lifecycle_hook</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.autoscaling.lifecycle_hook</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>auto_scaling_group_name</code></td><td><code>string</code></td><td>The name of the Auto Scaling group for the lifecycle hook.</td></tr>
<tr><td><code>default_result</code></td><td><code>string</code></td><td>The action the Auto Scaling group takes when the lifecycle hook timeout elapses or if an unexpected failure occurs. The valid values are CONTINUE and ABANDON (default).</td></tr>
<tr><td><code>heartbeat_timeout</code></td><td><code>integer</code></td><td>The maximum time, in seconds, that can elapse before the lifecycle hook times out. The range is from 30 to 7200 seconds. The default value is 3600 seconds (1 hour). If the lifecycle hook times out, Amazon EC2 Auto Scaling performs the action that you specified in the DefaultResult property.</td></tr>
<tr><td><code>lifecycle_hook_name</code></td><td><code>string</code></td><td>The name of the lifecycle hook.</td></tr>
<tr><td><code>lifecycle_transition</code></td><td><code>string</code></td><td>The instance state to which you want to attach the lifecycle hook.</td></tr>
<tr><td><code>notification_metadata</code></td><td><code>string</code></td><td>Additional information that is included any time Amazon EC2 Auto Scaling sends a message to the notification target.</td></tr>
<tr><td><code>notification_target_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the notification target that Amazon EC2 Auto Scaling uses to notify you when an instance is in the transition state for the lifecycle hook. You can specify an Amazon SQS queue or an Amazon SNS topic. The notification message includes the following information: lifecycle action token, user account ID, Auto Scaling group name, lifecycle hook name, instance ID, lifecycle transition, and notification metadata.</td></tr>
<tr><td><code>role_arn</code></td><td><code>string</code></td><td>The ARN of the IAM role that allows the Auto Scaling group to publish to the specified notification target, for example, an Amazon SNS topic or an Amazon SQS queue.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
auto_scaling_group_name,
default_result,
heartbeat_timeout,
lifecycle_hook_name,
lifecycle_transition,
notification_metadata,
notification_target_ar_n,
role_ar_n
FROM awscc.autoscaling.lifecycle_hook
WHERE region = 'us-east-1'
AND data__Identifier = '{AutoScalingGroupName}';
AND data__Identifier = '{LifecycleHookName}';
```

## Permissions

To operate on the <code>lifecycle_hook</code> resource, the following permissions are required:

### Read
```json
autoscaling:DescribeLifecycleHooks
```

### Update
```json
autoscaling:PutLifecycleHook,
autoscaling:DescribeLifecycleHooks,
iam:PassRole
```

### Delete
```json
autoscaling:DeleteLifecycleHook,
autoscaling:DescribeLifecycleHooks
```

