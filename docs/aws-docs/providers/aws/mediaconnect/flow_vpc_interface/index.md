---
title: flow_vpc_interface
hide_title: false
hide_table_of_contents: false
keywords:
  - flow_vpc_interface
  - mediaconnect
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>flow_vpc_interface</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>flow_vpc_interface</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>flow_vpc_interface</td></tr>
<tr><td><b>Id</b></td><td><code>aws.mediaconnect.flow_vpc_interface</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>flow_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN), a unique identifier for any AWS resource, of the flow.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>Immutable and has to be a unique against other VpcInterfaces in this Flow.</td></tr>
<tr><td><code>role_arn</code></td><td><code>string</code></td><td>Role Arn MediaConnect can assumes to create ENIs in customer's account.</td></tr>
<tr><td><code>security_group_ids</code></td><td><code>array</code></td><td>Security Group IDs to be used on ENI.</td></tr>
<tr><td><code>subnet_id</code></td><td><code>string</code></td><td>Subnet must be in the AZ of the Flow</td></tr>
<tr><td><code>network_interface_ids</code></td><td><code>array</code></td><td>IDs of the network interfaces created in customer's account by MediaConnect.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
flow_arn,
name,
role_arn,
security_group_ids,
subnet_id,
network_interface_ids
FROM aws.mediaconnect.flow_vpc_interface
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;FlowArn&gt;'
AND data__Identifier = '&lt;Name&gt;'
```
