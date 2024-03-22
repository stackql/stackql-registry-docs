---
title: instance_connect_endpoint
hide_title: false
hide_table_of_contents: false
keywords:
  - instance_connect_endpoint
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
Gets an individual <code>instance_connect_endpoint</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instance_connect_endpoint</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>instance_connect_endpoint</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.ec2.instance_connect_endpoint</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>The id of the instance connect endpoint</td></tr>
<tr><td><code>subnet_id</code></td><td><code>string</code></td><td>The subnet id of the instance connect endpoint</td></tr>
<tr><td><code>client_token</code></td><td><code>string</code></td><td>The client token of the instance connect endpoint.</td></tr>
<tr><td><code>preserve_client_ip</code></td><td><code>boolean</code></td><td>If true, the address of the instance connect endpoint client is preserved when connecting to the end resource</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>The tags of the instance connect endpoint.</td></tr>
<tr><td><code>security_group_ids</code></td><td><code>array</code></td><td>The security group IDs of the instance connect endpoint.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
id,
subnet_id,
client_token,
preserve_client_ip,
tags,
security_group_ids
FROM awscc.ec2.instance_connect_endpoint
WHERE data__Identifier = '<Id>';
```

## Permissions

To operate on the <code>instance_connect_endpoint</code> resource, the following permissions are required:

### Read
```json
ec2:DescribeInstanceConnectEndpoints
```

### Update
```json
ec2:DescribeInstanceConnectEndpoints,
ec2:CreateTags,
ec2:DeleteTags
```

### Delete
```json
ec2:DeleteInstanceConnectEndpoint,
ec2:DescribeInstanceConnectEndpoints
```

