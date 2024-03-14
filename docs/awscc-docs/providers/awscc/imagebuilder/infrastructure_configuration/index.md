---
title: infrastructure_configuration
hide_title: false
hide_table_of_contents: false
keywords:
  - infrastructure_configuration
  - imagebuilder
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>infrastructure_configuration</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>infrastructure_configuration</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>infrastructure_configuration</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.imagebuilder.infrastructure_configuration</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the infrastructure configuration.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the infrastructure configuration.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>The description of the infrastructure configuration.</td></tr>
<tr><td><code>instance_types</code></td><td><code>array</code></td><td>The instance types of the infrastructure configuration.</td></tr>
<tr><td><code>security_group_ids</code></td><td><code>array</code></td><td>The security group IDs of the infrastructure configuration.</td></tr>
<tr><td><code>logging</code></td><td><code>object</code></td><td>The logging configuration of the infrastructure configuration.</td></tr>
<tr><td><code>subnet_id</code></td><td><code>string</code></td><td>The subnet ID of the infrastructure configuration.</td></tr>
<tr><td><code>key_pair</code></td><td><code>string</code></td><td>The EC2 key pair of the infrastructure configuration..</td></tr>
<tr><td><code>terminate_instance_on_failure</code></td><td><code>boolean</code></td><td>The terminate instance on failure configuration of the infrastructure configuration.</td></tr>
<tr><td><code>instance_profile_name</code></td><td><code>string</code></td><td>The instance profile of the infrastructure configuration.</td></tr>
<tr><td><code>instance_metadata_options</code></td><td><code>object</code></td><td>The instance metadata option settings for the infrastructure configuration.</td></tr>
<tr><td><code>sns_topic_arn</code></td><td><code>string</code></td><td>The SNS Topic Amazon Resource Name (ARN) of the infrastructure configuration.</td></tr>
<tr><td><code>resource_tags</code></td><td><code>object</code></td><td>The tags attached to the resource created by Image Builder.</td></tr>
<tr><td><code>tags</code></td><td><code>object</code></td><td>The tags associated with the component.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
arn,
name,
description,
instance_types,
security_group_ids,
logging,
subnet_id,
key_pair,
terminate_instance_on_failure,
instance_profile_name,
instance_metadata_options,
sns_topic_arn,
resource_tags,
tags
FROM awscc.imagebuilder.infrastructure_configuration
WHERE data__Identifier = '<Arn>';
```

## Permissions

To operate on the <code>infrastructure_configuration</code> resource, the following permissions are required:

### Update
```json
iam:PassRole,
sns:Publish,
imagebuilder:GetInfrastructureConfiguration,
imagebuilder:UpdateInfrastructureConfiguration
```

### Read
```json
imagebuilder:GetInfrastructureConfiguration
```

### Delete
```json
imagebuilder:UnTagResource,
imagebuilder:GetInfrastructureConfiguration,
imagebuilder:DeleteInfrastructureConfiguration
```

