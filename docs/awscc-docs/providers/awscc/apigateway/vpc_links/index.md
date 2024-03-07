---
title: vpc_links
hide_title: false
hide_table_of_contents: false
keywords:
  - vpc_links
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
Retrieves a list of <code>vpc_links</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpc_links</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>vpc_links</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.apigateway.vpc_links</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>vpc_link_id</code></td><td><code>string</code></td><td>The ID of the instance that backs VPC link.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>vpc_links</code> resource, the following permissions are required:

### Create
```json
apigateway:POST,
apigateway:PUT,
apigateway:GET,
ec2:CreateVpcEndpointServiceConfiguration,
ec2:DeleteVpcEndpointServiceConfigurations,
ec2:DescribeVpcEndpointServiceConfigurations,
ec2:ModifyVpcEndpointServicePermissions
```

### List
```json
apigateway:GET,
ec2:CreateVpcEndpointServiceConfiguration,
ec2:DeleteVpcEndpointServiceConfigurations,
ec2:DescribeVpcEndpointServiceConfigurations,
ec2:ModifyVpcEndpointServicePermissions
```


## Example
```sql
SELECT
region,
vpc_link_id
FROM awscc.apigateway.vpc_links
WHERE region = 'us-east-1'
```
