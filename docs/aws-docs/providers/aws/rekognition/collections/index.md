---
title: collections
hide_title: false
hide_table_of_contents: false
keywords:
  - collections
  - rekognition
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

Creates, updates, deletes or gets a <code>collection</code> resource or lists <code>collections</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>collections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::Rekognition::Collection type creates an Amazon Rekognition Collection. A collection is a logical grouping of information about detected faces which can later be referenced for searches on the group</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.rekognition.collections" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The ARN of the stream processor</td></tr>
<tr><td><CopyableCode code="collection_id" /></td><td><code>string</code></td><td>The name of the collection</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
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
    <td><CopyableCode code="CollectionId, region" /></td>
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
List all <code>collections</code> in a region.
```sql
SELECT
region,
collection_id
FROM aws.rekognition.collections
WHERE region = 'us-east-1';
```
Gets all properties from a <code>collection</code>.
```sql
SELECT
region,
arn,
collection_id,
tags
FROM aws.rekognition.collections
WHERE region = 'us-east-1' AND data__Identifier = '<CollectionId>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>collection</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.rekognition.collections (
 CollectionId,
 region
)
SELECT 
'{{ CollectionId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.rekognition.collections (
 CollectionId,
 Tags,
 region
)
SELECT 
 '{{ CollectionId }}',
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
  - name: collection
    props:
      - name: CollectionId
        value: '{{ CollectionId }}'
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
DELETE FROM aws.rekognition.collections
WHERE data__Identifier = '<CollectionId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>collections</code> resource, the following permissions are required:

### Create
```json
rekognition:CreateCollection,
rekognition:DescribeCollection,
rekognition:ListTagsForResource,
rekognition:TagResource
```

### Read
```json
rekognition:DescribeCollection,
rekognition:ListTagsForResource
```

### Update
```json
rekognition:TagResource,
rekognition:UntagResource,
rekognition:DescribeCollection,
rekognition:ListTagsForResource
```

### Delete
```json
rekognition:DeleteCollection
```

### List
```json
rekognition:ListCollections
```

