---
title: dataset_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - dataset_groups
  - forecast
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


Used to retrieve a list of <code>dataset_groups</code> in a region or to create or delete a <code>dataset_groups</code> resource, use <code>dataset_group</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dataset_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Represents a dataset group that holds a collection of related datasets</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.forecast.dataset_groups" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="dataset_group_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the dataset group to delete.</td></tr>
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
dataset_group_arn
FROM aws.forecast.dataset_groups
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
 "DatasetGroupName": "{{ DatasetGroupName }}",
 "Domain": "{{ Domain }}"
}
>>>
--required properties only
INSERT INTO aws.forecast.dataset_groups (
 DatasetGroupName,
 Domain,
 region
)
SELECT 
{{ DatasetGroupName }},
 {{ Domain }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "DatasetArns": [
  "{{ DatasetArns[0] }}"
 ],
 "DatasetGroupName": "{{ DatasetGroupName }}",
 "Domain": "{{ Domain }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.forecast.dataset_groups (
 DatasetArns,
 DatasetGroupName,
 Domain,
 Tags,
 region
)
SELECT 
 {{ DatasetArns }},
 {{ DatasetGroupName }},
 {{ Domain }},
 {{ Tags }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.forecast.dataset_groups
WHERE data__Identifier = '<DatasetGroupArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>dataset_groups</code> resource, the following permissions are required:

### Create
```json
forecast:CreateDatasetGroup
```

### Delete
```json
forecast:DeleteDatasetGroup
```

### List
```json
forecast:ListDatasetGroups
```

