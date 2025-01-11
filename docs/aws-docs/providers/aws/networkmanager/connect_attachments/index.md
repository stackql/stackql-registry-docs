---
title: connect_attachments
hide_title: false
hide_table_of_contents: false
keywords:
  - connect_attachments
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

Creates, updates, deletes or gets a <code>connect_attachment</code> resource or lists <code>connect_attachments</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connect_attachments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>AWS::NetworkManager::ConnectAttachment Resource Type Definition</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.networkmanager.connect_attachments" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="core_network_id" /></td><td><code>string</code></td><td>ID of the CoreNetwork that the attachment will be attached to.</td></tr>
<tr><td><CopyableCode code="core_network_arn" /></td><td><code>string</code></td><td>The ARN of a core network.</td></tr>
<tr><td><CopyableCode code="attachment_id" /></td><td><code>string</code></td><td>The ID of the attachment.</td></tr>
<tr><td><CopyableCode code="owner_account_id" /></td><td><code>string</code></td><td>The ID of the attachment account owner.</td></tr>
<tr><td><CopyableCode code="attachment_type" /></td><td><code>string</code></td><td>The type of attachment.</td></tr>
<tr><td><CopyableCode code="state" /></td><td><code>string</code></td><td>State of the attachment.</td></tr>
<tr><td><CopyableCode code="edge_location" /></td><td><code>string</code></td><td>Edge location of the attachment.</td></tr>
<tr><td><CopyableCode code="resource_arn" /></td><td><code>string</code></td><td>The attachment resource ARN.</td></tr>
<tr><td><CopyableCode code="attachment_policy_rule_number" /></td><td><code>integer</code></td><td>The policy rule number associated with the attachment.</td></tr>
<tr><td><CopyableCode code="segment_name" /></td><td><code>string</code></td><td>The name of the segment attachment.</td></tr>
<tr><td><CopyableCode code="proposed_segment_change" /></td><td><code>object</code></td><td>The attachment to move from one segment to another.</td></tr>
<tr><td><CopyableCode code="network_function_group_name" /></td><td><code>string</code></td><td>The name of the network function group attachment.</td></tr>
<tr><td><CopyableCode code="proposed_network_function_group_change" /></td><td><code>object</code></td><td>The attachment to move from one network function group to another.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>Tags for the attachment.</td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td>Creation time of the attachment.</td></tr>
<tr><td><CopyableCode code="updated_at" /></td><td><code>string</code></td><td>Last update time of the attachment.</td></tr>
<tr><td><CopyableCode code="transport_attachment_id" /></td><td><code>string</code></td><td>Id of transport attachment</td></tr>
<tr><td><CopyableCode code="options" /></td><td><code>object</code></td><td>Protocol options for connect attachment</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-connectattachment.html"><code>AWS::NetworkManager::ConnectAttachment</code></a>.

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
    <td><CopyableCode code="CoreNetworkId, EdgeLocation, TransportAttachmentId, Options, region" /></td>
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
Gets all <code>connect_attachments</code> in a region.
```sql
SELECT
region,
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
tags,
created_at,
updated_at,
transport_attachment_id,
options
FROM aws.networkmanager.connect_attachments
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>connect_attachment</code>.
```sql
SELECT
region,
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
tags,
created_at,
updated_at,
transport_attachment_id,
options
FROM aws.networkmanager.connect_attachments
WHERE region = 'us-east-1' AND data__Identifier = '<AttachmentId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>connect_attachment</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.networkmanager.connect_attachments (
 CoreNetworkId,
 EdgeLocation,
 TransportAttachmentId,
 Options,
 region
)
SELECT 
'{{ CoreNetworkId }}',
 '{{ EdgeLocation }}',
 '{{ TransportAttachmentId }}',
 '{{ Options }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.networkmanager.connect_attachments (
 CoreNetworkId,
 EdgeLocation,
 ProposedSegmentChange,
 NetworkFunctionGroupName,
 ProposedNetworkFunctionGroupChange,
 Tags,
 TransportAttachmentId,
 Options,
 region
)
SELECT 
 '{{ CoreNetworkId }}',
 '{{ EdgeLocation }}',
 '{{ ProposedSegmentChange }}',
 '{{ NetworkFunctionGroupName }}',
 '{{ ProposedNetworkFunctionGroupChange }}',
 '{{ Tags }}',
 '{{ TransportAttachmentId }}',
 '{{ Options }}',
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
  - name: connect_attachment
    props:
      - name: CoreNetworkId
        value: '{{ CoreNetworkId }}'
      - name: EdgeLocation
        value: '{{ EdgeLocation }}'
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
      - name: TransportAttachmentId
        value: '{{ TransportAttachmentId }}'
      - name: Options
        value:
          Protocol: '{{ Protocol }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.networkmanager.connect_attachments
WHERE data__Identifier = '<AttachmentId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>connect_attachments</code> resource, the following permissions are required:

### Create
```json
networkmanager:GetConnectAttachment,
networkmanager:CreateConnectAttachment,
networkmanager:TagResource,
ec2:DescribeRegions
```

### Read
```json
networkmanager:GetConnectAttachment
```

### Update
```json
networkmanager:GetConnectAttachment,
networkmanager:ListTagsForResource,
networkmanager:TagResource,
networkmanager:UntagResource,
ec2:DescribeRegions
```

### Delete
```json
networkmanager:GetConnectAttachment,
networkmanager:DeleteAttachment,
ec2:DescribeRegions
```

### List
```json
networkmanager:ListAttachments
```
