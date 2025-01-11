---
title: billing_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - billing_groups
  - billingconductor
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

Creates, updates, deletes or gets a <code>billing_group</code> resource or lists <code>billing_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>billing_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A billing group is a set of linked account which belong to the same end customer. It can be seen as a virtual consolidated billing family.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.billingconductor.billing_groups" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Billing Group ARN</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="primary_account_id" /></td><td><code>string</code></td><td>This account will act as a virtual payer account of the billing group</td></tr>
<tr><td><CopyableCode code="computation_preference" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="account_grouping" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="size" /></td><td><code>integer</code></td><td>Number of accounts in the billing group</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="status_reason" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="creation_time" /></td><td><code>integer</code></td><td>Creation timestamp in UNIX epoch time format</td></tr>
<tr><td><CopyableCode code="last_modified_time" /></td><td><code>integer</code></td><td>Latest modified timestamp in UNIX epoch time format</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-billinggroup.html"><code>AWS::BillingConductor::BillingGroup</code></a>.

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
    <td><CopyableCode code="Name, AccountGrouping, PrimaryAccountId, ComputationPreference, region" /></td>
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
Gets all <code>billing_groups</code> in a region.
```sql
SELECT
region,
arn,
name,
description,
primary_account_id,
computation_preference,
account_grouping,
size,
status,
status_reason,
creation_time,
last_modified_time,
tags
FROM aws.billingconductor.billing_groups
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>billing_group</code>.
```sql
SELECT
region,
arn,
name,
description,
primary_account_id,
computation_preference,
account_grouping,
size,
status,
status_reason,
creation_time,
last_modified_time,
tags
FROM aws.billingconductor.billing_groups
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>billing_group</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.billingconductor.billing_groups (
 Name,
 PrimaryAccountId,
 ComputationPreference,
 AccountGrouping,
 region
)
SELECT 
'{{ Name }}',
 '{{ PrimaryAccountId }}',
 '{{ ComputationPreference }}',
 '{{ AccountGrouping }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.billingconductor.billing_groups (
 Name,
 Description,
 PrimaryAccountId,
 ComputationPreference,
 AccountGrouping,
 Tags,
 region
)
SELECT 
 '{{ Name }}',
 '{{ Description }}',
 '{{ PrimaryAccountId }}',
 '{{ ComputationPreference }}',
 '{{ AccountGrouping }}',
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
  - name: billing_group
    props:
      - name: Name
        value: '{{ Name }}'
      - name: Description
        value: '{{ Description }}'
      - name: PrimaryAccountId
        value: '{{ PrimaryAccountId }}'
      - name: ComputationPreference
        value:
          PricingPlanArn: '{{ PricingPlanArn }}'
      - name: AccountGrouping
        value:
          LinkedAccountIds:
            - '{{ LinkedAccountIds[0] }}'
          AutoAssociate: '{{ AutoAssociate }}'
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
DELETE FROM aws.billingconductor.billing_groups
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>billing_groups</code> resource, the following permissions are required:

### Create
```json
billingconductor:CreateBillingGroup,
billingconductor:AssociateAccounts,
billingconductor:ListBillingGroups,
billingconductor:TagResource,
billingconductor:ListTagsForResource
```

### Read
```json
billingconductor:ListBillingGroups,
billingconductor:ListAccountAssociations,
organizations:ListAccounts,
billingconductor:ListTagsForResource
```

### List
```json
billingconductor:ListBillingGroups,
billingconductor:ListAccountAssociations,
organizations:ListAccounts,
billingconductor:ListTagsForResource
```

### Update
```json
billingconductor:UpdateBillingGroup,
billingconductor:ListAccountAssociations,
organizations:ListAccounts,
billingconductor:AssociateAccounts,
billingconductor:DisassociateAccounts,
billingconductor:ListBillingGroups,
billingconductor:TagResource,
billingconductor:UntagResource
```

### Delete
```json
billingconductor:DeleteBillingGroup,
billingconductor:ListBillingGroups,
billingconductor:UntagResource,
billingconductor:UpdateBillingGroup
```
