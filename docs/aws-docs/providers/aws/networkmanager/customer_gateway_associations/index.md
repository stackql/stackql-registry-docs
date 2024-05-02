---
title: customer_gateway_associations
hide_title: false
hide_table_of_contents: false
keywords:
  - customer_gateway_associations
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
Retrieves a list of <code>customer_gateway_associations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>customer_gateway_associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::NetworkManager::CustomerGatewayAssociation type associates a customer gateway with a device and optionally, with a link.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.networkmanager.customer_gateway_associations</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>global_network_id</code></td><td><code>string</code></td><td>The ID of the global network.</td></tr>
<tr><td><code>customer_gateway_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the customer gateway.</td></tr>
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
    <td><code>create_resource</code></td>
    <td><code>INSERT</code></td>
    <td><code>data__DesiredState, region</code></td>
  </tr>
  <tr>
    <td><code>list_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
global_network_id,
customer_gateway_arn
FROM aws.networkmanager.customer_gateway_associations
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>customer_gateway_associations</code> resource, the following permissions are required:

### Create
```json
networkmanager:GetCustomerGatewayAssociations,
networkmanager:AssociateCustomerGateway
```

### List
```json
networkmanager:GetCustomerGatewayAssociations
```

