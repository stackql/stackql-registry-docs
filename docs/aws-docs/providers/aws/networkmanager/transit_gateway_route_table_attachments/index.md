---
title: transit_gateway_route_table_attachments
hide_title: false
hide_table_of_contents: false
keywords:
  - transit_gateway_route_table_attachments
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

Creates, updates, deletes or gets a <code>transit_gateway_route_table_attachment</code> resource or lists <code>transit_gateway_route_table_attachments</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>transit_gateway_route_table_attachments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>AWS::NetworkManager::TransitGatewayRouteTableAttachment Resource Type definition.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.networkmanager.transit_gateway_route_table_attachments" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="peering_id" /></td><td><code>string</code></td><td>The Id of peering between transit gateway and core network.</td></tr>
<tr><td><CopyableCode code="transit_gateway_route_table_arn" /></td><td><code>string</code></td><td>The Arn of transit gateway route table.</td></tr>
<tr><td><CopyableCode code="core_network_id" /></td><td><code>string</code></td><td>The ID of a core network where you're creating a site-to-site VPN attachment.</td></tr>
<tr><td><CopyableCode code="core_network_arn" /></td><td><code>string</code></td><td>The ARN of a core network for the VPC attachment.</td></tr>
<tr><td><CopyableCode code="attachment_id" /></td><td><code>string</code></td><td>The ID of the attachment.</td></tr>
<tr><td><CopyableCode code="owner_account_id" /></td><td><code>string</code></td><td>Owner account of the attachment.</td></tr>
<tr><td><CopyableCode code="attachment_type" /></td><td><code>string</code></td><td>The type of attachment.</td></tr>
<tr><td><CopyableCode code="state" /></td><td><code>string</code></td><td>The state of the attachment.</td></tr>
<tr><td><CopyableCode code="edge_location" /></td><td><code>string</code></td><td>The Region where the edge is located.</td></tr>
<tr><td><CopyableCode code="resource_arn" /></td><td><code>string</code></td><td>The ARN of the Resource.</td></tr>
<tr><td><CopyableCode code="attachment_policy_rule_number" /></td><td><code>integer</code></td><td>The policy rule number associated with the attachment.</td></tr>
<tr><td><CopyableCode code="segment_name" /></td><td><code>string</code></td><td>The name of the segment that attachment is in.</td></tr>
<tr><td><CopyableCode code="proposed_segment_change" /></td><td><code>object</code></td><td>The attachment to move from one segment to another.</td></tr>
<tr><td><CopyableCode code="network_function_group_name" /></td><td><code>string</code></td><td>The name of the network function group attachment.</td></tr>
<tr><td><CopyableCode code="proposed_network_function_group_change" /></td><td><code>object</code></td><td>The attachment to move from one network function group to another.</td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td>Creation time of the attachment.</td></tr>
<tr><td><CopyableCode code="updated_at" /></td><td><code>string</code></td><td>Last update time of the attachment.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-transitgatewayroutetableattachment.html"><code>AWS::NetworkManager::TransitGatewayRouteTableAttachment</code></a>.

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
    <td><CopyableCode code="PeeringId, TransitGatewayRouteTableArn, region" /></td>
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
Gets all <code>transit_gateway_route_table_attachments</code> in a region.
```sql
SELECT
region,
peering_id,
transit_gateway_route_table_arn,
core_network_id,
core_network_arn,
attachment_id,
owner_account_id,
attachment_type,
state,
edge_location,
resource_arn,
attachment_policy_rule_number,
segment_name,
proposed_segment_change,
network_function_group_name,
proposed_network_function_group_change,
created_at,
updated_at,
tags
FROM aws.networkmanager.transit_gateway_route_table_attachments
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>transit_gateway_route_table_attachment</code>.
```sql
SELECT
region,
peering_id,
transit_gateway_route_table_arn,
core_network_id,
core_network_arn,
attachment_id,
owner_account_id,
attachment_type,
state,
edge_location,
resource_arn,
attachment_policy_rule_number,
segment_name,
proposed_segment_change,
network_function_group_name,
proposed_network_function_group_change,
created_at,
updated_at,
tags
FROM aws.networkmanager.transit_gateway_route_table_attachments
WHERE region = 'us-east-1' AND data__Identifier = '<AttachmentId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>transit_gateway_route_table_attachment</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.networkmanager.transit_gateway_route_table_attachments (
 PeeringId,
 TransitGatewayRouteTableArn,
 region
)
SELECT 
'{{ PeeringId }}',
 '{{ TransitGatewayRouteTableArn }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.networkmanager.transit_gateway_route_table_attachments (
 PeeringId,
 TransitGatewayRouteTableArn,
 ProposedSegmentChange,
 NetworkFunctionGroupName,
 ProposedNetworkFunctionGroupChange,
 Tags,
 region
)
SELECT 
 '{{ PeeringId }}',
 '{{ TransitGatewayRouteTableArn }}',
 '{{ ProposedSegmentChange }}',
 '{{ NetworkFunctionGroupName }}',
 '{{ ProposedNetworkFunctionGroupChange }}',
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
  - name: transit_gateway_route_table_attachment
    props:
      - name: PeeringId
        value: '{{ PeeringId }}'
      - name: TransitGatewayRouteTableArn
        value: '{{ TransitGatewayRouteTableArn }}'
      - name: ProposedSegmentChange
        value:
          Tags:
            - Key: '{{ Key }}'
              Value: '{{ Value }}'
          AttachmentPolicyRuleNumber: '{{ AttachmentPolicyRuleNumber }}'
          SegmentName: '{{ SegmentName }}'
      - name: NetworkFunctionGroupName
        value: '{{ NetworkFunctionGroupName }}'
      - name: ProposedNetworkFunctionGroupChange
        value:
          Tags:
            - null
          AttachmentPolicyRuleNumber: '{{ AttachmentPolicyRuleNumber }}'
          NetworkFunctionGroupName: '{{ NetworkFunctionGroupName }}'
      - name: Tags
        value:
          - null

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.networkmanager.transit_gateway_route_table_attachments
WHERE data__Identifier = '<AttachmentId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>transit_gateway_route_table_attachments</code> resource, the following permissions are required:

### Create
```json
networkmanager:CreateTransitGatewayRouteTableAttachment,
networkmanager:GetTransitGatewayRouteTableAttachment,
networkmanager:TagResource,
iam:CreateServiceLinkedRole,
ec2:DescribeRegions
```

### Read
```json
networkmanager:GetTransitGatewayRouteTableAttachment
```

### Update
```json
networkmanager:GetTransitGatewayRouteTableAttachment,
networkmanager:ListTagsForResource,
networkmanager:TagResource,
networkmanager:UntagResource,
ec2:DescribeRegions
```

### Delete
```json
networkmanager:GetTransitGatewayRouteTableAttachment,
networkmanager:DeleteAttachment,
ec2:DescribeRegions
```

### List
```json
networkmanager:ListAttachments
```
