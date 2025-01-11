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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets a <code>transit_gateway_registration</code> resource or lists <code>transit_gateway_registrations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>transit_gateway_registrations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::NetworkManager::TransitGatewayRegistration type registers a transit gateway in your global network. The transit gateway can be in any AWS Region, but it must be owned by the same AWS account that owns the global network. You cannot register a transit gateway in more than one global network.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.networkmanager.transit_gateway_registrations" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="global_network_id" /></td><td><code>string</code></td><td>The ID of the global network.</td></tr>
<tr><td><CopyableCode code="transit_gateway_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the transit gateway.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-transitgatewayregistration.html"><code>AWS::NetworkManager::TransitGatewayRegistration</code></a>.

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
    <td><CopyableCode code="GlobalNetworkId, TransitGatewayArn, region" /></td>
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
Gets all <code>transit_gateway_registrations</code> in a region.
```sql
SELECT
region,
global_network_id,
transit_gateway_arn
FROM aws.networkmanager.transit_gateway_registrations
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>transit_gateway_registration</code>.
```sql
SELECT
region,
global_network_id,
transit_gateway_arn
FROM aws.networkmanager.transit_gateway_registrations
WHERE region = 'us-east-1' AND data__Identifier = '<GlobalNetworkId>|<TransitGatewayArn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>transit_gateway_registration</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.networkmanager.transit_gateway_registrations (
 GlobalNetworkId,
 TransitGatewayArn,
 region
)
SELECT 
'{{ GlobalNetworkId }}',
 '{{ TransitGatewayArn }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.networkmanager.transit_gateway_registrations (
 GlobalNetworkId,
 TransitGatewayArn,
 region
)
SELECT 
 '{{ GlobalNetworkId }}',
 '{{ TransitGatewayArn }}',
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
  - name: transit_gateway_registration
    props:
      - name: GlobalNetworkId
        value: '{{ GlobalNetworkId }}'
      - name: TransitGatewayArn
        value: '{{ TransitGatewayArn }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.networkmanager.transit_gateway_registrations
WHERE data__Identifier = '<GlobalNetworkId|TransitGatewayArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>transit_gateway_registrations</code> resource, the following permissions are required:

### Create
```json
networkmanager:RegisterTransitGateway,
networkmanager:GetTransitGatewayRegistrations
```

### Read
```json
networkmanager:GetTransitGatewayRegistrations
```

### List
```json
networkmanager:GetTransitGatewayRegistrations
```

### Delete
```json
networkmanager:DeregisterTransitGateway,
networkmanager:GetTransitGatewayRegistrations
```
