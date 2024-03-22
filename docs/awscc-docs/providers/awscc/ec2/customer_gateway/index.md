---
title: customer_gateway
hide_title: false
hide_table_of_contents: false
keywords:
  - customer_gateway
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
Gets an individual <code>customer_gateway</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>customer_gateway</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>customer_gateway</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.ec2.customer_gateway</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>customer_gateway_id</code></td><td><code>string</code></td><td>CustomerGateway ID generated after customer gateway is created. Each customer gateway has a unique ID.</td></tr>
<tr><td><code>bgp_asn</code></td><td><code>integer</code></td><td>For devices that support BGP, the customer gateway's BGP ASN.</td></tr>
<tr><td><code>ip_address</code></td><td><code>string</code></td><td>The internet-routable IP address for the customer gateway's outside interface. The address must be static.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>One or more tags for the customer gateway.</td></tr>
<tr><td><code>type</code></td><td><code>string</code></td><td>The type of VPN connection that this customer gateway supports.</td></tr>
<tr><td><code>device_name</code></td><td><code>string</code></td><td>A name for the customer gateway device.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
customer_gateway_id,
bgp_asn,
ip_address,
tags,
type,
device_name
FROM awscc.ec2.customer_gateway
WHERE data__Identifier = '<CustomerGatewayId>';
```

## Permissions

To operate on the <code>customer_gateway</code> resource, the following permissions are required:

### Read
```json
ec2:DescribeCustomerGateways
```

### Update
```json
ec2:CreateTags,
ec2:DeleteTags
```

### Delete
```json
ec2:DeleteCustomerGateway,
ec2:DescribeCustomerGateways
```

