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
<tr><td><b>Description</b></td><td>endpoint</td></tr>
<tr><td><b>Id</b></td><td><code>aws.s3outposts.endpoint</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the endpoint.</td></tr>
<tr><td><code>CidrBlock</code></td><td><code>string</code></td><td>The VPC CIDR committed by this endpoint.</td></tr>
<tr><td><code>CreationTime</code></td><td><code>undefined</code></td><td>The time the endpoint was created.</td></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td>The ID of the endpoint.</td></tr>
<tr><td><code>NetworkInterfaces</code></td><td><code>array</code></td><td>The network interfaces of the endpoint.</td></tr>
<tr><td><code>OutpostId</code></td><td><code>string</code></td><td>The id of the customer outpost on which the bucket resides.</td></tr>
<tr><td><code>SecurityGroupId</code></td><td><code>string</code></td><td>The ID of the security group to use with the endpoint.</td></tr>
<tr><td><code>Status</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>SubnetId</code></td><td><code>string</code></td><td>The ID of the subnet in the selected VPC. The subnet must belong to the Outpost.</td></tr>
<tr><td><code>AccessType</code></td><td><code>string</code></td><td>The type of access for the on-premise network connectivity for the Outpost endpoint. To access endpoint from an on-premises network, you must specify the access type and provide the customer owned Ipv4 pool.</td></tr>
<tr><td><code>CustomerOwnedIpv4Pool</code></td><td><code>string</code></td><td>The ID of the customer-owned IPv4 pool for the Endpoint. IP addresses will be allocated from this pool for the endpoint.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.s3outposts.endpoint<br/>WHERE region = 'us-east-1'<br/>AND data__Identifier = '&lt;Arn&gt;'
</pre>
