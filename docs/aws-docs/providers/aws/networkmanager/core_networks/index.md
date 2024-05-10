---
title: core_networks
hide_title: false
hide_table_of_contents: false
keywords:
  - core_networks
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


Used to retrieve a list of <code>core_networks</code> in a region or to create or delete a <code>core_networks</code> resource, use <code>core_network</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>core_networks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>AWS::NetworkManager::CoreNetwork Resource Type Definition.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.networkmanager.core_networks" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="core_network_id" /></td><td><code>string</code></td><td>The Id of core network</td></tr>
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
core_network_id
FROM aws.networkmanager.core_networks
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
 "GlobalNetworkId": "{{ GlobalNetworkId }}"
}
>>>
--required properties only
INSERT INTO aws.networkmanager.core_networks (
 GlobalNetworkId,
 region
)
SELECT 
{{ GlobalNetworkId }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "GlobalNetworkId": "{{ GlobalNetworkId }}",
 "PolicyDocument": {},
 "Description": "{{ Description }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.networkmanager.core_networks (
 GlobalNetworkId,
 PolicyDocument,
 Description,
 Tags,
 region
)
SELECT 
 {{ GlobalNetworkId }},
 {{ PolicyDocument }},
 {{ Description }},
 {{ Tags }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.networkmanager.core_networks
WHERE data__Identifier = '<CoreNetworkId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>core_networks</code> resource, the following permissions are required:

### Create
```json
networkmanager:CreateCoreNetwork,
networkmanager:GetCoreNetwork,
networkmanager:GetCoreNetworkPolicy,
networkmanager:TagResource,
ec2:DescribeRegions
```

### Delete
```json
networkmanager:DeleteCoreNetwork,
networkmanager:UntagResource,
networkmanager:GetCoreNetwork,
networkmanager:GetCoreNetworkPolicy,
ec2:DescribeRegions
```

### List
```json
networkmanager:ListCoreNetworks
```

