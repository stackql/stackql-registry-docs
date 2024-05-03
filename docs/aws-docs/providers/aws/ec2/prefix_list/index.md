---
title: prefix_list
hide_title: false
hide_table_of_contents: false
keywords:
  - prefix_list
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

Gets or operates on an individual <code>prefix_list</code> resource, use <code>prefix_lists</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>prefix_list</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema of AWS::EC2::PrefixList Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.prefix_list" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="prefix_list_name" /></td><td><code>string</code></td><td>Name of Prefix List.</td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
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
FROM aws.ec2.prefix_list
WHERE data__Identifier = '<PrefixListId>';
```

## Permissions

To operate on the <code>prefix_list</code> resource, the following permissions are required:

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

