---
title: transit_gateway_multicast_domains
hide_title: false
hide_table_of_contents: false
keywords:
  - transit_gateway_multicast_domains
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


Used to retrieve a list of <code>transit_gateway_multicast_domains</code> in a region or to create or delete a <code>transit_gateway_multicast_domains</code> resource, use <code>transit_gateway_multicast_domain</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>transit_gateway_multicast_domains</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::EC2::TransitGatewayMulticastDomain type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.transit_gateway_multicast_domains" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="transit_gateway_multicast_domain_id" /></td><td><code>string</code></td><td>The ID of the transit gateway multicast domain.</td></tr>
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
transit_gateway_multicast_domain_id
FROM aws.ec2.transit_gateway_multicast_domains
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
 "TransitGatewayId": "{{ TransitGatewayId }}"
}
>>>
--required properties only
INSERT INTO aws.ec2.transit_gateway_multicast_domains (
 TransitGatewayId,
 region
)
SELECT 
{{ TransitGatewayId }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "TransitGatewayId": "{{ TransitGatewayId }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ],
 "Options": {
  "AutoAcceptSharedAssociations": "{{ AutoAcceptSharedAssociations }}",
  "Igmpv2Support": "{{ Igmpv2Support }}",
  "StaticSourcesSupport": "{{ StaticSourcesSupport }}"
 }
}
>>>
--all properties
INSERT INTO aws.ec2.transit_gateway_multicast_domains (
 TransitGatewayId,
 Tags,
 Options,
 region
)
SELECT 
 {{ TransitGatewayId }},
 {{ Tags }},
 {{ Options }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.ec2.transit_gateway_multicast_domains
WHERE data__Identifier = '<TransitGatewayMulticastDomainId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>transit_gateway_multicast_domains</code> resource, the following permissions are required:

### Create
```json
ec2:DescribeTransitGatewayMulticastDomains,
ec2:CreateTransitGatewayMulticastDomain,
ec2:CreateTags
```

### Delete
```json
ec2:DescribeTransitGatewayMulticastDomains,
ec2:DeleteTransitGatewayMulticastDomain,
ec2:DeleteTags
```

### List
```json
ec2:DescribeTransitGatewayMulticastDomains
```

