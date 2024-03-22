---
title: vpc_endpoint_service_permissions
hide_title: false
hide_table_of_contents: false
keywords:
  - vpc_endpoint_service_permissions
  - ec2
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>vpc_endpoint_service_permissions</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpc_endpoint_service_permissions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>vpc_endpoint_service_permissions</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.ec2.vpc_endpoint_service_permissions</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>allowed_principals</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>service_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
allowed_principals,
service_id
FROM awscc.ec2.vpc_endpoint_service_permissions
WHERE data__Identifier = '<ServiceId>';
```

## Permissions

To operate on the <code>vpc_endpoint_service_permissions</code> resource, the following permissions are required:

### Update
```json
ec2:CreateVpcEndpointServicePermissions,
ec2:ModifyVpcEndpointServicePermissions,
ec2:DeleteVpcEndpointServicePermissions,
ec2:DescribeVpcEndpointServicePermissions
```

### Read
```json
ec2:CreateVpcEndpointServicePermissions,
ec2:ModifyVpcEndpointServicePermissions,
ec2:DeleteVpcEndpointServicePermissions,
ec2:DescribeVpcEndpointServicePermissions
```

### Delete
```json
ec2:CreateVpcEndpointServicePermissions,
ec2:ModifyVpcEndpointServicePermissions,
ec2:DeleteVpcEndpointServicePermissions,
ec2:DescribeVpcEndpointServicePermissions
```

