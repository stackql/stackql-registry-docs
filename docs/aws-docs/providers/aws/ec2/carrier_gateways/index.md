---
title: carrier_gateways
hide_title: false
hide_table_of_contents: false
keywords:
  - carrier_gateways
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Used to retrieve a list of <code>carrier_gateways</code> in a region or to create or delete a <code>carrier_gateways</code> resource, use <code>carrier_gateway</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>carrier_gateways</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An example resource schema demonstrating some basic constructs and validation rules.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.carrier_gateways" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="carrier_gateway_id" /></td><td><code>string</code></td><td>The ID of the carrier gateway.</td></tr>
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
carrier_gateway_id
FROM aws.ec2.carrier_gateways
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
 "VpcId": "{{ VpcId }}"
}
>>>
--required properties only
INSERT INTO aws.ec2.carrier_gateways (
 VpcId,
 region
)
SELECT 
{{ .VpcId }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "VpcId": "{{ VpcId }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.ec2.carrier_gateways (
 VpcId,
 Tags,
 region
)
SELECT 
 {{ .VpcId }},
 {{ .Tags }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.ec2.carrier_gateways
WHERE data__Identifier = '<CarrierGatewayId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>carrier_gateways</code> resource, the following permissions are required:

### Create
```json
ec2:CreateCarrierGateway,
ec2:DescribeCarrierGateways,
ec2:CreateTags
```

### Delete
```json
ec2:DeleteCarrierGateway,
ec2:DescribeCarrierGateways
```

### List
```json
ec2:DescribeCarrierGateways
```

