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
<tr><td><b>Description</b></td><td>lifecycle_hooks</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.autoscaling.lifecycle_hooks</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>auto_scaling_group_name</code></td><td><code>string</code></td><td>The name of the Auto Scaling group for the lifecycle hook.</td></tr>
<tr><td><code>lifecycle_hook_name</code></td><td><code>string</code></td><td>The name of the lifecycle hook.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
auto_scaling_group_name,
lifecycle_hook_name
FROM awscc.autoscaling.lifecycle_hooks
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>lifecycle_hooks</code> resource, the following permissions are required:

### Create
```json
autoscaling:PutLifecycleHook,
autoscaling:DescribeLifecycleHooks,
iam:PassRole
```

### List
```json
autoscaling:DescribeLifecycleHooks
```

