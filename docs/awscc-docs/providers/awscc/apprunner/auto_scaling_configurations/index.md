---
title: auto_scaling_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - auto_scaling_configurations
  - apprunner
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>auto_scaling_configurations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>auto_scaling_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>auto_scaling_configurations</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.apprunner.auto_scaling_configurations</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>auto_scaling_configuration_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of this auto scaling configuration.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>auto_scaling_configurations</code> resource, the following permissions are required:

### Create
```json
apprunner:CreateAutoScalingConfiguration,
apprunner:DescribeAutoScalingConfiguration,
apprunner:TagResource
```

### List
```json
apprunner:ListAutoScalingConfiguration
```


## Example
```sql
SELECT
region,
auto_scaling_configuration_arn
FROM awscc.apprunner.auto_scaling_configurations
WHERE region = 'us-east-1'
```
