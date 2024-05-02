---
title: security_group
hide_title: false
hide_table_of_contents: false
keywords:
  - security_group
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
Gets an individual <code>security_group</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>security_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EC2::SecurityGroup</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.security_group</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>group_description</code></td><td><code>string</code></td><td>A description for the security group.</td></tr>
<tr><td><code>group_name</code></td><td><code>string</code></td><td>The name of the security group.</td></tr>
<tr><td><code>vpc_id</code></td><td><code>string</code></td><td>The ID of the VPC for the security group.</td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>The group name or group ID depending on whether the SG is created in default or specific VPC</td></tr>
<tr><td><code>security_group_ingress</code></td><td><code>array</code></td><td>The inbound rules associated with the security group. There is a short interruption during which you cannot connect to the security group.</td></tr>
<tr><td><code>security_group_egress</code></td><td><code>array</code></td><td>&#91;VPC only&#93; The outbound rules associated with the security group. There is a short interruption during which you cannot connect to the security group.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>Any tags assigned to the security group.</td></tr>
<tr><td><code>group_id</code></td><td><code>string</code></td><td>The group ID of the specified security group.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
group_description,
group_name,
vpc_id,
id,
security_group_ingress,
security_group_egress,
tags,
group_id
FROM aws.ec2.security_group
WHERE data__Identifier = '<Id>';
```

## Permissions

To operate on the <code>security_group</code> resource, the following permissions are required:

### Read
```json
ec2:DescribeSecurityGroups
```

### Update
```json
ec2:RevokeSecurityGroupEgress,
ec2:RevokeSecurityGroupIngress,
ec2:DescribeSecurityGroups,
ec2:AuthorizeSecurityGroupEgress,
ec2:AuthorizeSecurityGroupIngress,
ec2:CreateTags,
ec2:DeleteTags
```

### Delete
```json
ec2:DeleteSecurityGroup,
ec2:DescribeInstances
```

