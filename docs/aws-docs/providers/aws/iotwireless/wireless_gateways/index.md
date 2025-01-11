---
title: wireless_gateways
hide_title: false
hide_table_of_contents: false
keywords:
  - wireless_gateways
  - iotwireless
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

Creates, updates, deletes or gets a <code>wireless_gateway</code> resource or lists <code>wireless_gateways</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>wireless_gateways</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Create and manage wireless gateways, including LoRa gateways.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iotwireless.wireless_gateways" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Name of Wireless Gateway.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>Description of Wireless Gateway.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A list of key-value pairs that contain metadata for the gateway.</td></tr>
<tr><td><CopyableCode code="lo_ra_wan" /></td><td><code>object</code></td><td>The combination of Package, Station and Model which represents the version of the LoRaWAN Wireless Gateway.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Arn for Wireless Gateway. Returned upon successful create.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>Id for Wireless Gateway. Returned upon successful create.</td></tr>
<tr><td><CopyableCode code="thing_arn" /></td><td><code>string</code></td><td>Thing Arn. Passed into Update to associate a Thing with the Wireless Gateway.</td></tr>
<tr><td><CopyableCode code="thing_name" /></td><td><code>string</code></td><td>Thing Name. If there is a Thing created, this can be returned with a Get call.</td></tr>
<tr><td><CopyableCode code="last_uplink_received_at" /></td><td><code>string</code></td><td>The date and time when the most recent uplink was received.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessgateway.html"><code>AWS::IoTWireless::WirelessGateway</code></a>.

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
    <td><CopyableCode code="LoRaWAN, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
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
Gets all <code>wireless_gateways</code> in a region.
```sql
SELECT
region,
name,
description,
tags,
lo_ra_wan,
arn,
id,
thing_arn,
thing_name,
last_uplink_received_at
FROM aws.iotwireless.wireless_gateways
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>wireless_gateway</code>.
```sql
SELECT
region,
name,
description,
tags,
lo_ra_wan,
arn,
id,
thing_arn,
thing_name,
last_uplink_received_at
FROM aws.iotwireless.wireless_gateways
WHERE region = 'us-east-1' AND data__Identifier = '<Id>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>wireless_gateway</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.iotwireless.wireless_gateways (
 LoRaWAN,
 region
)
SELECT 
'{{ LoRaWAN }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.iotwireless.wireless_gateways (
 Name,
 Description,
 Tags,
 LoRaWAN,
 ThingArn,
 ThingName,
 LastUplinkReceivedAt,
 region
)
SELECT 
 '{{ Name }}',
 '{{ Description }}',
 '{{ Tags }}',
 '{{ LoRaWAN }}',
 '{{ ThingArn }}',
 '{{ ThingName }}',
 '{{ LastUplinkReceivedAt }}',
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
  - name: wireless_gateway
    props:
      - name: Name
        value: '{{ Name }}'
      - name: Description
        value: '{{ Description }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: LoRaWAN
        value:
          GatewayEui: '{{ GatewayEui }}'
          RfRegion: '{{ RfRegion }}'
      - name: ThingArn
        value: '{{ ThingArn }}'
      - name: ThingName
        value: '{{ ThingName }}'
      - name: LastUplinkReceivedAt
        value: '{{ LastUplinkReceivedAt }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.iotwireless.wireless_gateways
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>wireless_gateways</code> resource, the following permissions are required:

### Create
```json
iotwireless:CreateWirelessGateway,
iotwireless:TagResource
```

### Read
```json
iotwireless:GetWirelessGateway,
iotwireless:ListTagsForResource
```

### Update
```json
iotwireless:GetWirelessGateway,
iotwireless:UpdateWirelessGateway,
iotwireless:AssociateWirelessGatewayWithThing,
iotwireless:TagResource,
iotwireless:UntagResource
```

### Delete
```json
iotwireless:DeleteWirelessGateway,
iotwireless:DisassociateWirelessGatewayFromThing
```

### List
```json
iotwireless:ListWirelessGateways,
iotwireless:ListTagsForResource
```
