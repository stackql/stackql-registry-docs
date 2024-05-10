---
title: resource_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_sets
  - fms
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


Used to retrieve a list of <code>resource_sets</code> in a region or to create or delete a <code>resource_sets</code> resource, use <code>resource_set</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resource_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Creates an AWS Firewall Manager resource set.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.fms.resource_sets" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="id" /></td><td><code>undefined</code></td><td></td></tr>
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
id
FROM aws.fms.resource_sets
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
 "Name": "{{ Name }}",
 "ResourceTypeList": [
  "{{ ResourceTypeList[0] }}"
 ]
}
>>>
--required properties only
INSERT INTO aws.fms.resource_sets (
 Name,
 ResourceTypeList,
 region
)
SELECT 
{{ Name }},
 {{ ResourceTypeList }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Name": "{{ Name }}",
 "Description": "{{ Description }}",
 "ResourceTypeList": [
  "{{ ResourceTypeList[0] }}"
 ],
 "Resources": [
  "{{ Resources[0] }}"
 ],
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.fms.resource_sets (
 Name,
 Description,
 ResourceTypeList,
 Resources,
 Tags,
 region
)
SELECT 
 {{ Name }},
 {{ Description }},
 {{ ResourceTypeList }},
 {{ Resources }},
 {{ Tags }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.fms.resource_sets
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>resource_sets</code> resource, the following permissions are required:

### Create
```json
fms:PutResourceSet,
fms:BatchAssociateResource,
fms:ListResourceSetResources,
fms:TagResource
```

### Delete
```json
fms:DeleteResourceSet
```

### List
```json
fms:ListResourceSets
```

