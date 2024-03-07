---
title: transit_gateway_registrations
hide_title: false
hide_table_of_contents: false
keywords:
  - transit_gateway_registrations
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
Retrieves a list of <code>transit_gateway_registrations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>transit_gateway_registrations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>transit_gateway_registrations</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.networkmanager.transit_gateway_registrations</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>global_network_id</code></td><td><code>string</code></td><td>The ID of the global network.</td></tr>
<tr><td><code>transit_gateway_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the transit gateway.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
global_network_id,
transit_gateway_arn
FROM awscc.networkmanager.transit_gateway_registrations
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>transit_gateway_registrations</code> resource, the following permissions are required:

### Create
```json
networkmanager:RegisterTransitGateway,
networkmanager:GetTransitGatewayRegistrations
```

### List
```json
networkmanager:GetTransitGatewayRegistrations
```

