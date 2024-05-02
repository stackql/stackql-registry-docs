---
title: transit_gateway_registration
hide_title: false
hide_table_of_contents: false
keywords:
  - transit_gateway_registration
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
Gets an individual <code>transit_gateway_registration</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>transit_gateway_registration</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::NetworkManager::TransitGatewayRegistration type registers a transit gateway in your global network. The transit gateway can be in any AWS Region, but it must be owned by the same AWS account that owns the global network. You cannot register a transit gateway in more than one global network.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.networkmanager.transit_gateway_registration</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>global_network_id</code></td><td><code>string</code></td><td>The ID of the global network.</td></tr>
<tr><td><code>transit_gateway_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the transit gateway.</td></tr>
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
global_network_id,
transit_gateway_arn
FROM aws.networkmanager.transit_gateway_registration
WHERE data__Identifier = '<GlobalNetworkId>|<TransitGatewayArn>';
```

## Permissions

To operate on the <code>transit_gateway_registration</code> resource, the following permissions are required:

### Read
```json
networkmanager:GetTransitGatewayRegistrations
```

### Delete
```json
networkmanager:DeregisterTransitGateway,
networkmanager:GetTransitGatewayRegistrations
```

