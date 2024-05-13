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


Used to retrieve a list of <code>billing_groups</code> in a region or to create or delete a <code>billing_groups</code> resource, use <code>billing_group</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>billing_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A billing group is a set of linked account which belong to the same end customer. It can be seen as a virtual consolidated billing family.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.billingconductor.billing_groups" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Billing Group ARN</td></tr>
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
    <td><CopyableCode code="Name, AccountGrouping, PrimaryAccountId, ComputationPreference, region" /></td>
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
arn
FROM aws.billingconductor.billing_groups
WHERE region = 'us-east-1';
```

## `INSERT` Example

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

## `DELETE` Example

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

### List
```json
billingconductor:ListBillingGroups,
billingconductor:ListAccountAssociations,
organizations:ListAccounts,
billingconductor:ListTagsForResource
```

### Delete
```json
billingconductor:DeleteBillingGroup,
billingconductor:ListBillingGroups,
billingconductor:UntagResource,
billingconductor:UpdateBillingGroup
```

