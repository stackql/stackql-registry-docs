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

Creates, updates, deletes or gets a <code>cluster</code> resource or lists <code>clusters</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An object representing an Amazon EKS cluster.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.eks.clusters" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="logging" /></td><td><code>object</code></td><td>Enable exporting the Kubernetes control plane logs for your cluster to CloudWatch Logs based on log types. By default, cluster control plane logs aren't exported to CloudWatch Logs.</td></tr>
<tr><td><CopyableCode code="encryption_config_key_arn" /></td><td><code>string</code></td><td>Amazon Resource Name (ARN) or alias of the customer master key (CMK).</td></tr>
<tr><td><CopyableCode code="access_config" /></td><td><code>object</code></td><td>An object representing the Access Config to use for the cluster.</td></tr>
<tr><td><CopyableCode code="certificate_authority_data" /></td><td><code>string</code></td><td>The certificate-authority-data for your cluster.</td></tr>
<tr><td><CopyableCode code="encryption_config" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="kubernetes_network_config" /></td><td><code>object</code></td><td>The Kubernetes network configuration for the cluster.</td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the IAM role that provides permissions for the Kubernetes control plane to make calls to AWS API operations on your behalf.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The unique name to give to your cluster.</td></tr>
<tr><td><CopyableCode code="endpoint" /></td><td><code>string</code></td><td>The endpoint for your Kubernetes API server, such as https://5E1D0CEXAMPLEA591B746AFC5AB30262.yl4.us-west-2.eks.amazonaws.com.</td></tr>
<tr><td><CopyableCode code="version" /></td><td><code>string</code></td><td>The desired Kubernetes version for your cluster. If you don't specify a value here, the latest version available in Amazon EKS is used.</td></tr>
<tr><td><CopyableCode code="cluster_security_group_id" /></td><td><code>string</code></td><td>The cluster security group that was created by Amazon EKS for the cluster. Managed node groups use this security group for control plane to data plane communication.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The unique ID given to your cluster.</td></tr>
<tr><td><CopyableCode code="outpost_config" /></td><td><code>object</code></td><td>An object representing the Outpost configuration to use for AWS EKS outpost cluster.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The ARN of the cluster, such as arn:aws:eks:us-west-2:666666666666:cluster/prod.</td></tr>
<tr><td><CopyableCode code="resources_vpc_config" /></td><td><code>object</code></td><td>An object representing the VPC configuration to use for an Amazon EKS cluster.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="open_id_connect_issuer_url" /></td><td><code>string</code></td><td>The issuer URL for the cluster's OIDC identity provider, such as https://oidc.eks.us-west-2.amazonaws.com/id/EXAMPLED539D4633E53DE1B716D3041E. If you need to remove https:// from this output value, you can include the following code in your template.</td></tr>
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
    <td><CopyableCode code="RoleArn, ResourcesVpcConfig, region" /></td>
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
    <td><CopyableCode code="list_resource" /></td>
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
List all <code>clusters</code> in a region.
```sql
SELECT
region,
name
FROM aws.eks.clusters
WHERE region = 'us-east-1';
```
Gets all properties from a <code>cluster</code>.
```sql
SELECT
region,
logging,
encryption_config_key_arn,
access_config,
certificate_authority_data,
encryption_config,
kubernetes_network_config,
role_arn,
name,
endpoint,
version,
cluster_security_group_id,
id,
outpost_config,
arn,
resources_vpc_config,
tags,
open_id_connect_issuer_url
FROM aws.eks.clusters
WHERE region = 'us-east-1' AND data__Identifier = '<Name>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>cluster</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.eks.clusters (
 RoleArn,
 ResourcesVpcConfig,
 region
)
SELECT 
'{{ RoleArn }}',
 '{{ ResourcesVpcConfig }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.eks.clusters (
 Logging,
 AccessConfig,
 EncryptionConfig,
 KubernetesNetworkConfig,
 RoleArn,
 Name,
 Version,
 OutpostConfig,
 ResourcesVpcConfig,
 Tags,
 region
)
SELECT 
 '{{ Logging }}',
 '{{ AccessConfig }}',
 '{{ EncryptionConfig }}',
 '{{ KubernetesNetworkConfig }}',
 '{{ RoleArn }}',
 '{{ Name }}',
 '{{ Version }}',
 '{{ OutpostConfig }}',
 '{{ ResourcesVpcConfig }}',
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
  - name: cluster
    props:
      - name: Logging
        value:
          ClusterLogging:
            EnabledTypes:
              - Type: '{{ Type }}'
      - name: AccessConfig
        value:
          AuthenticationMode: '{{ AuthenticationMode }}'
          BootstrapClusterCreatorAdminPermissions: '{{ BootstrapClusterCreatorAdminPermissions }}'
      - name: EncryptionConfig
        value:
          - Resources:
              - '{{ Resources[0] }}'
            Provider:
              KeyArn: '{{ KeyArn }}'
      - name: KubernetesNetworkConfig
        value:
          ServiceIpv4Cidr: '{{ ServiceIpv4Cidr }}'
          ServiceIpv6Cidr: '{{ ServiceIpv6Cidr }}'
          IpFamily: '{{ IpFamily }}'
      - name: RoleArn
        value: '{{ RoleArn }}'
      - name: Name
        value: '{{ Name }}'
      - name: Version
        value: '{{ Version }}'
      - name: OutpostConfig
        value:
          OutpostArns:
            - '{{ OutpostArns[0] }}'
          ControlPlanePlacement:
            GroupName: '{{ GroupName }}'
          ControlPlaneInstanceType: '{{ ControlPlaneInstanceType }}'
      - name: ResourcesVpcConfig
        value:
          EndpointPublicAccess: '{{ EndpointPublicAccess }}'
          PublicAccessCidrs:
            - '{{ PublicAccessCidrs[0] }}'
          EndpointPrivateAccess: '{{ EndpointPrivateAccess }}'
          SecurityGroupIds:
            - '{{ SecurityGroupIds[0] }}'
          SubnetIds:
            - '{{ SubnetIds[0] }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.eks.clusters
WHERE data__Identifier = '<Name>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>clusters</code> resource, the following permissions are required:

### Read
```json
eks:DescribeCluster
```

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

### Update
```json
iam:PassRole,
eks:UpdateClusterConfig,
eks:UpdateClusterVersion,
eks:DescribeCluster,
eks:DescribeUpdate,
eks:TagResource,
eks:UntagResource
```

### List
```json
eks:ListClusters
```

### Delete
```json
eks:DeleteCluster,
eks:DescribeCluster
```

