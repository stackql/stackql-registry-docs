---
title: clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters
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


Used to retrieve a list of <code>clusters</code> in a region or to create or delete a <code>clusters</code> resource, use <code>cluster</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An object representing an Amazon EKS cluster.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.eks.clusters" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The unique name to give to your cluster.</td></tr>
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
name
FROM aws.eks.clusters
WHERE region = 'us-east-1';
```

## `INSERT` Example

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
    ]
}>
<TabItem value="required">

```sql
<<<json
{
 "ResourcesVpcConfig": {
  "EndpointPrivateAccess": "{{ EndpointPrivateAccess }}",
  "EndpointPublicAccess": "{{ EndpointPublicAccess }}",
  "PublicAccessCidrs": [
   "{{ PublicAccessCidrs[0] }}"
  ],
  "SecurityGroupIds": [
   "{{ SecurityGroupIds[0] }}"
  ],
  "SubnetIds": [
   "{{ SubnetIds[0] }}"
  ]
 },
 "RoleArn": "{{ RoleArn }}"
}
>>>
--required properties only
INSERT INTO aws.eks.clusters (
 ResourcesVpcConfig,
 RoleArn,
 region
)
SELECT 
{{ .ResourcesVpcConfig }},
 {{ .RoleArn }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "EncryptionConfig": [
  {
   "Provider": {
    "KeyArn": "{{ KeyArn }}"
   },
   "Resources": [
    "{{ Resources[0] }}"
   ]
  }
 ],
 "KubernetesNetworkConfig": {
  "ServiceIpv4Cidr": "{{ ServiceIpv4Cidr }}",
  "ServiceIpv6Cidr": "{{ ServiceIpv6Cidr }}",
  "IpFamily": "{{ IpFamily }}"
 },
 "Logging": {
  "ClusterLogging": {
   "EnabledTypes": [
    {
     "Type": "{{ Type }}"
    }
   ]
  }
 },
 "Name": "{{ Name }}",
 "ResourcesVpcConfig": {
  "EndpointPrivateAccess": "{{ EndpointPrivateAccess }}",
  "EndpointPublicAccess": "{{ EndpointPublicAccess }}",
  "PublicAccessCidrs": [
   "{{ PublicAccessCidrs[0] }}"
  ],
  "SecurityGroupIds": [
   "{{ SecurityGroupIds[0] }}"
  ],
  "SubnetIds": [
   "{{ SubnetIds[0] }}"
  ]
 },
 "OutpostConfig": {
  "OutpostArns": [
   "{{ OutpostArns[0] }}"
  ],
  "ControlPlaneInstanceType": "{{ ControlPlaneInstanceType }}",
  "ControlPlanePlacement": {
   "GroupName": "{{ GroupName }}"
  }
 },
 "AccessConfig": {
  "BootstrapClusterCreatorAdminPermissions": "{{ BootstrapClusterCreatorAdminPermissions }}",
  "AuthenticationMode": "{{ AuthenticationMode }}"
 },
 "RoleArn": "{{ RoleArn }}",
 "Version": "{{ Version }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.eks.clusters (
 EncryptionConfig,
 KubernetesNetworkConfig,
 Logging,
 Name,
 ResourcesVpcConfig,
 OutpostConfig,
 AccessConfig,
 RoleArn,
 Version,
 Tags,
 region
)
SELECT 
 {{ .EncryptionConfig }},
 {{ .KubernetesNetworkConfig }},
 {{ .Logging }},
 {{ .Name }},
 {{ .ResourcesVpcConfig }},
 {{ .OutpostConfig }},
 {{ .AccessConfig }},
 {{ .RoleArn }},
 {{ .Version }},
 {{ .Tags }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.eks.clusters
WHERE data__Identifier = '<Name>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>clusters</code> resource, the following permissions are required:

### Create
```json
eks:CreateCluster,
eks:DescribeCluster,
eks:TagResource,
iam:PassRole,
iam:GetRole,
iam:ListAttachedRolePolicies,
iam:CreateServiceLinkedRole,
iam:CreateInstanceProfile,
iam:TagInstanceProfile,
iam:AddRoleToInstanceProfile,
iam:GetInstanceProfile,
iam:DeleteInstanceProfile,
iam:RemoveRoleFromInstanceProfile,
ec2:DescribeSubnets,
ec2:DescribeVpcs,
kms:DescribeKey,
kms:CreateGrant
```

### Delete
```json
eks:DeleteCluster,
eks:DescribeCluster
```

### List
```json
eks:ListClusters
```

