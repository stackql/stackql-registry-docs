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


Used to retrieve a list of <code>nodegroups</code> in a region or to create or delete a <code>nodegroups</code> resource, use <code>nodegroup</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>nodegroups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::EKS::Nodegroup</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.eks.nodegroups" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
id
FROM aws.eks.nodegroups
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>nodegroup</code> resource, using <a ref="https://pypi.org/project/stack-deploy/" target="_blank"><code><b>stack-deploy</b></code></a>.

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
-- nodegroup.iql (required properties only)
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
-- nodegroup.iql (all properties)
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
      - name: Version
        value: '{{ Version }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
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

### Delete
```json
eks:DeleteNodegroup,
eks:DescribeNodegroup
```

### List
```json
eks:ListNodegroups
```

