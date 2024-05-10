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


Used to retrieve a list of <code>prefix_lists</code> in a region or to create or delete a <code>prefix_lists</code> resource, use <code>prefix_list</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>prefix_lists</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema of AWS::EC2::PrefixList Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.prefix_lists" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="prefix_list_id" /></td><td><code>string</code></td><td>Id of Prefix List.</td></tr>
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
prefix_list_id
FROM aws.ec2.prefix_lists
WHERE region = 'us-east-1';
```

## `INSERT` Example

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
    ]
}>
<TabItem value="required">

```sql
<<<json
{
 "PrefixListName": "{{ PrefixListName }}",
 "AddressFamily": "{{ AddressFamily }}"
}
>>>
--required properties only
INSERT INTO aws.ec2.prefix_lists (
 PrefixListName,
 AddressFamily,
 region
)
SELECT 
{{ .PrefixListName }},
 {{ .AddressFamily }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "PrefixListName": "{{ PrefixListName }}",
 "AddressFamily": "{{ AddressFamily }}",
 "MaxEntries": "{{ MaxEntries }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ],
 "Entries": [
  {
   "Cidr": "{{ Cidr }}",
   "Description": "{{ Description }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.ec2.prefix_lists (
 PrefixListName,
 AddressFamily,
 MaxEntries,
 Tags,
 Entries,
 region
)
SELECT 
 {{ .PrefixListName }},
 {{ .AddressFamily }},
 {{ .MaxEntries }},
 {{ .Tags }},
 {{ .Entries }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
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

