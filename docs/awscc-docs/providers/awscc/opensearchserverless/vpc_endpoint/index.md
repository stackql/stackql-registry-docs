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
Gets an individual <code>vpc_endpoint</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpc_endpoint</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>vpc_endpoint</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.opensearchserverless.vpc_endpoint</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>The identifier of the VPC Endpoint</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the VPC Endpoint</td></tr>
<tr><td><code>security_group_ids</code></td><td><code>array</code></td><td>The ID of one or more security groups to associate with the endpoint network interface</td></tr>
<tr><td><code>subnet_ids</code></td><td><code>array</code></td><td>The ID of one or more subnets in which to create an endpoint network interface</td></tr>
<tr><td><code>vpc_id</code></td><td><code>string</code></td><td>The ID of the VPC in which the endpoint will be used.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

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


## Example
```sql
SELECT
region,
id,
name,
security_group_ids,
subnet_ids,
vpc_id
FROM awscc.opensearchserverless.vpc_endpoint
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```
