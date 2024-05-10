---
title: verified_access_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - verified_access_groups
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


Used to retrieve a list of <code>verified_access_groups</code> in a region or to create or delete a <code>verified_access_groups</code> resource, use <code>verified_access_group</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>verified_access_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::EC2::VerifiedAccessGroup resource creates an AWS EC2 Verified Access Group.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.verified_access_groups" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="verified_access_group_id" /></td><td><code>string</code></td><td>The ID of the AWS Verified Access group.</td></tr>
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
verified_access_group_id
FROM aws.ec2.verified_access_groups
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
 "VerifiedAccessInstanceId": "{{ VerifiedAccessInstanceId }}"
}
>>>
--required properties only
INSERT INTO aws.ec2.verified_access_groups (
 VerifiedAccessInstanceId,
 region
)
SELECT 
{{ .VerifiedAccessInstanceId }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "VerifiedAccessInstanceId": "{{ VerifiedAccessInstanceId }}",
 "Description": "{{ Description }}",
 "PolicyDocument": "{{ PolicyDocument }}",
 "PolicyEnabled": "{{ PolicyEnabled }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ],
 "SseSpecification": {
  "KmsKeyArn": "{{ KmsKeyArn }}",
  "CustomerManagedKeyEnabled": "{{ CustomerManagedKeyEnabled }}"
 }
}
>>>
--all properties
INSERT INTO aws.ec2.verified_access_groups (
 VerifiedAccessInstanceId,
 Description,
 PolicyDocument,
 PolicyEnabled,
 Tags,
 SseSpecification,
 region
)
SELECT 
 {{ .VerifiedAccessInstanceId }},
 {{ .Description }},
 {{ .PolicyDocument }},
 {{ .PolicyEnabled }},
 {{ .Tags }},
 {{ .SseSpecification }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.ec2.verified_access_groups
WHERE data__Identifier = '<VerifiedAccessGroupId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>verified_access_groups</code> resource, the following permissions are required:

### Create
```json
ec2:CreateVerifiedAccessGroup,
ec2:DescribeVerifiedAccessGroups,
ec2:GetVerifiedAccessGroupPolicy,
ec2:CreateTags,
ec2:DescribeTags,
kms:DescribeKey,
kms:RetireGrant,
kms:CreateGrant,
kms:GenerateDataKey,
kms:Decrypt
```

### Delete
```json
ec2:DeleteVerifiedAccessGroup,
ec2:DeleteTags,
ec2:DescribeVerifiedAccessGroups,
ec2:DescribeTags,
kms:DescribeKey,
kms:RetireGrant,
kms:CreateGrant,
kms:GenerateDataKey,
kms:Decrypt
```

### List
```json
ec2:DescribeVerifiedAccessGroups,
ec2:DescribeTags,
kms:DescribeKey,
kms:RetireGrant,
kms:CreateGrant,
kms:GenerateDataKey,
kms:Decrypt
```

