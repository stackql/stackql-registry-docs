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
Retrieves a list of <code>prefix_lists</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>prefix_lists</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>prefix_lists</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.ec2.prefix_lists</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>prefix_list_id</code></td><td><code>string</code></td><td>Id of Prefix List.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
prefix_list_id
FROM awscc.ec2.prefix_lists
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>prefix_lists</code> resource, the following permissions are required:

### Create
```json
EC2:CreateManagedPrefixList,
EC2:DescribeManagedPrefixLists,
EC2:CreateTags
```

### List
```json
EC2:DescribeManagedPrefixLists,
EC2:GetManagedPrefixListEntries
```

