---
title: registries
hide_title: false
hide_table_of_contents: false
keywords:
  - registries
  - eventschemas
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


Used to retrieve a list of <code>registries</code> in a region or to create or delete a <code>registries</code> resource, use <code>registry</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>registries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EventSchemas::Registry</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.eventschemas.registries" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="registry_arn" /></td><td><code>string</code></td><td>The ARN of the registry.</td></tr>
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
registry_arn
FROM aws.eventschemas.registries
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
 "RegistryName": "{{ RegistryName }}",
 "Description": "{{ Description }}",
 "Tags": [
  {
   "Value": "{{ Value }}",
   "Key": "{{ Key }}"
  }
 ]
}
>>>
--required properties only
INSERT INTO aws.eventschemas.registries (
 RegistryName,
 Description,
 Tags,
 region
)
SELECT 
{{ RegistryName }},
 {{ Description }},
 {{ Tags }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "RegistryName": "{{ RegistryName }}",
 "Description": "{{ Description }}",
 "Tags": [
  {
   "Value": "{{ Value }}",
   "Key": "{{ Key }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.eventschemas.registries (
 RegistryName,
 Description,
 Tags,
 region
)
SELECT 
 {{ RegistryName }},
 {{ Description }},
 {{ Tags }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.eventschemas.registries
WHERE data__Identifier = '<RegistryArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>registries</code> resource, the following permissions are required:

### Create
```json
schemas:DescribeRegistry,
schemas:CreateRegistry,
schemas:TagResource
```

### Delete
```json
schemas:DescribeRegistry,
schemas:DeleteRegistry
```

### List
```json
schemas:ListRegistries
```

