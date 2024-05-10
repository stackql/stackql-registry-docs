---
title: annotation_stores
hide_title: false
hide_table_of_contents: false
keywords:
  - annotation_stores
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


Used to retrieve a list of <code>annotation_stores</code> in a region or to create or delete a <code>annotation_stores</code> resource, use <code>annotation_store</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>annotation_stores</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Omics::AnnotationStore Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.omics.annotation_stores" /></td></tr>
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
FROM aws.omics.annotation_stores
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>annotation_store</code> resource, using <a ref="https://pypi.org/project/stack-deploy/" target="_blank"><code><b>stack-deploy</b></code></a>.

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
-- annotation_store.iql (required properties only)
INSERT INTO aws.omics.annotation_stores (
 Name,
 StoreFormat,
 region
)
SELECT 
'{{ Name }}',
 '{{ StoreFormat }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- annotation_store.iql (all properties)
INSERT INTO aws.omics.annotation_stores (
 Description,
 Name,
 Reference,
 SseConfig,
 StoreFormat,
 StoreOptions,
 Tags,
 region
)
SELECT 
 '{{ Description }}',
 '{{ Name }}',
 '{{ Reference }}',
 '{{ SseConfig }}',
 '{{ StoreFormat }}',
 '{{ StoreOptions }}',
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
  - name: annotation_store
    props:
      - name: Description
        value: '{{ Description }}'
      - name: Name
        value: '{{ Name }}'
      - name: Reference
        value:
          ReferenceArn: '{{ ReferenceArn }}'
      - name: SseConfig
        value:
          Type: '{{ Type }}'
          KeyArn: '{{ KeyArn }}'
      - name: StoreFormat
        value: '{{ StoreFormat }}'
      - name: StoreOptions
        value: null
      - name: Tags
        value: {}

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.omics.annotation_stores
WHERE data__Identifier = '<Name>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>annotation_stores</code> resource, the following permissions are required:

### Create
```json
omics:CreateAnnotationStore,
omics:TagResource,
kms:DescribeKey,
kms:GenerateDataKey,
kms:CreateGrant,
ram:AcceptResourceShareInvitation,
ram:GetResourceShareInvitations,
omics:GetAnnotationStore
```

### Delete
```json
omics:DeleteAnnotationStore,
omics:ListAnnotationStores
```

### List
```json
omics:ListAnnotationStores
```

