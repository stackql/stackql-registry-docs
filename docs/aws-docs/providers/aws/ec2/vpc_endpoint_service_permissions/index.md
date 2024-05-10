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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Gets or updates an individual <code>vpc_endpoint_service_permissions</code> resource, use <code>vpc_endpoint_service_permissions</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpc_endpoint_service_permissions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EC2::VPCEndpointServicePermissions</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.vpc_endpoint_service_permissions" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="allowed_principals" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="service_id" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
allowed_principals,
service_id
FROM aws.ec2.vpc_endpoint_service_permissions
WHERE region = 'us-east-1' AND data__Identifier = '<ServiceId>';
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

