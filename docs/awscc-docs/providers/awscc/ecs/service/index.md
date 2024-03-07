---
title: service
hide_title: false
hide_table_of_contents: false
keywords:
  - service
  - ecs
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>service</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>service</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.ecs.service</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>service_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>capacity_provider_strategy</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>cluster</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>deployment_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>deployment_controller</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>desired_count</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>enable_ec_smanaged_tags</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>enable_execute_command</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>health_check_grace_period_seconds</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>launch_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>load_balancers</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>network_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>placement_constraints</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>placement_strategies</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>platform_version</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>propagate_tags</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>role</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>scheduling_strategy</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>service_connect_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>service_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>service_registries</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>task_definition</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>volume_configurations</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
service_arn,
capacity_provider_strategy,
cluster,
deployment_configuration,
deployment_controller,
desired_count,
enable_ec_smanaged_tags,
enable_execute_command,
health_check_grace_period_seconds,
launch_type,
load_balancers,
name,
network_configuration,
placement_constraints,
placement_strategies,
platform_version,
propagate_tags,
role,
scheduling_strategy,
service_connect_configuration,
service_name,
service_registries,
tags,
task_definition,
volume_configurations
FROM awscc.ecs.service
WHERE region = 'us-east-1'
AND data__Identifier = '{ServiceArn}';
AND data__Identifier = '{Cluster}';
```

## Permissions

To operate on the <code>service</code> resource, the following permissions are required:

### Read
```json
ecs:DescribeServices
```

### Update
```json
ecs:DescribeServices,
ecs:ListTagsForResource,
ecs:TagResource,
ecs:UntagResource,
ecs:UpdateService
```

### Delete
```json
ecs:DeleteService,
ecs:DescribeServices
```

