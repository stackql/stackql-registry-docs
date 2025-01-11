---
title: transit_gateway_peering_attachments
hide_title: false
hide_table_of_contents: false
keywords:
  - transit_gateway_peering_attachments
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

Creates, updates, deletes or gets a <code>transit_gateway_peering_attachment</code> resource or lists <code>transit_gateway_peering_attachments</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>transit_gateway_peering_attachments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::EC2::TransitGatewayPeeringAttachment type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.transit_gateway_peering_attachments" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="status" /></td><td><code>object</code></td><td>The status of the transit gateway peering attachment.</td></tr>
<tr><td><CopyableCode code="transit_gateway_id" /></td><td><code>string</code></td><td>The ID of the transit gateway.</td></tr>
<tr><td><CopyableCode code="peer_transit_gateway_id" /></td><td><code>string</code></td><td>The ID of the peer transit gateway.</td></tr>
<tr><td><CopyableCode code="peer_account_id" /></td><td><code>string</code></td><td>The ID of the peer account</td></tr>
<tr><td><CopyableCode code="state" /></td><td><code>string</code></td><td>The state of the transit gateway peering attachment. Note that the initiating state has been deprecated.</td></tr>
<tr><td><CopyableCode code="creation_time" /></td><td><code>string</code></td><td>The time the transit gateway peering attachment was created.</td></tr>
<tr><td><CopyableCode code="peer_region" /></td><td><code>string</code></td><td>Peer Region</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The tags for the transit gateway peering attachment.</td></tr>
<tr><td><CopyableCode code="transit_gateway_attachment_id" /></td><td><code>string</code></td><td>The ID of the transit gateway peering attachment.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewaypeeringattachment.html"><code>AWS::EC2::TransitGatewayPeeringAttachment</code></a>.

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
    <td><CopyableCode code="TransitGatewayId, PeerTransitGatewayId, PeerAccountId, PeerRegion, region" /></td>
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
Gets all <code>transit_gateway_peering_attachments</code> in a region.
```sql
SELECT
region,
status,
transit_gateway_id,
peer_transit_gateway_id,
peer_account_id,
state,
creation_time,
peer_region,
tags,
transit_gateway_attachment_id
FROM aws.ec2.transit_gateway_peering_attachments
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>transit_gateway_peering_attachment</code>.
```sql
SELECT
region,
status,
transit_gateway_id,
peer_transit_gateway_id,
peer_account_id,
state,
creation_time,
peer_region,
tags,
transit_gateway_attachment_id
FROM aws.ec2.transit_gateway_peering_attachments
WHERE region = 'us-east-1' AND data__Identifier = '<TransitGatewayAttachmentId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>transit_gateway_peering_attachment</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.ec2.transit_gateway_peering_attachments (
 TransitGatewayId,
 PeerTransitGatewayId,
 PeerAccountId,
 PeerRegion,
 region
)
SELECT 
'{{ TransitGatewayId }}',
 '{{ PeerTransitGatewayId }}',
 '{{ PeerAccountId }}',
 '{{ PeerRegion }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.ec2.transit_gateway_peering_attachments (
 TransitGatewayId,
 PeerTransitGatewayId,
 PeerAccountId,
 PeerRegion,
 Tags,
 region
)
SELECT 
 '{{ TransitGatewayId }}',
 '{{ PeerTransitGatewayId }}',
 '{{ PeerAccountId }}',
 '{{ PeerRegion }}',
 '{{ Tags }}',
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
  - name: transit_gateway_peering_attachment
    props:
      - name: TransitGatewayId
        value: '{{ TransitGatewayId }}'
      - name: PeerTransitGatewayId
        value: '{{ PeerTransitGatewayId }}'
      - name: PeerAccountId
        value: '{{ PeerAccountId }}'
      - name: PeerRegion
        value: '{{ PeerRegion }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.ec2.transit_gateway_peering_attachments
WHERE data__Identifier = '<TransitGatewayAttachmentId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>transit_gateway_peering_attachments</code> resource, the following permissions are required:

### Read
```json
ec2:DescribeTransitGatewayPeeringAttachments
```

### Create
```json
ec2:CreateTransitGatewayPeeringAttachment,
ec2:DescribeTransitGatewayPeeringAttachments,
ec2:CreateTags
```

### Update
```json
ec2:DescribeTransitGatewayPeeringAttachments,
ec2:CreateTags,
ec2:DeleteTags
```

### List
```json
ec2:DescribeTransitGatewayPeeringAttachments
```

### Delete
```json
ec2:DeleteTransitGatewayPeeringAttachment,
ec2:DescribeTransitGatewayPeeringAttachments,
ec2:DeleteTags
```
