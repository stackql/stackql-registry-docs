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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Gets or operates on an individual <code>instance_profile</code> resource, use <code>instance_profiles</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instance_profile</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::DMS::InstanceProfile.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.dms.instance_profile" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="instance_profile_arn" /></td><td><code>string</code></td><td>The property describes an ARN of the instance profile.</td></tr>
<tr><td><CopyableCode code="instance_profile_identifier" /></td><td><code>string</code></td><td>The property describes an identifier for the instance profile. It is used for describing&#x2F;deleting&#x2F;modifying. Can be name&#x2F;arn</td></tr>
<tr><td><CopyableCode code="availability_zone" /></td><td><code>string</code></td><td>The property describes an availability zone of the instance profile.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The optional description of the instance profile.</td></tr>
<tr><td><CopyableCode code="kms_key_arn" /></td><td><code>string</code></td><td>The property describes kms key arn for the instance profile.</td></tr>
<tr><td><CopyableCode code="publicly_accessible" /></td><td><code>boolean</code></td><td>The property describes the publicly accessible of the instance profile</td></tr>
<tr><td><CopyableCode code="network_type" /></td><td><code>string</code></td><td>The property describes a network type for the instance profile.</td></tr>
<tr><td><CopyableCode code="instance_profile_name" /></td><td><code>string</code></td><td>The property describes a name for the instance profile.</td></tr>
<tr><td><CopyableCode code="instance_profile_creation_time" /></td><td><code>string</code></td><td>The property describes a creating time of the instance profile.</td></tr>
<tr><td><CopyableCode code="subnet_group_identifier" /></td><td><code>string</code></td><td>The property describes a subnet group identifier for the instance profile.</td></tr>
<tr><td><CopyableCode code="vpc_security_groups" /></td><td><code>array</code></td><td>The property describes vps security groups for the instance profile.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
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
FROM aws.dms.instance_profile
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

