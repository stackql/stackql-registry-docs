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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Gets or operates on an individual <code>customer_gateway_association</code> resource, use <code>customer_gateway_associations</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>customer_gateway_association</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::NetworkManager::CustomerGatewayAssociation type associates a customer gateway with a device and optionally, with a link.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.networkmanager.customer_gateway_association" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="global_network_id" /></td><td><code>string</code></td><td>The ID of the global network.</td></tr>
<tr><td><CopyableCode code="customer_gateway_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the customer gateway.</td></tr>
<tr><td><CopyableCode code="device_id" /></td><td><code>string</code></td><td>The ID of the device</td></tr>
<tr><td><CopyableCode code="link_id" /></td><td><code>string</code></td><td>The ID of the link</td></tr>
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
global_network_id,
customer_gateway_arn,
device_id,
link_id
FROM aws.networkmanager.customer_gateway_association
WHERE data__Identifier = '<GlobalNetworkId>|<CustomerGatewayArn>';
```

## Permissions

To operate on the <code>customer_gateway_association</code> resource, the following permissions are required:

### Read
```json
networkmanager:GetCustomerGatewayAssociations
```

### Delete
```json
networkmanager:DisassociateCustomerGateway
```

