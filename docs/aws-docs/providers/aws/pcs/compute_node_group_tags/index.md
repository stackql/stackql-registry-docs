---
title: compute_node_group_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - compute_node_group_tags
  - pcs
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

Expands all tag keys and values for <code>compute_node_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>compute_node_group_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>AWS::PCS::ComputeNodeGroup resource creates an AWS PCS compute node group.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.pcs.compute_node_group_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="ami_id" /></td><td><code>string</code></td><td>The ID of the Amazon Machine Image (AMI) that AWS PCS uses to launch instances. If not provided, AWS PCS uses the AMI ID specified in the custom launch template.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The unique Amazon Resource Name (ARN) of the compute node group.</td></tr>
<tr><td><CopyableCode code="cluster_id" /></td><td><code>string</code></td><td>The ID of the cluster of the compute node group.</td></tr>
<tr><td><CopyableCode code="custom_launch_template" /></td><td><code>object</code></td><td>An Amazon EC2 launch template AWS PCS uses to launch compute nodes.</td></tr>
<tr><td><CopyableCode code="error_info" /></td><td><code>array</code></td><td>The list of errors that occurred during compute node group provisioning.</td></tr>
<tr><td><CopyableCode code="iam_instance_profile_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the IAM instance profile used to pass an IAM role when launching EC2 instances. The role contained in your instance profile must have pcs:RegisterComputeNodeGroupInstance permissions attached to provision instances correctly.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The generated unique ID of the compute node group.</td></tr>
<tr><td><CopyableCode code="instance_configs" /></td><td><code>array</code></td><td>A list of EC2 instance configurations that AWS PCS can provision in the compute node group.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name that identifies the compute node group.</td></tr>
<tr><td><CopyableCode code="purchase_option" /></td><td><code>string</code></td><td>Specifies how EC2 instances are purchased on your behalf. AWS PCS supports On-Demand and Spot instances. For more information, see Instance purchasing options in the Amazon Elastic Compute Cloud User Guide. If you don't provide this option, it defaults to On-Demand.</td></tr>
<tr><td><CopyableCode code="scaling_configuration" /></td><td><code>object</code></td><td>Specifies the boundaries of the compute node group auto scaling.</td></tr>
<tr><td><CopyableCode code="slurm_configuration" /></td><td><code>object</code></td><td>Additional options related to the Slurm scheduler.</td></tr>
<tr><td><CopyableCode code="spot_options" /></td><td><code>object</code></td><td>Additional configuration when you specify SPOT as the purchase option.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>The provisioning status of the compute node group. The provisioning status doesn't indicate the overall health of the compute node group.</td></tr>
<tr><td><CopyableCode code="subnet_ids" /></td><td><code>array</code></td><td>The list of subnet IDs where instances are provisioned by the compute node group. The subnets must be in the same VPC as the cluster.</td></tr>
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
Expands tags for all <code>compute_node_groups</code> in a region.
```sql
SELECT
region,
ami_id,
arn,
cluster_id,
custom_launch_template,
error_info,
iam_instance_profile_arn,
id,
instance_configs,
name,
purchase_option,
scaling_configuration,
slurm_configuration,
spot_options,
status,
subnet_ids,
tag_key,
tag_value
FROM aws.pcs.compute_node_group_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>compute_node_group_tags</code> resource, see <a href="/providers/aws/pcs/compute_node_groups/#permissions"><code>compute_node_groups</code></a>

