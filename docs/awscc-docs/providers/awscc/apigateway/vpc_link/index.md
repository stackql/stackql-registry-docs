---
title: vpc_link
hide_title: false
hide_table_of_contents: false
keywords:
  - vpc_link
  - apigateway
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>vpc_link</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpc_link</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>vpc_link</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.apigateway.vpc_link</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>A name for the VPC link.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>A description of the VPC link.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of arbitrary tags (key-value pairs) to associate with the stage.</td></tr>
<tr><td><code>target_arns</code></td><td><code>array</code></td><td>The ARN of network load balancer of the VPC targeted by the VPC link. The network load balancer must be owned by the same AWS account of the API owner.</td></tr>
<tr><td><code>vpc_link_id</code></td><td><code>string</code></td><td>The ID of the instance that backs VPC link.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
name,
description,
tags,
target_arns,
vpc_link_id
FROM awscc.apigateway.vpc_link
WHERE region = 'us-east-1'
AND data__Identifier = '{VpcLinkId}';
```

## Permissions

To operate on the <code>vpc_link</code> resource, the following permissions are required:

### Update
```json
apigateway:PATCH,
apigateway:GET,
apigateway:PUT,
ec2:CreateVpcEndpointServiceConfiguration,
ec2:DeleteVpcEndpointServiceConfigurations,
ec2:DescribeVpcEndpointServiceConfigurations,
ec2:ModifyVpcEndpointServicePermissions
```

### Read
```json
apigateway:GET,
ec2:CreateVpcEndpointServiceConfiguration,
ec2:DeleteVpcEndpointServiceConfigurations,
ec2:DescribeVpcEndpointServiceConfigurations,
ec2:ModifyVpcEndpointServicePermissions
```

### Delete
```json
apigateway:GET,
apigateway:DELETE,
apigateway:PUT,
ec2:CreateVpcEndpointServiceConfiguration,
ec2:DeleteVpcEndpointServiceConfigurations,
ec2:DescribeVpcEndpointServiceConfigurations,
ec2:ModifyVpcEndpointServicePermissions
```

