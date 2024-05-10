---
title: transit_gateway_multicast_group_sources
hide_title: false
hide_table_of_contents: false
keywords:
  - transit_gateway_multicast_group_sources
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


Used to retrieve a list of <code>transit_gateway_multicast_group_sources</code> in a region or to create or delete a <code>transit_gateway_multicast_group_sources</code> resource, use <code>transit_gateway_multicast_group_source</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>transit_gateway_multicast_group_sources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::EC2::TransitGatewayMulticastGroupSource registers and deregisters members and sources (network interfaces) with the transit gateway multicast group</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.transit_gateway_multicast_group_sources" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="transit_gateway_multicast_domain_id" /></td><td><code>string</code></td><td>The ID of the transit gateway multicast domain.</td></tr>
<tr><td><CopyableCode code="group_ip_address" /></td><td><code>string</code></td><td>The IP address assigned to the transit gateway multicast group.</td></tr>
<tr><td><CopyableCode code="network_interface_id" /></td><td><code>string</code></td><td>The ID of the transit gateway attachment.</td></tr>
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
transit_gateway_multicast_domain_id,
group_ip_address,
network_interface_id
FROM aws.ec2.transit_gateway_multicast_group_sources
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
 "GroupIpAddress": "{{ GroupIpAddress }}",
 "TransitGatewayMulticastDomainId": "{{ TransitGatewayMulticastDomainId }}",
 "NetworkInterfaceId": "{{ NetworkInterfaceId }}"
}
>>>
--required properties only
INSERT INTO aws.ec2.transit_gateway_multicast_group_sources (
 GroupIpAddress,
 TransitGatewayMulticastDomainId,
 NetworkInterfaceId,
 region
)
SELECT 
{{ GroupIpAddress }},
 {{ TransitGatewayMulticastDomainId }},
 {{ NetworkInterfaceId }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "GroupIpAddress": "{{ GroupIpAddress }}",
 "TransitGatewayMulticastDomainId": "{{ TransitGatewayMulticastDomainId }}",
 "NetworkInterfaceId": "{{ NetworkInterfaceId }}"
}
>>>
--all properties
INSERT INTO aws.ec2.transit_gateway_multicast_group_sources (
 GroupIpAddress,
 TransitGatewayMulticastDomainId,
 NetworkInterfaceId,
 region
)
SELECT 
 {{ GroupIpAddress }},
 {{ TransitGatewayMulticastDomainId }},
 {{ NetworkInterfaceId }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.ec2.transit_gateway_multicast_group_sources
WHERE data__Identifier = '<TransitGatewayMulticastDomainId|GroupIpAddress|NetworkInterfaceId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>transit_gateway_multicast_group_sources</code> resource, the following permissions are required:

### Create
```json
ec2:RegisterTransitGatewayMulticastGroupSources,
ec2:SearchTransitGatewayMulticastGroups
```

### Delete
```json
ec2:DeregisterTransitGatewayMulticastGroupSources,
ec2:SearchTransitGatewayMulticastGroups
```

### List
```json
ec2:SearchTransitGatewayMulticastGroups
```

