---
title: transit_gateway_peerings
hide_title: false
hide_table_of_contents: false
keywords:
  - transit_gateway_peerings
  - networkmanager
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>transit_gateway_peerings</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>transit_gateway_peerings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>transit_gateway_peerings</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.networkmanager.transit_gateway_peerings</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>peering_id</code></td><td><code>string</code></td><td>The Id of the transit gateway peering</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>transit_gateway_peerings</code> resource, the following permissions are required:

### Create
<pre>
networkmanager:CreateTransitGatewayPeering,
networkmanager:TagResource,
networkmanager:GetTransitGatewayPeering,
iam:CreateServiceLinkedRole,
ec2:CreateTransitGatewayPeeringAttachment,
ec2:AcceptTransitGatewayPeeringAttachment,
ec2:DescribeRegions</pre>

### List
<pre>
networkmanager:ListPeerings</pre>


## Example
```sql
SELECT
region,
peering_id
FROM awscc.networkmanager.transit_gateway_peerings
WHERE region = 'us-east-1'
```
