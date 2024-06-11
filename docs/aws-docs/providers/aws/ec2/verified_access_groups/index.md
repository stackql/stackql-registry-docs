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

Creates, updates, deletes or gets a <code>verified_access_group</code> resource or lists <code>verified_access_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>verified_access_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::EC2::VerifiedAccessGroup resource creates an AWS EC2 Verified Access Group.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.verified_access_groups" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="verified_access_group_id" /></td><td><code>string</code></td><td>The ID of the AWS Verified Access group.</td></tr>
<tr><td><CopyableCode code="verified_access_instance_id" /></td><td><code>string</code></td><td>The ID of the AWS Verified Access instance.</td></tr>
<tr><td><CopyableCode code="verified_access_group_arn" /></td><td><code>string</code></td><td>The ARN of the Verified Access group.</td></tr>
<tr><td><CopyableCode code="owner" /></td><td><code>string</code></td><td>The AWS account number that owns the group.</td></tr>
<tr><td><CopyableCode code="creation_time" /></td><td><code>string</code></td><td>Time this Verified Access Group was created.</td></tr>
<tr><td><CopyableCode code="last_updated_time" /></td><td><code>string</code></td><td>Time this Verified Access Group was last updated.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A description for the AWS Verified Access group.</td></tr>
<tr><td><CopyableCode code="policy_document" /></td><td><code>string</code></td><td>The AWS Verified Access policy document.</td></tr>
<tr><td><CopyableCode code="policy_enabled" /></td><td><code>boolean</code></td><td>The status of the Verified Access policy.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="sse_specification" /></td><td><code>object</code></td><td>The configuration options for customer provided KMS encryption.</td></tr>
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
    <td><CopyableCode code="VerifiedAccessInstanceId, region" /></td>
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
    <td><CopyableCode code="list_resource" /></td>
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
List all <code>verified_access_groups</code> in a region.
```sql
SELECT
region,
verified_access_group_id
FROM aws.ec2.verified_access_groups
WHERE region = 'us-east-1';
```
Gets all properties from a <code>verified_access_group</code>.
```sql
SELECT
region,
verified_access_group_id,
verified_access_instance_id,
verified_access_group_arn,
owner,
creation_time,
last_updated_time,
description,
policy_document,
policy_enabled,
tags,
sse_specification
FROM aws.ec2.verified_access_groups
WHERE region = 'us-east-1' AND data__Identifier = '<VerifiedAccessGroupId>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>verified_access_group</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.ec2.verified_access_groups (
 VerifiedAccessInstanceId,
 region
)
SELECT 
'{{ VerifiedAccessInstanceId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
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
 '{{ VerifiedAccessInstanceId }}',
 '{{ Description }}',
 '{{ PolicyDocument }}',
 '{{ PolicyEnabled }}',
 '{{ Tags }}',
 '{{ SseSpecification }}',
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
  - name: verified_access_group
    props:
      - name: VerifiedAccessInstanceId
        value: '{{ VerifiedAccessInstanceId }}'
      - name: Description
        value: '{{ Description }}'
      - name: PolicyDocument
        value: '{{ PolicyDocument }}'
      - name: PolicyEnabled
        value: '{{ PolicyEnabled }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: SseSpecification
        value:
          KmsKeyArn: '{{ KmsKeyArn }}'
          CustomerManagedKeyEnabled: '{{ CustomerManagedKeyEnabled }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
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

### Read
```json
ec2:DescribeVerifiedAccessGroups,
ec2:GetVerifiedAccessGroupPolicy,
ec2:DescribeTags,
kms:DescribeKey,
kms:RetireGrant,
kms:CreateGrant,
kms:GenerateDataKey,
kms:Decrypt
```

### Update
```json
ec2:ModifyVerifiedAccessGroup,
ec2:ModifyVerifiedAccessGroupPolicy,
ec2:DescribeVerifiedAccessGroups,
ec2:GetVerifiedAccessGroupPolicy,
ec2:DescribeTags,
ec2:DeleteTags,
ec2:CreateTags,
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

