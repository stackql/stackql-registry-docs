---
title: storage_lens_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - storage_lens_groups
  - s3
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

Creates, updates, deletes or gets a <code>storage_lens_group</code> resource or lists <code>storage_lens_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>storage_lens_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::S3::StorageLensGroup resource is an Amazon S3 resource type that you can use to create Storage Lens Group.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.s3.storage_lens_groups" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>The name that identifies the Amazon S3 Storage Lens Group.</code></td><td></td></tr>
<tr><td><CopyableCode code="filter" /></td><td><code>Sets the Storage Lens Group filter.</code></td><td></td></tr>
<tr><td><CopyableCode code="storage_lens_group_arn" /></td><td><code>string</code></td><td>The ARN for the Amazon S3 Storage Lens Group.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A set of tags (key-value pairs) for this Amazon S3 Storage Lens Group.</td></tr>
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
    <td><CopyableCode code="Name, Filter, region" /></td>
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
List all <code>storage_lens_groups</code> in a region.
```sql
SELECT
region,
name
FROM aws.s3.storage_lens_groups
WHERE region = 'us-east-1';
```
Gets all properties from a <code>storage_lens_group</code>.
```sql
SELECT
region,
name,
filter,
storage_lens_group_arn,
tags
FROM aws.s3.storage_lens_groups
WHERE region = 'us-east-1' AND data__Identifier = '<Name>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>storage_lens_group</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.s3.storage_lens_groups (
 Name,
 Filter,
 region
)
SELECT 
'{{ Name }}',
 '{{ Filter }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.s3.storage_lens_groups (
 Name,
 Filter,
 Tags,
 region
)
SELECT 
 '{{ Name }}',
 '{{ Filter }}',
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
  - name: storage_lens_group
    props:
      - name: Name
        value: '{{ Name }}'
      - name: Filter
        value:
          MatchAnyPrefix:
            - '{{ MatchAnyPrefix[0] }}'
          MatchAnySuffix:
            - '{{ MatchAnySuffix[0] }}'
          MatchAnyTag:
            - Key: '{{ Key }}'
              Value: '{{ Value }}'
          MatchObjectSize:
            BytesGreaterThan: '{{ BytesGreaterThan }}'
            BytesLessThan: '{{ BytesLessThan }}'
          MatchObjectAge:
            DaysGreaterThan: '{{ DaysGreaterThan }}'
            DaysLessThan: '{{ DaysLessThan }}'
          And:
            MatchAnyPrefix: null
            MatchAnySuffix: null
            MatchAnyTag: null
            MatchObjectSize: null
            MatchObjectAge: null
          Or:
            MatchAnyPrefix: null
            MatchAnySuffix: null
            MatchAnyTag: null
            MatchObjectSize: null
            MatchObjectAge: null
      - name: Tags
        value:
          - null

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.s3.storage_lens_groups
WHERE data__Identifier = '<Name>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>storage_lens_groups</code> resource, the following permissions are required:

### Create
```json
s3:CreateStorageLensGroup,
s3:GetStorageLensGroup,
s3:TagResource,
s3:ListTagsForResource
```

### Read
```json
s3:GetStorageLensGroup,
s3:ListTagsForResource
```

### Update
```json
s3:GetStorageLensGroup,
s3:UpdateStorageLensGroup,
s3:TagResource,
s3:UntagResource,
s3:ListTagsForResource
```

### Delete
```json
s3:DeleteStorageLensGroup
```

### List
```json
s3:ListStorageLensGroups
```

