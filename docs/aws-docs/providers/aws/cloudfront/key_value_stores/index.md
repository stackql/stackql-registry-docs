---
title: key_value_stores
hide_title: false
hide_table_of_contents: false
keywords:
  - key_value_stores
  - cloudfront
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

Creates, updates, deletes or gets a <code>key_value_store</code> resource or lists <code>key_value_stores</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>key_value_stores</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::CloudFront::KeyValueStore</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cloudfront.key_value_stores" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="comment" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="import_source" /></td><td><code>undefined</code></td><td></td></tr>
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
List all <code>key_value_stores</code> in a region.
```sql
SELECT
region,
name
FROM aws.cloudfront.key_value_stores
;
```
Gets all properties from a <code>key_value_store</code>.
```sql
SELECT
region,
arn,
id,
status,
name,
comment,
import_source
FROM aws.cloudfront.key_value_stores
WHERE data__Identifier = '<Name>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>key_value_store</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.cloudfront.key_value_stores (
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
INSERT INTO aws.cloudfront.key_value_stores (
 Name,
 Comment,
 ImportSource,
 region
)
SELECT 
 '{{ Name }}',
 '{{ Comment }}',
 '{{ ImportSource }}',
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
  - name: key_value_store
    props:
      - name: Name
        value: '{{ Name }}'
      - name: Comment
        value: '{{ Comment }}'
      - name: ImportSource
        value:
          SourceType: '{{ SourceType }}'
          SourceArn: '{{ SourceArn }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.cloudfront.key_value_stores
WHERE data__Identifier = '<Name>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>key_value_stores</code> resource, the following permissions are required:

### Create
```json
cloudfront:CreateKeyValueStore,
cloudfront:DescribeKeyValueStore,
s3:GetObject,
s3:HeadObject,
s3:GetBucketLocation
```

### Delete
```json
cloudfront:DeleteKeyValueStore,
cloudfront:DescribeKeyValueStore
```

### List
```json
cloudfront:ListKeyValueStores
```

### Read
```json
cloudfront:DescribeKeyValueStore
```

### Update
```json
cloudfront:UpdateKeyValueStore,
cloudfront:DescribeKeyValueStore
```

