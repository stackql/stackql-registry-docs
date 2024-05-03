---
title: vpc_endpoint
hide_title: false
hide_table_of_contents: false
keywords:
  - vpc_endpoint
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

Gets or operates on an individual <code>vpc_endpoint</code> resource, use <code>vpc_endpoints</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpc_endpoint</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Amazon OpenSearchServerless vpc endpoint resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.opensearchserverless.vpc_endpoint" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The identifier of the VPC Endpoint</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the VPC Endpoint</td></tr>
<tr><td><CopyableCode code="security_group_ids" /></td><td><code>array</code></td><td>The ID of one or more security groups to associate with the endpoint network interface</td></tr>
<tr><td><CopyableCode code="subnet_ids" /></td><td><code>array</code></td><td>The ID of one or more subnets in which to create an endpoint network interface</td></tr>
<tr><td><CopyableCode code="vpc_id" /></td><td><code>string</code></td><td>The ID of the VPC in which the endpoint will be used.</td></tr>
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
id,
name,
security_group_ids,
subnet_ids,
vpc_id
FROM aws.opensearchserverless.vpc_endpoint
WHERE data__Identifier = '<Id>';
```

## Permissions

To operate on the <code>vpc_endpoint</code> resource, the following permissions are required:

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

