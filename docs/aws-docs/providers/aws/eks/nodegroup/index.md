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
Gets an individual <code>nodegroup</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>nodegroup</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>nodegroup</td></tr>
<tr><td><b>Id</b></td><td><code>aws.eks.nodegroup</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>ami_type</code></td><td><code>string</code></td><td>The AMI type for your node group.</td></tr>
<tr><td><code>capacity_type</code></td><td><code>string</code></td><td>The capacity type of your managed node group.</td></tr>
<tr><td><code>cluster_name</code></td><td><code>string</code></td><td>Name of the cluster to create the node group in.</td></tr>
<tr><td><code>disk_size</code></td><td><code>integer</code></td><td>The root device disk size (in GiB) for your node group instances.</td></tr>
<tr><td><code>force_update_enabled</code></td><td><code>boolean</code></td><td>Force the update if the existing node group's pods are unable to be drained due to a pod disruption budget issue.</td></tr>
<tr><td><code>instance_types</code></td><td><code>array</code></td><td>Specify the instance types for a node group.</td></tr>
<tr><td><code>labels</code></td><td><code>object</code></td><td>The Kubernetes labels to be applied to the nodes in the node group when they are created.</td></tr>
<tr><td><code>launch_template</code></td><td><code>object</code></td><td>An object representing a node group's launch template specification.</td></tr>
<tr><td><code>nodegroup_name</code></td><td><code>string</code></td><td>The unique name to give your node group.</td></tr>
<tr><td><code>node_role</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the IAM role to associate with your node group.</td></tr>
<tr><td><code>release_version</code></td><td><code>string</code></td><td>The AMI version of the Amazon EKS-optimized AMI to use with your node group.</td></tr>
<tr><td><code>remote_access</code></td><td><code>object</code></td><td>The remote access (SSH) configuration to use with your node group.</td></tr>
<tr><td><code>scaling_config</code></td><td><code>object</code></td><td>The scaling configuration details for the Auto Scaling group that is created for your node group.</td></tr>
<tr><td><code>subnets</code></td><td><code>array</code></td><td>The subnets to use for the Auto Scaling group that is created for your node group.</td></tr>
<tr><td><code>tags</code></td><td><code>object</code></td><td>The metadata, as key-value pairs, to apply to the node group to assist with categorization and organization. Follows same schema as Labels for consistency.</td></tr>
<tr><td><code>taints</code></td><td><code>array</code></td><td>The Kubernetes taints to be applied to the nodes in the node group when they are created.</td></tr>
<tr><td><code>update_config</code></td><td><code>object</code></td><td>The node group update configuration.</td></tr>
<tr><td><code>version</code></td><td><code>string</code></td><td>The Kubernetes version to use for your managed nodes.</td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
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
WHERE region = 'us-east-1'
AND data__Identifier = '<Id>'
```
