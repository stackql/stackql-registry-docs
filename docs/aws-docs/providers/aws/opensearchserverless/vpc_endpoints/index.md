---
title: vpc_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - vpc_endpoints
  - opensearchserverless
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

Creates, updates, deletes or gets a <code>vpc_endpoint</code> resource or lists <code>vpc_endpoints</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpc_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Amazon OpenSearchServerless vpc endpoint resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.opensearchserverless.vpc_endpoints" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The identifier of the VPC Endpoint</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the VPC Endpoint</td></tr>
<tr><td><CopyableCode code="security_group_ids" /></td><td><code>array</code></td><td>The ID of one or more security groups to associate with the endpoint network interface</td></tr>
<tr><td><CopyableCode code="subnet_ids" /></td><td><code>array</code></td><td>The ID of one or more subnets in which to create an endpoint network interface</td></tr>
<tr><td><CopyableCode code="vpc_id" /></td><td><code>string</code></td><td>The ID of the VPC in which the endpoint will be used.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchserverless-vpcendpoint.html"><code>AWS::OpenSearchServerless::VpcEndpoint</code></a>.

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
    <td><CopyableCode code="Name, VpcId, SubnetIds, region" /></td>
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
Gets all <code>vpc_endpoints</code> in a region.
```sql
SELECT
region,
id,
name,
security_group_ids,
subnet_ids,
vpc_id
FROM aws.opensearchserverless.vpc_endpoints
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>vpc_endpoint</code>.
```sql
SELECT
region,
id,
name,
security_group_ids,
subnet_ids,
vpc_id
FROM aws.opensearchserverless.vpc_endpoints
WHERE region = 'us-east-1' AND data__Identifier = '<Id>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>vpc_endpoint</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.opensearchserverless.vpc_endpoints (
 Name,
 SubnetIds,
 VpcId,
 region
)
SELECT 
'{{ Name }}',
 '{{ SubnetIds }}',
 '{{ VpcId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.opensearchserverless.vpc_endpoints (
 Name,
 SecurityGroupIds,
 SubnetIds,
 VpcId,
 region
)
SELECT 
 '{{ Name }}',
 '{{ SecurityGroupIds }}',
 '{{ SubnetIds }}',
 '{{ VpcId }}',
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
  - name: vpc_endpoint
    props:
      - name: Name
        value: '{{ Name }}'
      - name: SecurityGroupIds
        value:
          - '{{ SecurityGroupIds[0] }}'
      - name: SubnetIds
        value:
          - '{{ SubnetIds[0] }}'
      - name: VpcId
        value: '{{ VpcId }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.opensearchserverless.vpc_endpoints
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>vpc_endpoints</code> resource, the following permissions are required:

### Create
```json
aoss:BatchGetVpcEndpoint,
aoss:CreateVpcEndpoint,
ec2:CreateVpcEndpoint,
ec2:DeleteVpcEndPoints,
ec2:DescribeVpcEndpoints,
ec2:ModifyVpcEndPoint,
ec2:DescribeVpcs,
ec2:DescribeSubnets,
ec2:DescribeSecurityGroups,
ec2:CreateTags,
route53:ChangeResourceRecordSets,
route53:GetChange,
route53:GetHostedZone,
route53:ListResourceRecordSets,
route53:ListHostedZonesByName,
route53:CreateHostedZone,
route53:ListHostedZonesByVPC,
route53:AssociateVPCWithHostedZone
```

### Read
```json
aoss:BatchGetVpcEndpoint,
ec2:DescribeVpcEndpoints
```

### Update
```json
aoss:BatchGetVpcEndpoint,
aoss:UpdateVpcEndpoint,
ec2:CreateVpcEndpoint,
ec2:DeleteVpcEndPoints,
ec2:DescribeVpcEndpoints,
ec2:ModifyVpcEndPoint,
ec2:DescribeVpcs,
ec2:DescribeSubnets,
ec2:DescribeSecurityGroups,
ec2:CreateTags,
route53:ChangeResourceRecordSets,
route53:GetChange,
route53:GetHostedZone,
route53:ListResourceRecordSets,
route53:ListHostedZonesByName,
route53:CreateHostedZone,
route53:ListHostedZonesByVPC,
route53:AssociateVPCWithHostedZone
```

### Delete
```json
aoss:BatchGetVpcEndpoint,
aoss:DeleteVpcEndpoint,
ec2:DeleteVpcEndPoints,
ec2:DescribeVpcEndpoints,
ec2:ModifyVpcEndPoint,
ec2:DescribeVpcs,
ec2:DescribeSubnets,
ec2:DescribeSecurityGroups,
ec2:CreateTags,
route53:ChangeResourceRecordSets,
route53:DeleteHostedZone,
route53:GetChange,
route53:GetHostedZone,
route53:ListResourceRecordSets,
route53:ListHostedZonesByName,
route53:ListHostedZonesByVPC,
route53:AssociateVPCWithHostedZone
```

### List
```json
aoss:ListVpcEndpoints,
ec2:DescribeVpcEndpoints
```
