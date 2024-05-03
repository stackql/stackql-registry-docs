---
title: nodegroup
hide_title: false
hide_table_of_contents: false
keywords:
  - nodegroup
  - eks
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

Gets or operates on an individual <code>nodegroup</code> resource, use <code>nodegroups</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>nodegroup</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::EKS::Nodegroup</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.eks.nodegroup" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="ami_type" /></td><td><code>string</code></td><td>The AMI type for your node group.</td></tr>
<tr><td><CopyableCode code="capacity_type" /></td><td><code>string</code></td><td>The capacity type of your managed node group.</td></tr>
<tr><td><CopyableCode code="cluster_name" /></td><td><code>string</code></td><td>Name of the cluster to create the node group in.</td></tr>
<tr><td><CopyableCode code="disk_size" /></td><td><code>integer</code></td><td>The root device disk size (in GiB) for your node group instances.</td></tr>
<tr><td><CopyableCode code="force_update_enabled" /></td><td><code>boolean</code></td><td>Force the update if the existing node group's pods are unable to be drained due to a pod disruption budget issue.</td></tr>
<tr><td><CopyableCode code="instance_types" /></td><td><code>array</code></td><td>Specify the instance types for a node group.</td></tr>
<tr><td><CopyableCode code="labels" /></td><td><code>object</code></td><td>The Kubernetes labels to be applied to the nodes in the node group when they are created.</td></tr>
<tr><td><CopyableCode code="launch_template" /></td><td><code>object</code></td><td>An object representing a node group's launch template specification.</td></tr>
<tr><td><CopyableCode code="nodegroup_name" /></td><td><code>string</code></td><td>The unique name to give your node group.</td></tr>
<tr><td><CopyableCode code="node_role" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the IAM role to associate with your node group.</td></tr>
<tr><td><CopyableCode code="release_version" /></td><td><code>string</code></td><td>The AMI version of the Amazon EKS-optimized AMI to use with your node group.</td></tr>
<tr><td><CopyableCode code="remote_access" /></td><td><code>object</code></td><td>The remote access (SSH) configuration to use with your node group.</td></tr>
<tr><td><CopyableCode code="scaling_config" /></td><td><code>object</code></td><td>The scaling configuration details for the Auto Scaling group that is created for your node group.</td></tr>
<tr><td><CopyableCode code="subnets" /></td><td><code>array</code></td><td>The subnets to use for the Auto Scaling group that is created for your node group.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td>The metadata, as key-value pairs, to apply to the node group to assist with categorization and organization. Follows same schema as Labels for consistency.</td></tr>
<tr><td><CopyableCode code="taints" /></td><td><code>array</code></td><td>The Kubernetes taints to be applied to the nodes in the node group when they are created.</td></tr>
<tr><td><CopyableCode code="update_config" /></td><td><code>object</code></td><td>The node group update configuration.</td></tr>
<tr><td><CopyableCode code="version" /></td><td><code>string</code></td><td>The Kubernetes version to use for your managed nodes.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
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
ami_type,
capacity_type,
cluster_name,
disk_size,
force_update_enabled,
instance_types,
labels,
launch_template,
nodegroup_name,
node_role,
release_version,
remote_access,
scaling_config,
subnets,
tags,
taints,
update_config,
version,
id,
arn
FROM aws.eks.nodegroup
WHERE data__Identifier = '<Id>';
```

## Permissions

To operate on the <code>nodegroup</code> resource, the following permissions are required:

### Read
```json
eks:DescribeNodegroup
```

### Delete
```json
eks:DeleteNodegroup,
eks:DescribeNodegroup
```

### Update
```json
iam:GetRole,
iam:PassRole,
eks:DescribeNodegroup,
eks:DescribeUpdate,
eks:ListUpdates,
eks:TagResource,
eks:UntagResource,
eks:UpdateNodegroupConfig,
eks:UpdateNodegroupVersion
```

