---
title: indices
hide_title: false
hide_table_of_contents: false
keywords:
  - indices
  - qbusiness
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

Creates, updates, deletes or gets an <code>index</code> resource or lists <code>indices</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>indices</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::QBusiness::Index Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.qbusiness.indices" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="application_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="capacity_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="display_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="document_attribute_configurations" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="index_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="index_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="index_statistics" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="updated_at" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="ApplicationId, DisplayName, region" /></td>
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
List all <code>indices</code> in a region.
```sql
SELECT
region,
application_id,
index_id
FROM aws.qbusiness.indices
WHERE region = 'us-east-1';
```
Gets all properties from an <code>index</code>.
```sql
SELECT
region,
application_id,
capacity_configuration,
created_at,
description,
display_name,
document_attribute_configurations,
index_arn,
index_id,
index_statistics,
type,
status,
tags,
updated_at
FROM aws.qbusiness.indices
WHERE region = 'us-east-1' AND data__Identifier = '<ApplicationId>|<IndexId>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>index</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.qbusiness.indices (
 ApplicationId,
 DisplayName,
 region
)
SELECT 
'{{ ApplicationId }}',
 '{{ DisplayName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.qbusiness.indices (
 ApplicationId,
 CapacityConfiguration,
 Description,
 DisplayName,
 DocumentAttributeConfigurations,
 Type,
 Tags,
 region
)
SELECT 
 '{{ ApplicationId }}',
 '{{ CapacityConfiguration }}',
 '{{ Description }}',
 '{{ DisplayName }}',
 '{{ DocumentAttributeConfigurations }}',
 '{{ Type }}',
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
  - name: index
    props:
      - name: ApplicationId
        value: '{{ ApplicationId }}'
      - name: CapacityConfiguration
        value:
          Units: null
      - name: Description
        value: '{{ Description }}'
      - name: DisplayName
        value: '{{ DisplayName }}'
      - name: DocumentAttributeConfigurations
        value:
          - Name: '{{ Name }}'
            Type: '{{ Type }}'
            Search: '{{ Search }}'
      - name: Type
        value: '{{ Type }}'
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
DELETE FROM aws.qbusiness.indices
WHERE data__Identifier = '<ApplicationId|IndexId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>indices</code> resource, the following permissions are required:

### Create
```json
qbusiness:CreateIndex,
qbusiness:GetIndex,
qbusiness:ListTagsForResource,
qbusiness:TagResource,
qbusiness:UpdateIndex
```

### Read
```json
qbusiness:GetIndex,
qbusiness:ListTagsForResource
```

### Update
```json
qbusiness:GetIndex,
qbusiness:ListTagsForResource,
qbusiness:TagResource,
qbusiness:UntagResource,
qbusiness:UpdateIndex
```

### Delete
```json
qbusiness:DeleteIndex,
qbusiness:GetIndex
```

### List
```json
qbusiness:ListIndices
```

