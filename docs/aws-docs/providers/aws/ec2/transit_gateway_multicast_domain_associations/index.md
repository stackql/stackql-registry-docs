---
title: transit_gateway_multicast_domain_associations
hide_title: false
hide_table_of_contents: false
keywords:
  - transit_gateway_multicast_domain_associations
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

Used to retrieve a list of <code>transit_gateway_multicast_domain_associations</code> in a region or create a <code>transit_gateway_multicast_domain_associations</code> resource, use <code>transit_gateway_multicast_domain_association</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>transit_gateway_multicast_domain_associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::EC2::TransitGatewayMulticastDomainAssociation type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.transit_gateway_multicast_domain_associations" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="transit_gateway_multicast_domain_id" /></td><td><code>string</code></td><td>The ID of the transit gateway multicast domain.</td></tr>
<tr><td><CopyableCode code="transit_gateway_attachment_id" /></td><td><code>string</code></td><td>The ID of the transit gateway attachment.</td></tr>
<tr><td><CopyableCode code="subnet_id" /></td><td><code>string</code></td><td>The IDs of the subnets to associate with the transit gateway multicast domain.</td></tr>
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
transit_gateway_attachment_id,
subnet_id
FROM aws.ec2.transit_gateway_multicast_domain_associations
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>transit_gateway_multicast_domain_associations</code> resource, the following permissions are required:

### Create
```json
ec2:AssociateTransitGatewayMulticastDomain,
ec2:GetTransitGatewayMulticastDomainAssociations
```

### List
```json
ec2:GetTransitGatewayMulticastDomainAssociations
```

