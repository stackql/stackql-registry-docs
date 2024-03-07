---
title: launch_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - launch_configurations
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
Retrieves a list of <code>launch_configurations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>launch_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>launch_configurations</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.autoscaling.launch_configurations</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>launch_configuration_name</code></td><td><code>string</code></td><td>The name of the launch configuration. This name must be unique per Region per account.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
launch_configuration_name
FROM awscc.autoscaling.launch_configurations
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>launch_configurations</code> resource, the following permissions are required:

### Create
```json
autoscaling:CreateLaunchConfiguration,
autoscaling:DescribeLaunchConfigurations,
iam:PassRole
```

### List
```json
autoscaling:DescribeLaunchConfigurations
```

