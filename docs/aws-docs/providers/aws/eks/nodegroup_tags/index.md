---
title: nodegroup_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - nodegroup_tags
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Expands all tag keys and values for <code>nodegroups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>nodegroup_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::EKS::Nodegroup</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.eks.nodegroup_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="ami_type" /></td><td><code>string</code></td><td>The AMI type for your node group.</td></tr>
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
<tr><td><CopyableCode code="taints" /></td><td><code>array</code></td><td>The Kubernetes taints to be applied to the nodes in the node group when they are created.</td></tr>
<tr><td><CopyableCode code="update_config" /></td><td><code>object</code></td><td>The node group update configuration.</td></tr>
<tr><td><CopyableCode code="version" /></td><td><code>string</code></td><td>The Kubernetes version to use for your managed nodes.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tag_key" /></td><td><code>string</code></td><td>Tag key.</td></tr>
<tr><td><CopyableCode code="tag_value" /></td><td><code>string</code></td><td>Tag value.</td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Expands tags for all <code>nodegroups</code> in a region.
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
taints,
update_config,
version,
id,
arn,
tag_key,
tag_value
FROM aws.eks.nodegroup_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>nodegroup_tags</code> resource, see <a href="/providers/aws/eks/nodegroups/#permissions"><code>nodegroups</code></a>


