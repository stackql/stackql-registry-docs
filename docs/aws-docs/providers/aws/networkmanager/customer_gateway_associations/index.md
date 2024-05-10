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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Used to retrieve a list of <code>customer_gateway_associations</code> in a region or to create or delete a <code>customer_gateway_associations</code> resource, use <code>customer_gateway_association</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>customer_gateway_associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::NetworkManager::CustomerGatewayAssociation type associates a customer gateway with a device and optionally, with a link.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.networkmanager.customer_gateway_associations" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="global_network_id" /></td><td><code>string</code></td><td>The ID of the global network.</td></tr>
<tr><td><CopyableCode code="customer_gateway_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the customer gateway.</td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
global_network_id,
customer_gateway_arn
FROM aws.networkmanager.customer_gateway_associations
WHERE region = 'us-east-1';
```

## `INSERT` Example

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },

    ]
}>
<TabItem value="required">

```sql
<<<json
{
 "GlobalNetworkId": "{{ GlobalNetworkId }}",
 "CustomerGatewayArn": "{{ CustomerGatewayArn }}",
 "DeviceId": "{{ DeviceId }}"
}
>>>
--required properties only
INSERT INTO aws.networkmanager.customer_gateway_associations (
 GlobalNetworkId,
 CustomerGatewayArn,
 DeviceId,
 region
)
SELECT 
{{ GlobalNetworkId }},
 {{ CustomerGatewayArn }},
 {{ DeviceId }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "GlobalNetworkId": "{{ GlobalNetworkId }}",
 "CustomerGatewayArn": "{{ CustomerGatewayArn }}",
 "DeviceId": "{{ DeviceId }}",
 "LinkId": "{{ LinkId }}"
}
>>>
--all properties
INSERT INTO aws.networkmanager.customer_gateway_associations (
 GlobalNetworkId,
 CustomerGatewayArn,
 DeviceId,
 LinkId,
 region
)
SELECT 
 {{ GlobalNetworkId }},
 {{ CustomerGatewayArn }},
 {{ DeviceId }},
 {{ LinkId }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.networkmanager.customer_gateway_associations
WHERE data__Identifier = '<GlobalNetworkId|CustomerGatewayArn>'
AND region = 'us-east-1';
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

### Delete
```json
networkmanager:DisassociateCustomerGateway
```

