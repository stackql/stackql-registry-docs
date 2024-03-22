---
title: network_acl
hide_title: false
hide_table_of_contents: false
keywords:
  - network_acl
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
Gets an individual <code>network_acl</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>network_acl</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>network_acl</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.ec2.network_acl</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>The tags to assign to the network ACL.</td></tr>
<tr><td><code>vpc_id</code></td><td><code>string</code></td><td>The ID of the VPC.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
id,
tags,
vpc_id
FROM awscc.ec2.network_acl
WHERE data__Identifier = '<Id>';
```

## Permissions

To operate on the <code>network_acl</code> resource, the following permissions are required:

### Read
```json
ec2:DescribeNetworkAcls,
ec2:DescribeTags
```

### Update
```json
ec2:DescribeNetworkAcls,
ec2:DeleteTags,
ec2:CreateTags
```

### Delete
```json
ec2:DeleteTags,
ec2:DeleteNetworkAcl,
ec2:DescribeNetworkAcls
```

