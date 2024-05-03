---
title: billing_group
hide_title: false
hide_table_of_contents: false
keywords:
  - billing_group
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

Gets or operates on an individual <code>billing_group</code> resource, use <code>billing_groups</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>billing_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A billing group is a set of linked account which belong to the same end customer. It can be seen as a virtual consolidated billing family.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.billingconductor.billing_group" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Billing Group ARN</td></tr>
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

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
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
FROM aws.billingconductor.billing_group
WHERE data__Identifier = '<Arn>';
```

## Permissions

To operate on the <code>billing_group</code> resource, the following permissions are required:

### Read
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

