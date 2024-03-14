---
title: environment
hide_title: false
hide_table_of_contents: false
keywords:
  - environment
  - m2
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>environment</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>environment</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>environment</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.m2.environment</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>The description of the environment.</td></tr>
<tr><td><code>engine_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>engine_version</code></td><td><code>string</code></td><td>The version of the runtime engine for the environment.</td></tr>
<tr><td><code>environment_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the runtime environment.</td></tr>
<tr><td><code>environment_id</code></td><td><code>string</code></td><td>The unique identifier of the environment.</td></tr>
<tr><td><code>high_availability_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>instance_type</code></td><td><code>string</code></td><td>The type of instance underlying the environment.</td></tr>
<tr><td><code>kms_key_id</code></td><td><code>string</code></td><td>The ID or the Amazon Resource Name (ARN) of the customer managed KMS Key used for encrypting environment-related resources.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the environment.</td></tr>
<tr><td><code>preferred_maintenance_window</code></td><td><code>string</code></td><td>Configures a desired maintenance window for the environment. If you do not provide a value, a random system-generated value will be assigned.</td></tr>
<tr><td><code>publicly_accessible</code></td><td><code>boolean</code></td><td>Specifies whether the environment is publicly accessible.</td></tr>
<tr><td><code>security_group_ids</code></td><td><code>array</code></td><td>The list of security groups for the VPC associated with this environment.</td></tr>
<tr><td><code>storage_configurations</code></td><td><code>array</code></td><td>The storage configurations defined for the runtime environment.</td></tr>
<tr><td><code>subnet_ids</code></td><td><code>array</code></td><td>The unique identifiers of the subnets assigned to this runtime environment.</td></tr>
<tr><td><code>tags</code></td><td><code>object</code></td><td>Tags associated to this environment.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
description,
engine_type,
engine_version,
environment_arn,
environment_id,
high_availability_config,
instance_type,
kms_key_id,
name,
preferred_maintenance_window,
publicly_accessible,
security_group_ids,
storage_configurations,
subnet_ids,
tags
FROM awscc.m2.environment
WHERE data__Identifier = '<EnvironmentArn>';
```

## Permissions

To operate on the <code>environment</code> resource, the following permissions are required:

### Read
```json
m2:ListTagsForResource,
m2:GetEnvironment
```

### Update
```json
m2:TagResource,
m2:UntagResource,
m2:ListTagsForResource,
m2:GetEnvironment,
m2:UpdateEnvironment
```

### Delete
```json
elasticloadbalancing:DeleteLoadBalancer,
m2:DeleteEnvironment,
m2:GetEnvironment
```

