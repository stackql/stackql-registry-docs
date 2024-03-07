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
Retrieves a list of <code>vpc_endpoints</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpc_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>vpc_endpoints</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.opensearchserverless.vpc_endpoints</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>The identifier of the VPC Endpoint</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>vpc_endpoints</code> resource, the following permissions are required:

### Create
<pre>
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
route53:AssociateVPCWithHostedZone</pre>

### List
<pre>
aoss:ListVpcEndpoints,
ec2:DescribeVpcEndpoints</pre>


## Example
```sql
SELECT
region,
id
FROM awscc.opensearchserverless.vpc_endpoints
WHERE region = 'us-east-1'
```
