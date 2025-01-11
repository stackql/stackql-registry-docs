---
title: transit_gateway_routes
hide_title: false
hide_table_of_contents: false
keywords:
  - transit_gateway_routes
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

Creates, updates, deletes or gets a <code>transit_gateway_route</code> resource or lists <code>transit_gateway_routes</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>transit_gateway_routes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EC2::TransitGatewayRoute</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.transit_gateway_routes" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="transit_gateway_route_table_id" /></td><td><code>string</code></td><td>The ID of transit gateway route table.</td></tr>
<tr><td><CopyableCode code="destination_cidr_block" /></td><td><code>string</code></td><td>The CIDR range used for destination matches. Routing decisions are based on the most specific match.</td></tr>
<tr><td><CopyableCode code="blackhole" /></td><td><code>boolean</code></td><td>Indicates whether to drop traffic that matches this route.</td></tr>
<tr><td><CopyableCode code="transit_gateway_attachment_id" /></td><td><code>string</code></td><td>The ID of transit gateway attachment.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayroute.html"><code>AWS::EC2::TransitGatewayRoute</code></a>.

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
    <td><CopyableCode code="TransitGatewayRouteTableId, DestinationCidrBlock, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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
Gets all <code>transit_gateway_routes</code> in a region.
```sql
SELECT
region,
transit_gateway_route_table_id,
destination_cidr_block,
blackhole,
transit_gateway_attachment_id
FROM aws.ec2.transit_gateway_routes
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>transit_gateway_route</code>.
```sql
SELECT
region,
transit_gateway_route_table_id,
destination_cidr_block,
blackhole,
transit_gateway_attachment_id
FROM aws.ec2.transit_gateway_routes
WHERE region = 'us-east-1' AND data__Identifier = '<TransitGatewayRouteTableId>|<DestinationCidrBlock>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>transit_gateway_route</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.ec2.transit_gateway_routes (
 TransitGatewayRouteTableId,
 DestinationCidrBlock,
 region
)
SELECT 
'{{ TransitGatewayRouteTableId }}',
 '{{ DestinationCidrBlock }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.ec2.transit_gateway_routes (
 TransitGatewayRouteTableId,
 DestinationCidrBlock,
 Blackhole,
 TransitGatewayAttachmentId,
 region
)
SELECT 
 '{{ TransitGatewayRouteTableId }}',
 '{{ DestinationCidrBlock }}',
 '{{ Blackhole }}',
 '{{ TransitGatewayAttachmentId }}',
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
  - name: transit_gateway_route
    props:
      - name: TransitGatewayRouteTableId
        value: '{{ TransitGatewayRouteTableId }}'
      - name: DestinationCidrBlock
        value: '{{ DestinationCidrBlock }}'
      - name: Blackhole
        value: '{{ Blackhole }}'
      - name: TransitGatewayAttachmentId
        value: '{{ TransitGatewayAttachmentId }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.ec2.transit_gateway_routes
WHERE data__Identifier = '<TransitGatewayRouteTableId|DestinationCidrBlock>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>transit_gateway_routes</code> resource, the following permissions are required:

### Read
```json
ec2:SearchTransitGatewayRoutes
```

### Create
```json
ec2:CreateTransitGatewayRoute,
ec2:SearchTransitGatewayRoutes
```

### List
```json
ec2:SearchTransitGatewayRoutes
```

### Delete
```json
ec2:DeleteTransitGatewayRoute,
ec2:SearchTransitGatewayRoutes
```
