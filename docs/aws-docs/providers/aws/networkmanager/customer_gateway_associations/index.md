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

Creates, updates, deletes or gets a <code>customer_gateway_association</code> resource or lists <code>customer_gateway_associations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>customer_gateway_associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::NetworkManager::CustomerGatewayAssociation type associates a customer gateway with a device and optionally, with a link.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.networkmanager.customer_gateway_associations" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="global_network_id" /></td><td><code>string</code></td><td>The ID of the global network.</td></tr>
<tr><td><CopyableCode code="customer_gateway_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the customer gateway.</td></tr>
<tr><td><CopyableCode code="device_id" /></td><td><code>string</code></td><td>The ID of the device</td></tr>
<tr><td><CopyableCode code="link_id" /></td><td><code>string</code></td><td>The ID of the link</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-customergatewayassociation.html"><code>AWS::NetworkManager::CustomerGatewayAssociation</code></a>.

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
    <td><CopyableCode code="GlobalNetworkId, CustomerGatewayArn, DeviceId, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Gets all <code>customer_gateway_associations</code> in a region.
```sql
SELECT
region,
global_network_id,
customer_gateway_arn,
device_id,
link_id
FROM aws.networkmanager.customer_gateway_associations
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>customer_gateway_association</code>.
```sql
SELECT
region,
global_network_id,
customer_gateway_arn,
device_id,
link_id
FROM aws.networkmanager.customer_gateway_associations
WHERE region = 'us-east-1' AND data__Identifier = '<GlobalNetworkId>|<CustomerGatewayArn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>customer_gateway_association</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
/*+ create */
INSERT INTO aws.networkmanager.customer_gateway_associations (
 GlobalNetworkId,
 CustomerGatewayArn,
 DeviceId,
 region
)
SELECT 
'{{ GlobalNetworkId }}',
 '{{ CustomerGatewayArn }}',
 '{{ DeviceId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.networkmanager.customer_gateway_associations (
 GlobalNetworkId,
 CustomerGatewayArn,
 DeviceId,
 LinkId,
 region
)
SELECT 
 '{{ GlobalNetworkId }}',
 '{{ CustomerGatewayArn }}',
 '{{ DeviceId }}',
 '{{ LinkId }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: customer_gateway_association
    props:
      - name: GlobalNetworkId
        value: '{{ GlobalNetworkId }}'
      - name: CustomerGatewayArn
        value: '{{ CustomerGatewayArn }}'
      - name: DeviceId
        value: '{{ DeviceId }}'
      - name: LinkId
        value: '{{ LinkId }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
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

### Read
```json
networkmanager:GetCustomerGatewayAssociations
```

### List
```json
networkmanager:GetCustomerGatewayAssociations
```

### Delete
```json
networkmanager:DisassociateCustomerGateway
```
