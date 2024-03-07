---
title: vpc_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - vpc_connections
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
Retrieves a list of <code>vpc_connections</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpc_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>vpc_connections</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.quicksight.vpc_connections</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>aws_account_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>v_pc_connection_id</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>vpc_connections</code> resource, the following permissions are required:

### Create
<pre>
quicksight:CreateVPCConnection,
quicksight:DescribeVPCConnection,
quicksight:ListTagsForResource,
quicksight:TagResource,
iam:PassRole</pre>

### List
<pre>
quicksight:ListVPCConnections</pre>


## Example
```sql
SELECT
region,
aws_account_id,
v_pc_connection_id
FROM awscc.quicksight.vpc_connections
WHERE region = 'us-east-1'
```
