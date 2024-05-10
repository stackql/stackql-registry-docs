---
title: gateways
hide_title: false
hide_table_of_contents: false
keywords:
  - gateways
  - iotsitewise
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


Used to retrieve a list of <code>gateways</code> in a region or to create or delete a <code>gateways</code> resource, use <code>gateway</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>gateways</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::IoTSiteWise::Gateway</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iotsitewise.gateways" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="gateway_id" /></td><td><code>string</code></td><td>The ID of the gateway device.</td></tr>
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
gateway_id
FROM aws.iotsitewise.gateways
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
 "GatewayName": "{{ GatewayName }}",
 "GatewayPlatform": {
  "Greengrass": {
   "GroupArn": "{{ GroupArn }}"
  },
  "GreengrassV2": {
   "CoreDeviceThingName": "{{ CoreDeviceThingName }}"
  },
  "SiemensIE": {
   "IotCoreThingName": "{{ IotCoreThingName }}"
  }
 }
}
>>>
--required properties only
INSERT INTO aws.iotsitewise.gateways (
 GatewayName,
 GatewayPlatform,
 region
)
SELECT 
{{ GatewayName }},
 {{ GatewayPlatform }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "GatewayName": "{{ GatewayName }}",
 "GatewayPlatform": {
  "Greengrass": {
   "GroupArn": "{{ GroupArn }}"
  },
  "GreengrassV2": {
   "CoreDeviceThingName": "{{ CoreDeviceThingName }}"
  },
  "SiemensIE": {
   "IotCoreThingName": "{{ IotCoreThingName }}"
  }
 },
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ],
 "GatewayCapabilitySummaries": [
  {
   "CapabilityNamespace": "{{ CapabilityNamespace }}",
   "CapabilityConfiguration": "{{ CapabilityConfiguration }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.iotsitewise.gateways (
 GatewayName,
 GatewayPlatform,
 Tags,
 GatewayCapabilitySummaries,
 region
)
SELECT 
 {{ GatewayName }},
 {{ GatewayPlatform }},
 {{ Tags }},
 {{ GatewayCapabilitySummaries }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.iotsitewise.gateways
WHERE data__Identifier = '<GatewayId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>gateways</code> resource, the following permissions are required:

### Create
```json
iotsitewise:CreateGateway,
iotsitewise:DescribeGateway,
iotsitewise:DescribeGatewayCapabilityConfiguration,
iotsitewise:UpdateGatewayCapabilityConfiguration,
iam:PassRole,
iam:GetRole,
greengrass:GetCoreDevice,
iotsitewise:ListTagsForResource,
iotsitewise:TagResource,
iot:DescribeThing
```

### Delete
```json
iotsitewise:DescribeGateway,
iotsitewise:DescribeGatewayCapabilityConfiguration,
iotsitewise:DeleteGateway
```

### List
```json
iotsitewise:ListGateways
```

