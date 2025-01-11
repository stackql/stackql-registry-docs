---
title: transit_gateways
hide_title: false
hide_table_of_contents: false
keywords:
  - transit_gateways
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

Creates, updates, deletes or gets a <code>transit_gateway</code> resource or lists <code>transit_gateways</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>transit_gateways</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EC2::TransitGateway</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.transit_gateways" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="default_route_table_propagation" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="transit_gateway_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="auto_accept_shared_attachments" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="default_route_table_association" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="vpn_ecmp_support" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="dns_support" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="security_group_referencing_support" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="multicast_support" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="amazon_side_asn" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="transit_gateway_cidr_blocks" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="association_default_route_table_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="propagation_default_route_table_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgateway.html"><code>AWS::EC2::TransitGateway</code></a>.

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
    <td><CopyableCode code="region" /></td>
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
Gets all <code>transit_gateways</code> in a region.
```sql
SELECT
region,
default_route_table_propagation,
transit_gateway_arn,
description,
auto_accept_shared_attachments,
default_route_table_association,
id,
vpn_ecmp_support,
dns_support,
security_group_referencing_support,
multicast_support,
amazon_side_asn,
transit_gateway_cidr_blocks,
tags,
association_default_route_table_id,
propagation_default_route_table_id
FROM aws.ec2.transit_gateways
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>transit_gateway</code>.
```sql
SELECT
region,
default_route_table_propagation,
transit_gateway_arn,
description,
auto_accept_shared_attachments,
default_route_table_association,
id,
vpn_ecmp_support,
dns_support,
security_group_referencing_support,
multicast_support,
amazon_side_asn,
transit_gateway_cidr_blocks,
tags,
association_default_route_table_id,
propagation_default_route_table_id
FROM aws.ec2.transit_gateways
WHERE region = 'us-east-1' AND data__Identifier = '<Id>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>transit_gateway</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.ec2.transit_gateways (
 DefaultRouteTablePropagation,
 Description,
 AutoAcceptSharedAttachments,
 DefaultRouteTableAssociation,
 VpnEcmpSupport,
 DnsSupport,
 SecurityGroupReferencingSupport,
 MulticastSupport,
 AmazonSideAsn,
 TransitGatewayCidrBlocks,
 Tags,
 AssociationDefaultRouteTableId,
 PropagationDefaultRouteTableId,
 region
)
SELECT 
'{{ DefaultRouteTablePropagation }}',
 '{{ Description }}',
 '{{ AutoAcceptSharedAttachments }}',
 '{{ DefaultRouteTableAssociation }}',
 '{{ VpnEcmpSupport }}',
 '{{ DnsSupport }}',
 '{{ SecurityGroupReferencingSupport }}',
 '{{ MulticastSupport }}',
 '{{ AmazonSideAsn }}',
 '{{ TransitGatewayCidrBlocks }}',
 '{{ Tags }}',
 '{{ AssociationDefaultRouteTableId }}',
 '{{ PropagationDefaultRouteTableId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.ec2.transit_gateways (
 DefaultRouteTablePropagation,
 Description,
 AutoAcceptSharedAttachments,
 DefaultRouteTableAssociation,
 VpnEcmpSupport,
 DnsSupport,
 SecurityGroupReferencingSupport,
 MulticastSupport,
 AmazonSideAsn,
 TransitGatewayCidrBlocks,
 Tags,
 AssociationDefaultRouteTableId,
 PropagationDefaultRouteTableId,
 region
)
SELECT 
 '{{ DefaultRouteTablePropagation }}',
 '{{ Description }}',
 '{{ AutoAcceptSharedAttachments }}',
 '{{ DefaultRouteTableAssociation }}',
 '{{ VpnEcmpSupport }}',
 '{{ DnsSupport }}',
 '{{ SecurityGroupReferencingSupport }}',
 '{{ MulticastSupport }}',
 '{{ AmazonSideAsn }}',
 '{{ TransitGatewayCidrBlocks }}',
 '{{ Tags }}',
 '{{ AssociationDefaultRouteTableId }}',
 '{{ PropagationDefaultRouteTableId }}',
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
  - name: transit_gateway
    props:
      - name: DefaultRouteTablePropagation
        value: '{{ DefaultRouteTablePropagation }}'
      - name: Description
        value: '{{ Description }}'
      - name: AutoAcceptSharedAttachments
        value: '{{ AutoAcceptSharedAttachments }}'
      - name: DefaultRouteTableAssociation
        value: '{{ DefaultRouteTableAssociation }}'
      - name: VpnEcmpSupport
        value: '{{ VpnEcmpSupport }}'
      - name: DnsSupport
        value: '{{ DnsSupport }}'
      - name: SecurityGroupReferencingSupport
        value: '{{ SecurityGroupReferencingSupport }}'
      - name: MulticastSupport
        value: '{{ MulticastSupport }}'
      - name: AmazonSideAsn
        value: '{{ AmazonSideAsn }}'
      - name: TransitGatewayCidrBlocks
        value:
          - '{{ TransitGatewayCidrBlocks[0] }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: AssociationDefaultRouteTableId
        value: '{{ AssociationDefaultRouteTableId }}'
      - name: PropagationDefaultRouteTableId
        value: '{{ PropagationDefaultRouteTableId }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.ec2.transit_gateways
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>transit_gateways</code> resource, the following permissions are required:

### Create
```json
ec2:CreateTransitGateway,
ec2:CreateTags,
ec2:DescribeTransitGateways,
ec2:DescribeTags,
ec2:DeleteTransitGateway,
ec2:DeleteTags,
ec2:ModifyTransitGateway,
ec2:ModifyTransitGatewayOptions
```

### Read
```json
ec2:CreateTransitGateway,
ec2:CreateTags,
ec2:DescribeTransitGateways,
ec2:DescribeTags,
ec2:DeleteTransitGateway,
ec2:DeleteTags,
ec2:ModifyTransitGateway,
ec2:ModifyTransitGatewayOptions
```

### Delete
```json
ec2:CreateTransitGateway,
ec2:CreateTags,
ec2:DescribeTransitGateways,
ec2:DescribeTags,
ec2:DeleteTransitGateway,
ec2:DeleteTags,
ec2:ModifyTransitGateway,
ec2:ModifyTransitGatewayOptions
```

### Update
```json
ec2:CreateTransitGateway,
ec2:CreateTags,
ec2:DescribeTransitGateways,
ec2:DescribeTags,
ec2:DeleteTransitGateway,
ec2:DeleteTags,
ec2:ModifyTransitGateway,
ec2:ModifyTransitGatewayOptions
```

### List
```json
ec2:CreateTransitGateway,
ec2:CreateTags,
ec2:DescribeTransitGateways,
ec2:DescribeTags,
ec2:DeleteTransitGateway,
ec2:DeleteTags,
ec2:ModifyTransitGateway,
ec2:ModifyTransitGatewayOptions
```
