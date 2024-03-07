---
title: vpc_ingress_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - vpc_ingress_connections
  - apprunner
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>vpc_ingress_connections</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpc_ingress_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>vpc_ingress_connections</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.apprunner.vpc_ingress_connections</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>vpc_ingress_connection_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the VpcIngressConnection.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
vpc_ingress_connection_arn
FROM awscc.apprunner.vpc_ingress_connections
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>vpc_ingress_connections</code> resource, the following permissions are required:

### Create
```json
apprunner:CreateVpcIngressConnection,
apprunner:DescribeVpcIngressConnection,
ec2:DescribeVpcs,
ec2:DescribeVpcEndpoints,
ec2:DescribeSubnets,
apprunner:TagResource
```

### List
```json
apprunner:ListVpcIngressConnections
```

