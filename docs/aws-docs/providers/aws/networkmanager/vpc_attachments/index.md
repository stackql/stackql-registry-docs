---
title: vpc_attachments
hide_title: false
hide_table_of_contents: false
keywords:
  - vpc_attachments
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


Used to retrieve a list of <code>vpc_attachments</code> in a region or to create or delete a <code>vpc_attachments</code> resource, use <code>vpc_attachment</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpc_attachments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>AWS::NetworkManager::VpcAttachment Resoruce Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.networkmanager.vpc_attachments" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="attachment_id" /></td><td><code>string</code></td><td>Id of the attachment.</td></tr>
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
attachment_id
FROM aws.networkmanager.vpc_attachments
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
 "CoreNetworkId": "{{ CoreNetworkId }}",
 "VpcArn": "{{ VpcArn }}",
 "SubnetArns": [
  "{{ SubnetArns[0] }}"
 ]
}
>>>
--required properties only
INSERT INTO aws.networkmanager.vpc_attachments (
 CoreNetworkId,
 VpcArn,
 SubnetArns,
 region
)
SELECT 
{{ .CoreNetworkId }},
 {{ .VpcArn }},
 {{ .SubnetArns }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "CoreNetworkId": "{{ CoreNetworkId }}",
 "VpcArn": "{{ VpcArn }}",
 "ProposedSegmentChange": {
  "Tags": [
   {
    "Key": "{{ Key }}",
    "Value": "{{ Value }}"
   }
  ],
  "AttachmentPolicyRuleNumber": "{{ AttachmentPolicyRuleNumber }}",
  "SegmentName": "{{ SegmentName }}"
 },
 "Tags": [
  null
 ],
 "SubnetArns": [
  "{{ SubnetArns[0] }}"
 ],
 "Options": {
  "Ipv6Support": "{{ Ipv6Support }}",
  "ApplianceModeSupport": "{{ ApplianceModeSupport }}"
 }
}
>>>
--all properties
INSERT INTO aws.networkmanager.vpc_attachments (
 CoreNetworkId,
 VpcArn,
 ProposedSegmentChange,
 Tags,
 SubnetArns,
 Options,
 region
)
SELECT 
 {{ .CoreNetworkId }},
 {{ .VpcArn }},
 {{ .ProposedSegmentChange }},
 {{ .Tags }},
 {{ .SubnetArns }},
 {{ .Options }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.networkmanager.vpc_attachments
WHERE data__Identifier = '<AttachmentId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>vpc_attachments</code> resource, the following permissions are required:

### Create
```json
networkmanager:CreateVpcAttachment,
networkmanager:GetVpcAttachment,
networkmanager:TagResource,
ec2:DescribeRegions,
iam:CreateServiceLinkedRole
```

### Delete
```json
networkmanager:DeleteAttachment,
networkmanager:GetVpcAttachment,
networkmanager:UntagResource,
ec2:DescribeRegions
```

### List
```json
networkmanager:ListAttachments
```

