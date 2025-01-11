---
title: compute_node_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - compute_node_groups
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

Creates, updates, deletes or gets a <code>compute_node_group</code> resource or lists <code>compute_node_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>compute_node_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>AWS::PCS::ComputeNodeGroup resource creates an AWS PCS compute node group.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.pcs.compute_node_groups" /></td></tr>
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
<tr><td><CopyableCode code="tags" /></td><td><code></code></td><td>1 or more tags added to the resource. Each tag consists of a tag key and tag value. The tag value is optional and can be an empty string.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcs-computenodegroup.html"><code>AWS::PCS::ComputeNodeGroup</code></a>.

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="ClusterId, CustomLaunchTemplate, IamInstanceProfileArn, InstanceConfigs, ScalingConfiguration, SubnetIds, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Gets all <code>compute_node_groups</code> in a region.
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
tags
FROM aws.pcs.compute_node_groups
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>compute_node_group</code>.
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
tags
FROM aws.pcs.compute_node_groups
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>compute_node_group</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
/*+ create */
INSERT INTO aws.pcs.compute_node_groups (
 ClusterId,
 CustomLaunchTemplate,
 IamInstanceProfileArn,
 InstanceConfigs,
 ScalingConfiguration,
 SubnetIds,
 region
)
SELECT 
'{{ ClusterId }}',
 '{{ CustomLaunchTemplate }}',
 '{{ IamInstanceProfileArn }}',
 '{{ InstanceConfigs }}',
 '{{ ScalingConfiguration }}',
 '{{ SubnetIds }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.pcs.compute_node_groups (
 AmiId,
 ClusterId,
 CustomLaunchTemplate,
 IamInstanceProfileArn,
 InstanceConfigs,
 Name,
 PurchaseOption,
 ScalingConfiguration,
 SlurmConfiguration,
 SpotOptions,
 SubnetIds,
 Tags,
 region
)
SELECT 
 '{{ AmiId }}',
 '{{ ClusterId }}',
 '{{ CustomLaunchTemplate }}',
 '{{ IamInstanceProfileArn }}',
 '{{ InstanceConfigs }}',
 '{{ Name }}',
 '{{ PurchaseOption }}',
 '{{ ScalingConfiguration }}',
 '{{ SlurmConfiguration }}',
 '{{ SpotOptions }}',
 '{{ SubnetIds }}',
 '{{ Tags }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: compute_node_group
    props:
      - name: AmiId
        value: '{{ AmiId }}'
      - name: ClusterId
        value: '{{ ClusterId }}'
      - name: CustomLaunchTemplate
        value:
          Id: '{{ Id }}'
          Version: '{{ Version }}'
      - name: IamInstanceProfileArn
        value: '{{ IamInstanceProfileArn }}'
      - name: InstanceConfigs
        value:
          - InstanceType: '{{ InstanceType }}'
      - name: Name
        value: '{{ Name }}'
      - name: PurchaseOption
        value: '{{ PurchaseOption }}'
      - name: ScalingConfiguration
        value:
          MaxInstanceCount: '{{ MaxInstanceCount }}'
          MinInstanceCount: '{{ MinInstanceCount }}'
      - name: SlurmConfiguration
        value:
          SlurmCustomSettings:
            - ParameterName: '{{ ParameterName }}'
              ParameterValue: '{{ ParameterValue }}'
      - name: SpotOptions
        value:
          AllocationStrategy: '{{ AllocationStrategy }}'
      - name: SubnetIds
        value:
          - '{{ SubnetIds[0] }}'
      - name: Tags
        value: null

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.pcs.compute_node_groups
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>compute_node_groups</code> resource, the following permissions are required:

### Create
```json
ec2:DescribeImages,
ec2:DescribeVpcs,
ec2:DescribeSubnets,
ec2:DescribeSecurityGroups,
ec2:DescribeLaunchTemplates,
ec2:DescribeLaunchTemplateVersions,
ec2:DescribeInstanceTypes,
ec2:DescribeInstanceTypeOfferings,
ec2:RunInstances,
ec2:CreateFleet,
ec2:CreateTags,
iam:PassRole,
iam:GetInstanceProfile,
pcs:CreateComputeNodeGroup,
pcs:GetComputeNodeGroup,
pcs:ListTagsForResource,
pcs:TagResource
```

### Read
```json
pcs:GetComputeNodeGroup,
pcs:ListTagsForResource
```

### Update
```json
ec2:DescribeImages,
ec2:DescribeVpcs,
ec2:DescribeSubnets,
ec2:DescribeSecurityGroups,
ec2:DescribeLaunchTemplates,
ec2:DescribeLaunchTemplateVersions,
ec2:DescribeInstanceTypes,
ec2:DescribeInstanceTypeOfferings,
ec2:RunInstances,
ec2:CreateFleet,
ec2:CreateTags,
iam:PassRole,
iam:GetInstanceProfile,
pcs:GetComputeNodeGroup,
pcs:UpdateComputeNodeGroup,
pcs:ListTagsForResource,
pcs:TagResource,
pcs:UntagResource
```

### Delete
```json
ec2:DescribeImages,
ec2:DescribeVpcs,
ec2:DescribeSubnets,
ec2:DescribeSecurityGroups,
ec2:DescribeLaunchTemplates,
ec2:DescribeLaunchTemplateVersions,
ec2:DescribeInstanceTypes,
ec2:DescribeInstanceTypeOfferings,
ec2:TerminateInstances,
ec2:CreateFleet,
ec2:CreateTags,
iam:PassRole,
iam:GetInstanceProfile,
pcs:GetComputeNodeGroup,
pcs:DeleteComputeNodeGroup,
pcs:ListTagsForResource,
pcs:TagResource,
pcs:UntagResource
```

### List
```json
pcs:ListClusters,
pcs:ListComputeNodeGroups
```
