---
title: faqs
hide_title: false
hide_table_of_contents: false
keywords:
  - faqs
  - kendra
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

Creates, updates, deletes or gets a <code>faq</code> resource or lists <code>faqs</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>faqs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A Kendra FAQ resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.kendra.faqs" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>Unique ID of index</td></tr>
<tr><td><CopyableCode code="index_id" /></td><td><code>string</code></td><td>Index ID</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>FAQ name</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>FAQ description</td></tr>
<tr><td><CopyableCode code="file_format" /></td><td><code>string</code></td><td>FAQ file format</td></tr>
<tr><td><CopyableCode code="s3_path" /></td><td><code>object</code></td><td>FAQ S3 path</td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td>FAQ role ARN</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>Tags for labeling the FAQ</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="language_code" /></td><td><code>string</code></td><td>The code for a language.</td></tr>
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
    <td><CopyableCode code="IndexId, Name, S3Path, RoleArn, region" /></td>
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
Gets all <code>faqs</code> in a region.
```sql
SELECT
region,
id,
index_id,
name,
description,
file_format,
s3_path,
role_arn,
tags,
arn,
language_code
FROM aws.kendra.faqs
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>faq</code>.
```sql
SELECT
region,
id,
index_id,
name,
description,
file_format,
s3_path,
role_arn,
tags,
arn,
language_code
FROM aws.kendra.faqs
WHERE region = 'us-east-1' AND data__Identifier = '<Id>|<IndexId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>faq</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.kendra.faqs (
 IndexId,
 Name,
 S3Path,
 RoleArn,
 region
)
SELECT 
'{{ IndexId }}',
 '{{ Name }}',
 '{{ S3Path }}',
 '{{ RoleArn }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.kendra.faqs (
 IndexId,
 Name,
 Description,
 FileFormat,
 S3Path,
 RoleArn,
 Tags,
 LanguageCode,
 region
)
SELECT 
 '{{ IndexId }}',
 '{{ Name }}',
 '{{ Description }}',
 '{{ FileFormat }}',
 '{{ S3Path }}',
 '{{ RoleArn }}',
 '{{ Tags }}',
 '{{ LanguageCode }}',
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
  - name: faq
    props:
      - name: IndexId
        value: '{{ IndexId }}'
      - name: Name
        value: '{{ Name }}'
      - name: Description
        value: '{{ Description }}'
      - name: FileFormat
        value: '{{ FileFormat }}'
      - name: S3Path
        value:
          Bucket: '{{ Bucket }}'
          Key: '{{ Key }}'
      - name: RoleArn
        value: '{{ RoleArn }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: LanguageCode
        value: '{{ LanguageCode }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.kendra.faqs
WHERE data__Identifier = '<Id|IndexId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>faqs</code> resource, the following permissions are required:

### Create
```json
kendra:CreateFaq,
kendra:DescribeFaq,
iam:PassRole,
kendra:ListTagsForResource,
kendra:TagResource
```

### Update
```json
kendra:ListTagsForResource,
kendra:UntagResource,
kendra:TagResource
```

### Read
```json
kendra:DescribeFaq,
kendra:ListTagsForResource
```

### Delete
```json
kendra:DeleteFaq,
kendra:DescribeFaq
```

### List
```json
kendra:ListFaqs
```

