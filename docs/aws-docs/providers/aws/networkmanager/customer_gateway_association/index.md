---
title: customer_gateway_association
hide_title: false
hide_table_of_contents: false
keywords:
  - customer_gateway_association
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
Gets an individual <code>customer_gateway_association</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>customer_gateway_association</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>customer_gateway_association</td></tr>
<tr><td><b>Id</b></td><td><code>aws.networkmanager.customer_gateway_association</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>global_network_id</code></td><td><code>string</code></td><td>The ID of the global network.</td></tr>
<tr><td><code>customer_gateway_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the customer gateway.</td></tr>
<tr><td><code>device_id</code></td><td><code>string</code></td><td>The ID of the device</td></tr>
<tr><td><code>link_id</code></td><td><code>string</code></td><td>The ID of the link</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
global_network_id,
customer_gateway_arn,
device_id,
link_id
FROM aws.networkmanager.customer_gateway_association
WHERE region = 'us-east-1'
AND data__Identifier = '<GlobalNetworkId>'
AND data__Identifier = '<CustomerGatewayArn>'
```
