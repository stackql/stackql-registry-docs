---
title: variant_stores
hide_title: false
hide_table_of_contents: false
keywords:
  - variant_stores
  - omics
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


Used to retrieve a list of <code>variant_stores</code> in a region or to create or delete a <code>variant_stores</code> resource, use <code>variant_store</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>variant_stores</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Omics::VariantStore Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.omics.variant_stores" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
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
name
FROM aws.omics.variant_stores
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
 "Name": "{{ Name }}",
 "Reference": {
  "ReferenceArn": "{{ ReferenceArn }}"
 }
}
>>>
--required properties only
INSERT INTO aws.omics.variant_stores (
 Name,
 Reference,
 region
)
SELECT 
{{ Name }},
 {{ Reference }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Description": "{{ Description }}",
 "Name": "{{ Name }}",
 "Reference": {
  "ReferenceArn": "{{ ReferenceArn }}"
 },
 "SseConfig": {
  "Type": "{{ Type }}",
  "KeyArn": "{{ KeyArn }}"
 },
 "Tags": {}
}
>>>
--all properties
INSERT INTO aws.omics.variant_stores (
 Description,
 Name,
 Reference,
 SseConfig,
 Tags,
 region
)
SELECT 
 {{ Description }},
 {{ Name }},
 {{ Reference }},
 {{ SseConfig }},
 {{ Tags }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.omics.variant_stores
WHERE data__Identifier = '<Name>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>variant_stores</code> resource, the following permissions are required:

### Create
```json
omics:CreateVariantStore,
omics:TagResource,
kms:DescribeKey,
kms:GenerateDataKey,
kms:CreateGrant,
ram:AcceptResourceShareInvitation,
ram:GetResourceShareInvitations,
omics:GetVariantStore
```

### Delete
```json
omics:DeleteVariantStore,
omics:ListVariantStores
```

### List
```json
omics:ListVariantStores
```

