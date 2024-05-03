---
title: transit_gateway_route_table_association
hide_title: false
hide_table_of_contents: false
keywords:
  - transit_gateway_route_table_association
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

Gets or operates on an individual <code>transit_gateway_route_table_association</code> resource, use <code>transit_gateway_route_table_associations</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>transit_gateway_route_table_association</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EC2::TransitGatewayRouteTableAssociation</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.transit_gateway_route_table_association" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="transit_gateway_route_table_id" /></td><td><code>string</code></td><td>The ID of transit gateway route table.</td></tr>
<tr><td><CopyableCode code="transit_gateway_attachment_id" /></td><td><code>string</code></td><td>The ID of transit gateway attachment.</td></tr>
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
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
transit_gateway_route_table_id,
transit_gateway_attachment_id
FROM aws.ec2.transit_gateway_route_table_association
WHERE data__Identifier = '<TransitGatewayRouteTableId>|<TransitGatewayAttachmentId>';
```

## Permissions

To operate on the <code>transit_gateway_route_table_association</code> resource, the following permissions are required:

### Read
```json
ec2:GetTransitGatewayRouteTableAssociations
```

### Delete
```json
ec2:GetTransitGatewayRouteTableAssociations,
ec2:DisassociateTransitGatewayRouteTable
```

