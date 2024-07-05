---
title: lifecycle_hooks_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - lifecycle_hooks_list_only
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Lists <code>lifecycle_hooks</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/lifecycle_hooks/"><code>lifecycle_hooks</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>lifecycle_hooks_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::AutoScaling::LifecycleHook</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.autoscaling.lifecycle_hooks_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="auto_scaling_group_name" /></td><td><code>string</code></td><td>The name of the Auto Scaling group for the lifecycle hook.</td></tr>
<tr><td><CopyableCode code="default_result" /></td><td><code>string</code></td><td>The action the Auto Scaling group takes when the lifecycle hook timeout elapses or if an unexpected failure occurs. The valid values are CONTINUE and ABANDON (default).</td></tr>
<tr><td><CopyableCode code="heartbeat_timeout" /></td><td><code>integer</code></td><td>The maximum time, in seconds, that can elapse before the lifecycle hook times out. The range is from 30 to 7200 seconds. The default value is 3600 seconds (1 hour). If the lifecycle hook times out, Amazon EC2 Auto Scaling performs the action that you specified in the DefaultResult property.</td></tr>
<tr><td><CopyableCode code="lifecycle_hook_name" /></td><td><code>string</code></td><td>The name of the lifecycle hook.</td></tr>
<tr><td><CopyableCode code="lifecycle_transition" /></td><td><code>string</code></td><td>The instance state to which you want to attach the lifecycle hook.</td></tr>
<tr><td><CopyableCode code="notification_metadata" /></td><td><code>string</code></td><td>Additional information that is included any time Amazon EC2 Auto Scaling sends a message to the notification target.</td></tr>
<tr><td><CopyableCode code="notification_target_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the notification target that Amazon EC2 Auto Scaling uses to notify you when an instance is in the transition state for the lifecycle hook. You can specify an Amazon SQS queue or an Amazon SNS topic. The notification message includes the following information: lifecycle action token, user account ID, Auto Scaling group name, lifecycle hook name, instance ID, lifecycle transition, and notification metadata.</td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td>The ARN of the IAM role that allows the Auto Scaling group to publish to the specified notification target, for example, an Amazon SNS topic or an Amazon SQS queue.</td></tr>
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
Lists all <code>lifecycle_hooks</code> in a region.
```sql
SELECT
region,
auto_scaling_group_name,
lifecycle_hook_name
FROM aws.autoscaling.lifecycle_hooks_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>lifecycle_hooks_list_only</code> resource, see <a href="/providers/aws/autoscaling/lifecycle_hooks/#permissions"><code>lifecycle_hooks</code></a>


