---
title: lifecycle_hooks
hide_title: false
hide_table_of_contents: false
keywords:
  - lifecycle_hooks
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
Retrieves a list of <code>lifecycle_hooks</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>lifecycle_hooks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.autoscaling.lifecycle_hooks</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>AutoScalingGroupName</code></td><td><code>string</code></td><td>The name of the Auto Scaling group for the lifecycle hook.</td></tr><tr><td><code>DefaultResult</code></td><td><code>string</code></td><td>The action the Auto Scaling group takes when the lifecycle hook timeout elapses or if an unexpected failure occurs. The valid values are CONTINUE and ABANDON (default).</td></tr><tr><td><code>HeartbeatTimeout</code></td><td><code>integer</code></td><td>The maximum time, in seconds, that can elapse before the lifecycle hook times out. The range is from 30 to 7200 seconds. The default value is 3600 seconds (1 hour). If the lifecycle hook times out, Amazon EC2 Auto Scaling performs the action that you specified in the DefaultResult property.</td></tr><tr><td><code>LifecycleHookName</code></td><td><code>string</code></td><td>The name of the lifecycle hook.</td></tr><tr><td><code>LifecycleTransition</code></td><td><code>string</code></td><td>The instance state to which you want to attach the lifecycle hook.</td></tr><tr><td><code>NotificationMetadata</code></td><td><code>string</code></td><td>Additional information that is included any time Amazon EC2 Auto Scaling sends a message to the notification target.</td></tr><tr><td><code>NotificationTargetARN</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the notification target that Amazon EC2 Auto Scaling uses to notify you when an instance is in the transition state for the lifecycle hook. You can specify an Amazon SQS queue or an Amazon SNS topic. The notification message includes the following information: lifecycle action token, user account ID, Auto Scaling group name, lifecycle hook name, instance ID, lifecycle transition, and notification metadata.</td></tr><tr><td><code>RoleARN</code></td><td><code>string</code></td><td>The ARN of the IAM role that allows the Auto Scaling group to publish to the specified notification target, for example, an Amazon SNS topic or an Amazon SQS queue.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.autoscaling.lifecycle_hooks
WHERE region = 'us-east-1'
</pre>
