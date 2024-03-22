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
Gets an individual <code>prefix_list</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>prefix_list</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>prefix_list</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.ec2.prefix_list</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>prefix_list_name</code></td><td><code>string</code></td><td>Name of Prefix List.</td></tr>
<tr><td><code>prefix_list_id</code></td><td><code>string</code></td><td>Id of Prefix List.</td></tr>
<tr><td><code>owner_id</code></td><td><code>string</code></td><td>Owner Id of Prefix List.</td></tr>
<tr><td><code>address_family</code></td><td><code>string</code></td><td>Ip Version of Prefix List.</td></tr>
<tr><td><code>max_entries</code></td><td><code>integer</code></td><td>Max Entries of Prefix List.</td></tr>
<tr><td><code>version</code></td><td><code>integer</code></td><td>Version of Prefix List.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>Tags for Prefix List</td></tr>
<tr><td><code>entries</code></td><td><code>array</code></td><td>Entries of Prefix List.</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the Prefix List.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
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
FROM awscc.ec2.prefix_list
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

