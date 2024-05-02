---
title: endpoint
hide_title: false
hide_table_of_contents: false
keywords:
  - endpoint
  - s3outposts
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>endpoint</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>endpoint</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type Definition for AWS::S3Outposts::Endpoint</td></tr>
<tr><td><b>Id</b></td><td><code>aws.s3outposts.endpoint</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the endpoint.</td></tr>
<tr><td><code>cidr_block</code></td><td><code>string</code></td><td>The VPC CIDR committed by this endpoint.</td></tr>
<tr><td><code>creation_time</code></td><td><code>string</code></td><td>The time the endpoint was created.</td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>The ID of the endpoint.</td></tr>
<tr><td><code>network_interfaces</code></td><td><code>array</code></td><td>The network interfaces of the endpoint.</td></tr>
<tr><td><code>outpost_id</code></td><td><code>string</code></td><td>The id of the customer outpost on which the bucket resides.</td></tr>
<tr><td><code>security_group_id</code></td><td><code>string</code></td><td>The ID of the security group to use with the endpoint.</td></tr>
<tr><td><code>status</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>subnet_id</code></td><td><code>string</code></td><td>The ID of the subnet in the selected VPC. The subnet must belong to the Outpost.</td></tr>
<tr><td><code>access_type</code></td><td><code>string</code></td><td>The type of access for the on-premise network connectivity for the Outpost endpoint. To access endpoint from an on-premises network, you must specify the access type and provide the customer owned Ipv4 pool.</td></tr>
<tr><td><code>customer_owned_ipv4_pool</code></td><td><code>string</code></td><td>The ID of the customer-owned IPv4 pool for the Endpoint. IP addresses will be allocated from this pool for the endpoint.</td></tr>
<tr><td><code>failed_reason</code></td><td><code>object</code></td><td>The failure reason, if any, for a create or delete endpoint operation.</td></tr>
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
arn,
cidr_block,
creation_time,
id,
network_interfaces,
outpost_id,
security_group_id,
status,
subnet_id,
access_type,
customer_owned_ipv4_pool,
failed_reason
FROM aws.s3outposts.endpoint
WHERE data__Identifier = '<Arn>';
```

## Permissions

To operate on the <code>endpoint</code> resource, the following permissions are required:

### Read
```json
s3-outposts:ListEndpoints
```

### Delete
```json
s3-outposts:DeleteEndpoint
```

