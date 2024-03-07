---
title: vpc_connection
hide_title: false
hide_table_of_contents: false
keywords:
  - vpc_connection
  - quicksight
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>vpc_connection</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpc_connection</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>vpc_connection</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.quicksight.vpc_connection</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>aws_account_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>v_pc_connection_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>v_pc_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>security_group_ids</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>subnet_ids</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>dns_resolvers</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>status</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>availability_status</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>network_interfaces</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>role_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>created_time</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>last_updated_time</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>vpc_connection</code> resource, the following permissions are required:

### Read
```json
quicksight:DescribeVPCConnection,
quicksight:ListTagsForResource
```

### Update
```json
quicksight:DescribeVPCConnection,
quicksight:UpdateVPCConnection,
quicksight:TagResource,
quicksight:UntagResource,
quicksight:ListTagsForResource,
iam:PassRole
```

### Delete
```json
quicksight:DescribeVPCConnection,
quicksight:DeleteVPCConnection,
quicksight:ListTagsForResource,
iam:PassRole
```


## Example
```sql
SELECT
region,
arn,
aws_account_id,
name,
v_pc_connection_id,
v_pc_id,
security_group_ids,
subnet_ids,
dns_resolvers,
status,
availability_status,
network_interfaces,
role_arn,
created_time,
last_updated_time,
tags
FROM awscc.quicksight.vpc_connection
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;AwsAccountId&gt;'
AND data__Identifier = '&lt;VPCConnectionId&gt;'
```
