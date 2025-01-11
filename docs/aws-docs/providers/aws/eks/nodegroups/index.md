---
title: nodegroups
hide_title: false
hide_table_of_contents: false
keywords:
  - nodegroups
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

Creates, updates, deletes or gets a <code>nodegroup</code> resource or lists <code>nodegroups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>nodegroups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::EKS::Nodegroup</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.eks.nodegroups" /></td></tr>
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
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td>The metadata, as key-value pairs, to apply to the node group to assist with categorization and organization. Follows same schema as Labels for consistency.</td></tr>
<tr><td><CopyableCode code="taints" /></td><td><code>array</code></td><td>The Kubernetes taints to be applied to the nodes in the node group when they are created.</td></tr>
<tr><td><CopyableCode code="update_config" /></td><td><code>object</code></td><td>The node group update configuration.</td></tr>
<tr><td><CopyableCode code="node_repair_config" /></td><td><code>object</code></td><td>The node auto repair configuration for node group.</td></tr>
<tr><td><CopyableCode code="version" /></td><td><code>string</code></td><td>The Kubernetes version to use for your managed nodes.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-nodegroup.html"><code>AWS::EKS::Nodegroup</code></a>.

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
    <td><CopyableCode code="ClusterName, NodeRole, Subnets, region" /></td>
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
Gets all <code>nodegroups</code> in a region.
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
node_repair_config,
version,
id,
arn
FROM aws.eks.nodegroups
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>nodegroup</code>.
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
node_repair_config,
version,
id,
arn
FROM aws.eks.nodegroups
WHERE region = 'us-east-1' AND data__Identifier = '<Id>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>nodegroup</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.eks.nodegroups (
 ClusterName,
 NodeRole,
 Subnets,
 region
)
SELECT 
'{{ ClusterName }}',
 '{{ NodeRole }}',
 '{{ Subnets }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.eks.nodegroups (
 AmiType,
 CapacityType,
 ClusterName,
 DiskSize,
 ForceUpdateEnabled,
 InstanceTypes,
 Labels,
 LaunchTemplate,
 NodegroupName,
 NodeRole,
 ReleaseVersion,
 RemoteAccess,
 ScalingConfig,
 Subnets,
 Tags,
 Taints,
 UpdateConfig,
 NodeRepairConfig,
 Version,
 region
)
SELECT 
 '{{ AmiType }}',
 '{{ CapacityType }}',
 '{{ ClusterName }}',
 '{{ DiskSize }}',
 '{{ ForceUpdateEnabled }}',
 '{{ InstanceTypes }}',
 '{{ Labels }}',
 '{{ LaunchTemplate }}',
 '{{ NodegroupName }}',
 '{{ NodeRole }}',
 '{{ ReleaseVersion }}',
 '{{ RemoteAccess }}',
 '{{ ScalingConfig }}',
 '{{ Subnets }}',
 '{{ Tags }}',
 '{{ Taints }}',
 '{{ UpdateConfig }}',
 '{{ NodeRepairConfig }}',
 '{{ Version }}',
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
  - name: nodegroup
    props:
      - name: AmiType
        value: '{{ AmiType }}'
      - name: CapacityType
        value: '{{ CapacityType }}'
      - name: ClusterName
        value: '{{ ClusterName }}'
      - name: DiskSize
        value: '{{ DiskSize }}'
      - name: ForceUpdateEnabled
        value: '{{ ForceUpdateEnabled }}'
      - name: InstanceTypes
        value:
          - '{{ InstanceTypes[0] }}'
      - name: Labels
        value: {}
      - name: LaunchTemplate
        value:
          Id: '{{ Id }}'
          Version: '{{ Version }}'
          Name: '{{ Name }}'
      - name: NodegroupName
        value: '{{ NodegroupName }}'
      - name: NodeRole
        value: '{{ NodeRole }}'
      - name: ReleaseVersion
        value: '{{ ReleaseVersion }}'
      - name: RemoteAccess
        value:
          SourceSecurityGroups:
            - '{{ SourceSecurityGroups[0] }}'
          Ec2SshKey: '{{ Ec2SshKey }}'
      - name: ScalingConfig
        value:
          MinSize: '{{ MinSize }}'
          DesiredSize: '{{ DesiredSize }}'
          MaxSize: '{{ MaxSize }}'
      - name: Subnets
        value:
          - '{{ Subnets[0] }}'
      - name: Tags
        value: {}
      - name: Taints
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
            Effect: '{{ Effect }}'
      - name: UpdateConfig
        value:
          MaxUnavailable: null
          MaxUnavailablePercentage: null
      - name: NodeRepairConfig
        value:
          Enabled: '{{ Enabled }}'
      - name: Version
        value: '{{ Version }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.eks.nodegroups
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>nodegroups</code> resource, the following permissions are required:

### Create
```json
eks:CreateNodegroup,
eks:DescribeNodegroup,
eks:TagResource,
ec2:DescribeSubnets,
ec2:DescribeVpcs,
ec2:DescribeSecurityGroups,
ec2:DescribeKeyPairs,
ec2:CreateTags,
ec2:DeleteTags,
ec2:DescribeRouteTables,
ec2:DescribeLaunchTemplates,
ec2:DescribeLaunchTemplateVersions,
ec2:RunInstances,
iam:CreateServiceLinkedRole,
iam:GetRole,
iam:PassRole,
iam:ListAttachedRolePolicies
```

### Read
```json
eks:DescribeNodegroup
```

### Delete
```json
eks:DeleteNodegroup,
eks:DescribeNodegroup
```

### List
```json
eks:ListNodegroups
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
