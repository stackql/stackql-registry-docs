---
title: transit_gateway_vpc_attachments
hide_title: false
hide_table_of_contents: false
keywords:
  - transit_gateway_vpc_attachments
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


Used to retrieve a list of <code>transit_gateway_vpc_attachments</code> in a region or to create or delete a <code>transit_gateway_vpc_attachments</code> resource, use <code>transit_gateway_vpc_attachment</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>transit_gateway_vpc_attachments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EC2::TransitGatewayVpcAttachment</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.transit_gateway_vpc_attachments" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
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
id
FROM aws.ec2.transit_gateway_vpc_attachments
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
 "TransitGatewayId": "{{ TransitGatewayId }}",
 "VpcId": "{{ VpcId }}",
 "SubnetIds": [
  "{{ SubnetIds[0] }}"
 ]
}
>>>
--required properties only
INSERT INTO aws.ec2.transit_gateway_vpc_attachments (
 TransitGatewayId,
 VpcId,
 SubnetIds,
 region
)
SELECT 
{{ TransitGatewayId }},
 {{ VpcId }},
 {{ SubnetIds }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Options": {
  "Ipv6Support": "{{ Ipv6Support }}",
  "ApplianceModeSupport": "{{ ApplianceModeSupport }}",
  "DnsSupport": "{{ DnsSupport }}"
 },
 "TransitGatewayId": "{{ TransitGatewayId }}",
 "VpcId": "{{ VpcId }}",
 "RemoveSubnetIds": [
  "{{ RemoveSubnetIds[0] }}"
 ],
 "SubnetIds": [
  "{{ SubnetIds[0] }}"
 ],
 "AddSubnetIds": [
  "{{ AddSubnetIds[0] }}"
 ],
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.ec2.transit_gateway_vpc_attachments (
 Options,
 TransitGatewayId,
 VpcId,
 RemoveSubnetIds,
 SubnetIds,
 AddSubnetIds,
 Tags,
 region
)
SELECT 
 {{ Options }},
 {{ TransitGatewayId }},
 {{ VpcId }},
 {{ RemoveSubnetIds }},
 {{ SubnetIds }},
 {{ AddSubnetIds }},
 {{ Tags }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.ec2.transit_gateway_vpc_attachments
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>transit_gateway_vpc_attachments</code> resource, the following permissions are required:

### Create
```json
ec2:DescribeTransitGatewayAttachments,
ec2:DescribeTransitGatewayVpcAttachments,
ec2:CreateTransitGatewayVpcAttachment,
ec2:DeleteTransitGatewayVpcAttachment,
ec2:CreateTags,
ec2:DeleteTags,
ec2:DescribeTags,
ec2:DescribeTransitGatewayAttachments,
ec2:ModifyTransitGatewayVpcAttachment
```

### List
```json
ec2:DescribeTransitGatewayAttachments,
ec2:DescribeTransitGatewayVpcAttachments,
ec2:DescribeTags,
ec2:CreateTransitGatewayVpcAttachment,
ec2:CreateTags,
ec2:DeleteTransitGatewayVpcAttachment,
ec2:DeleteTags,
ec2:ModifyTransitGatewayVpcAttachment
```

### Delete
```json
ec2:DescribeTransitGatewayAttachments,
ec2:DescribeTransitGatewayVpcAttachments,
ec2:CreateTransitGatewayVpcAttachment,
ec2:DeleteTransitGatewayVpcAttachment,
ec2:CreateTags,
ec2:DeleteTags,
ec2:DescribeTags,
ec2:DescribeTransitGatewayAttachments,
ec2:ModifyTransitGatewayVpcAttachment
```

