---
title: instance_profile
hide_title: false
hide_table_of_contents: false
keywords:
  - instance_profile
  - dms
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>instance_profile</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instance_profile</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>instance_profile</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.dms.instance_profile</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>instance_profile_arn</code></td><td><code>string</code></td><td>The property describes an ARN of the instance profile.</td></tr>
<tr><td><code>instance_profile_identifier</code></td><td><code>string</code></td><td>The property describes an identifier for the instance profile. It is used for describing&#x2F;deleting&#x2F;modifying. Can be name&#x2F;arn</td></tr>
<tr><td><code>availability_zone</code></td><td><code>string</code></td><td>The property describes an availability zone of the instance profile.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>The optional description of the instance profile.</td></tr>
<tr><td><code>kms_key_arn</code></td><td><code>string</code></td><td>The property describes kms key arn for the instance profile.</td></tr>
<tr><td><code>publicly_accessible</code></td><td><code>boolean</code></td><td>The property describes the publicly accessible of the instance profile</td></tr>
<tr><td><code>network_type</code></td><td><code>string</code></td><td>The property describes a network type for the instance profile.</td></tr>
<tr><td><code>instance_profile_name</code></td><td><code>string</code></td><td>The property describes a name for the instance profile.</td></tr>
<tr><td><code>instance_profile_creation_time</code></td><td><code>string</code></td><td>The property describes a creating time of the instance profile.</td></tr>
<tr><td><code>subnet_group_identifier</code></td><td><code>string</code></td><td>The property describes a subnet group identifier for the instance profile.</td></tr>
<tr><td><code>vpc_security_groups</code></td><td><code>array</code></td><td>The property describes vps security groups for the instance profile.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
instance_profile_arn,
instance_profile_identifier,
availability_zone,
description,
kms_key_arn,
publicly_accessible,
network_type,
instance_profile_name,
instance_profile_creation_time,
subnet_group_identifier,
vpc_security_groups,
tags
FROM awscc.dms.instance_profile
WHERE data__Identifier = '<InstanceProfileArn>';
```

## Permissions

To operate on the <code>instance_profile</code> resource, the following permissions are required:

### Read
```json
dms:ListInstanceProfiles,
dms:DescribeInstanceProfiles,
dms:ListTagsForResource
```

### Update
```json
dms:UpdateInstanceProfile,
dms:ModifyInstanceProfile,
dms:AddTagsToResource,
dms:RemoveTagsToResource,
dms:ListTagsForResource
```

### Delete
```json
dms:DeleteInstanceProfile
```

