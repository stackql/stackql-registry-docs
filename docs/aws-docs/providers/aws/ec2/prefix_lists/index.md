---
title: prefix_lists
hide_title: false
hide_table_of_contents: false
keywords:
  - prefix_lists
  - ec2
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

Creates, updates, deletes or gets a <code>prefix_list</code> resource or lists <code>prefix_lists</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>prefix_lists</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema of AWS::EC2::PrefixList Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.prefix_lists" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="prefix_list_name" /></td><td><code>string</code></td><td>Name of Prefix List.</td></tr>
<tr><td><CopyableCode code="prefix_list_id" /></td><td><code>string</code></td><td>Id of Prefix List.</td></tr>
<tr><td><CopyableCode code="owner_id" /></td><td><code>string</code></td><td>Owner Id of Prefix List.</td></tr>
<tr><td><CopyableCode code="address_family" /></td><td><code>string</code></td><td>Ip Version of Prefix List.</td></tr>
<tr><td><CopyableCode code="max_entries" /></td><td><code>integer</code></td><td>Max Entries of Prefix List.</td></tr>
<tr><td><CopyableCode code="version" /></td><td><code>integer</code></td><td>Version of Prefix List.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>Tags for Prefix List</td></tr>
<tr><td><CopyableCode code="entries" /></td><td><code>array</code></td><td>Entries of Prefix List.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the Prefix List.</td></tr>
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
    <td><CopyableCode code="PrefixListName, AddressFamily, region" /></td>
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
List all <code>prefix_lists</code> in a region.
```sql
SELECT
region,
prefix_list_id
FROM aws.ec2.prefix_lists
WHERE region = 'us-east-1';
```
Gets all properties from a <code>prefix_list</code>.
```sql
SELECT
region,
prefix_list_name,
prefix_list_id,
owner_id,
address_family,
max_entries,
version,
tags,
entries,
arn
FROM aws.ec2.prefix_lists
WHERE region = 'us-east-1' AND data__Identifier = '<PrefixListId>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>prefix_list</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.ec2.prefix_lists (
 PrefixListName,
 AddressFamily,
 region
)
SELECT 
'{{ PrefixListName }}',
 '{{ AddressFamily }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.ec2.prefix_lists (
 PrefixListName,
 AddressFamily,
 MaxEntries,
 Tags,
 Entries,
 region
)
SELECT 
 '{{ PrefixListName }}',
 '{{ AddressFamily }}',
 '{{ MaxEntries }}',
 '{{ Tags }}',
 '{{ Entries }}',
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
  - name: prefix_list
    props:
      - name: PrefixListName
        value: '{{ PrefixListName }}'
      - name: AddressFamily
        value: '{{ AddressFamily }}'
      - name: MaxEntries
        value: '{{ MaxEntries }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: Entries
        value:
          - Cidr: '{{ Cidr }}'
            Description: '{{ Description }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.ec2.prefix_lists
WHERE data__Identifier = '<PrefixListId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>prefix_lists</code> resource, the following permissions are required:

### Create
```json
EC2:CreateManagedPrefixList,
EC2:DescribeManagedPrefixLists,
EC2:CreateTags
```

### Read
```json
EC2:GetManagedPrefixListEntries,
EC2:DescribeManagedPrefixLists
```

### Update
```json
EC2:DescribeManagedPrefixLists,
EC2:GetManagedPrefixListEntries,
EC2:ModifyManagedPrefixList,
EC2:CreateTags,
EC2:DeleteTags
```

### Delete
```json
EC2:DeleteManagedPrefixList,
EC2:DescribeManagedPrefixLists
```

### List
```json
EC2:DescribeManagedPrefixLists,
EC2:GetManagedPrefixListEntries
```

