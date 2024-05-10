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


Used to retrieve a list of <code>storage_lens_groups</code> in a region or to create or delete a <code>storage_lens_groups</code> resource, use <code>storage_lens_group</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>storage_lens_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::S3::StorageLensGroup resource is an Amazon S3 resource type that you can use to create Storage Lens Group.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.s3.storage_lens_groups" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="name" /></td><td><code>undefined</code></td><td></td></tr>
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
FROM aws.s3.storage_lens_groups
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>storage_lens_group</code> resource, using <a ref="https://pypi.org/project/stack-deploy/" target="_blank"><code><b>stack-deploy</b></code></a>.

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
-- storage_lens_group.iql (required properties only)
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
-- storage_lens_group.iql (all properties)
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

## `DELETE` Example

```sql
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

### Delete
```json
s3:DeleteStorageLensGroup
```

### List
```json
s3:ListStorageLensGroups
```

