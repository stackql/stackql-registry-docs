---
title: direct_connect_gateway_attachments
hide_title: false
hide_table_of_contents: false
keywords:
  - direct_connect_gateway_attachments
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

Creates, updates, deletes or gets a <code>direct_connect_gateway_attachment</code> resource or lists <code>direct_connect_gateway_attachments</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>direct_connect_gateway_attachments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>AWS::NetworkManager::DirectConnectGatewayAttachment Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.networkmanager.direct_connect_gateway_attachments" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="core_network_id" /></td><td><code>string</code></td><td>The ID of a core network for the Direct Connect Gateway attachment.</td></tr>
<tr><td><CopyableCode code="core_network_arn" /></td><td><code>string</code></td><td>The ARN of a core network for the Direct Connect Gateway attachment.</td></tr>
<tr><td><CopyableCode code="attachment_id" /></td><td><code>string</code></td><td>Id of the attachment.</td></tr>
<tr><td><CopyableCode code="owner_account_id" /></td><td><code>string</code></td><td>Owner account of the attachment.</td></tr>
<tr><td><CopyableCode code="attachment_type" /></td><td><code>string</code></td><td>Attachment type.</td></tr>
<tr><td><CopyableCode code="state" /></td><td><code>string</code></td><td>State of the attachment.</td></tr>
<tr><td><CopyableCode code="edge_locations" /></td><td><code>array</code></td><td>The Regions where the edges are located.</td></tr>
<tr><td><CopyableCode code="direct_connect_gateway_arn" /></td><td><code>string</code></td><td>The ARN of the Direct Connect Gateway.</td></tr>
<tr><td><CopyableCode code="resource_arn" /></td><td><code>string</code></td><td>The ARN of the Resource.</td></tr>
<tr><td><CopyableCode code="attachment_policy_rule_number" /></td><td><code>integer</code></td><td>The policy rule number associated with the attachment.</td></tr>
<tr><td><CopyableCode code="segment_name" /></td><td><code>string</code></td><td>The name of the segment attachment..</td></tr>
<tr><td><CopyableCode code="proposed_segment_change" /></td><td><code>object</code></td><td>The attachment to move from one segment to another.</td></tr>
<tr><td><CopyableCode code="network_function_group_name" /></td><td><code>string</code></td><td>The name of the network function group attachment.</td></tr>
<tr><td><CopyableCode code="proposed_network_function_group_change" /></td><td><code>object</code></td><td>The attachment to move from one network function group to another.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>Tags for the attachment.</td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td>Creation time of the attachment.</td></tr>
<tr><td><CopyableCode code="updated_at" /></td><td><code>string</code></td><td>Last update time of the attachment.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-directconnectgatewayattachment.html"><code>AWS::NetworkManager::DirectConnectGatewayAttachment</code></a>.

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
    <td><CopyableCode code="CoreNetworkId, DirectConnectGatewayArn, EdgeLocations, region" /></td>
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
Gets all <code>direct_connect_gateway_attachments</code> in a region.
```sql
SELECT
region,
core_network_id,
core_network_arn,
attachment_id,
owner_account_id,
attachment_type,
state,
edge_locations,
direct_connect_gateway_arn,
resource_arn,
attachment_policy_rule_number,
segment_name,
proposed_segment_change,
network_function_group_name,
proposed_network_function_group_change,
tags,
created_at,
updated_at
FROM aws.networkmanager.direct_connect_gateway_attachments
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>direct_connect_gateway_attachment</code>.
```sql
SELECT
region,
core_network_id,
core_network_arn,
attachment_id,
owner_account_id,
attachment_type,
state,
edge_locations,
direct_connect_gateway_arn,
resource_arn,
attachment_policy_rule_number,
segment_name,
proposed_segment_change,
network_function_group_name,
proposed_network_function_group_change,
tags,
created_at,
updated_at
FROM aws.networkmanager.direct_connect_gateway_attachments
WHERE region = 'us-east-1' AND data__Identifier = '<AttachmentId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>direct_connect_gateway_attachment</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.networkmanager.direct_connect_gateway_attachments (
 CoreNetworkId,
 EdgeLocations,
 DirectConnectGatewayArn,
 region
)
SELECT 
'{{ CoreNetworkId }}',
 '{{ EdgeLocations }}',
 '{{ DirectConnectGatewayArn }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.networkmanager.direct_connect_gateway_attachments (
 CoreNetworkId,
 EdgeLocations,
 DirectConnectGatewayArn,
 ProposedSegmentChange,
 ProposedNetworkFunctionGroupChange,
 Tags,
 region
)
SELECT 
 '{{ CoreNetworkId }}',
 '{{ EdgeLocations }}',
 '{{ DirectConnectGatewayArn }}',
 '{{ ProposedSegmentChange }}',
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
  - name: direct_connect_gateway_attachment
    props:
      - name: CoreNetworkId
        value: '{{ CoreNetworkId }}'
      - name: EdgeLocations
        value:
          - '{{ EdgeLocations[0] }}'
      - name: DirectConnectGatewayArn
        value: '{{ DirectConnectGatewayArn }}'
      - name: ProposedSegmentChange
        value:
          Tags:
            - Key: '{{ Key }}'
              Value: '{{ Value }}'
          AttachmentPolicyRuleNumber: '{{ AttachmentPolicyRuleNumber }}'
          SegmentName: '{{ SegmentName }}'
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
DELETE FROM aws.networkmanager.direct_connect_gateway_attachments
WHERE data__Identifier = '<AttachmentId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>direct_connect_gateway_attachments</code> resource, the following permissions are required:

### Create
```json
networkmanager:CreateDirectConnectGatewayAttachment,
networkmanager:GetDirectConnectGatewayAttachment,
networkmanager:TagResource,
ec2:DescribeRegions,
iam:CreateServiceLinkedRole
```

### Read
```json
networkmanager:GetDirectConnectGatewayAttachment
```

### Update
```json
networkmanager:UpdateDirectConnectGatewayAttachment,
networkmanager:GetDirectConnectGatewayAttachment,
networkmanager:ListTagsForResource,
networkmanager:TagResource,
networkmanager:UntagResource,
ec2:DescribeRegions
```

### Delete
```json
networkmanager:DeleteAttachment,
networkmanager:GetDirectConnectGatewayAttachment,
networkmanager:UntagResource,
ec2:DescribeRegions
```

### List
```json
networkmanager:ListAttachments
```
