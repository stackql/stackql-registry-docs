---
title: reference_stores
hide_title: false
hide_table_of_contents: false
keywords:
  - reference_stores
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

Creates, updates, deletes or gets a <code>reference_store</code> resource or lists <code>reference_stores</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>reference_stores</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Omics::ReferenceStore Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.omics.reference_stores" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The store's ARN.</td></tr>
<tr><td><CopyableCode code="creation_time" /></td><td><code>string</code></td><td>When the store was created.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A description for the store.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>A name for the store.</td></tr>
<tr><td><CopyableCode code="reference_store_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="sse_config" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>A map of resource tags</code></td><td></td></tr>
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
    <td><CopyableCode code="Name, region" /></td>
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
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
List all <code>reference_stores</code> in a region.
```sql
SELECT
region,
reference_store_id
FROM aws.omics.reference_stores
WHERE region = 'us-east-1';
```
Gets all properties from a <code>reference_store</code>.
```sql
SELECT
region,
arn,
creation_time,
description,
name,
reference_store_id,
sse_config,
tags
FROM aws.omics.reference_stores
WHERE region = 'us-east-1' AND data__Identifier = '<ReferenceStoreId>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>reference_store</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.omics.reference_stores (
 Name,
 region
)
SELECT 
'{{ Name }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.omics.reference_stores (
 Description,
 Name,
 SseConfig,
 Tags,
 region
)
SELECT 
 '{{ Description }}',
 '{{ Name }}',
 '{{ SseConfig }}',
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
  - name: reference_store
    props:
      - name: Description
        value: '{{ Description }}'
      - name: Name
        value: '{{ Name }}'
      - name: SseConfig
        value:
          Type: '{{ Type }}'
          KeyArn: '{{ KeyArn }}'
      - name: Tags
        value: {}

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.omics.reference_stores
WHERE data__Identifier = '<ReferenceStoreId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>reference_stores</code> resource, the following permissions are required:

### Create
```json
omics:CreateReferenceStore,
omics:TagResource
```

### Read
```json
omics:GetReferenceStore,
omics:ListTagsForResource
```

### Delete
```json
omics:DeleteReferenceStore
```

### List
```json
omics:ListReferenceStores
```

