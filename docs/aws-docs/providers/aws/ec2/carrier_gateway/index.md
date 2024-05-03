---
title: carrier_gateway
hide_title: false
hide_table_of_contents: false
keywords:
  - carrier_gateway
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Gets or operates on an individual <code>carrier_gateway</code> resource, use <code>carrier_gateways</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>carrier_gateway</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An example resource schema demonstrating some basic constructs and validation rules.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.carrier_gateway" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="carrier_gateway_id" /></td><td><code>string</code></td><td>The ID of the carrier gateway.</td></tr>
<tr><td><CopyableCode code="state" /></td><td><code>string</code></td><td>The state of the carrier gateway.</td></tr>
<tr><td><CopyableCode code="vpc_id" /></td><td><code>string</code></td><td>The ID of the VPC.</td></tr>
<tr><td><CopyableCode code="owner_id" /></td><td><code>string</code></td><td>The ID of the owner.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The tags for the carrier gateway.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
carrier_gateway_id,
state,
vpc_id,
owner_id,
tags
FROM aws.ec2.carrier_gateway
WHERE data__Identifier = '<CarrierGatewayId>';
```

## Permissions

To operate on the <code>carrier_gateway</code> resource, the following permissions are required:

### Read
```json
ec2:DescribeCarrierGateways
```

### Update
```json
ec2:DescribeCarrierGateways,
ec2:CreateTags,
ec2:DeleteTags
```

### Delete
```json
ec2:DeleteCarrierGateway,
ec2:DescribeCarrierGateways
```
