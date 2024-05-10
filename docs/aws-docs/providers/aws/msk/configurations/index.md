---
title: configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - configurations
  - msk
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


Used to retrieve a list of <code>configurations</code> in a region or to create or delete a <code>configurations</code> resource, use <code>configuration</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::MSK::Configuration</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.msk.configurations" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
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
arn
FROM aws.msk.configurations
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
 "ServerProperties": "{{ ServerProperties }}"
}
>>>
--required properties only
INSERT INTO aws.msk.configurations (
 Name,
 ServerProperties,
 region
)
SELECT 
{{ .Name }},
 {{ .ServerProperties }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Name": "{{ Name }}",
 "Description": "{{ Description }}",
 "ServerProperties": "{{ ServerProperties }}",
 "KafkaVersionsList": [
  "{{ KafkaVersionsList[0] }}"
 ],
 "LatestRevision": {
  "CreationTime": "{{ CreationTime }}",
  "Description": "{{ Description }}",
  "Revision": "{{ Revision }}"
 }
}
>>>
--all properties
INSERT INTO aws.msk.configurations (
 Name,
 Description,
 ServerProperties,
 KafkaVersionsList,
 LatestRevision,
 region
)
SELECT 
 {{ .Name }},
 {{ .Description }},
 {{ .ServerProperties }},
 {{ .KafkaVersionsList }},
 {{ .LatestRevision }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.msk.configurations
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>configurations</code> resource, the following permissions are required:

### Create
```json
kafka:CreateConfiguration,
Kafka:DescribeConfiguration
```

### Delete
```json
kafka:DeleteConfiguration,
kafka:DescribeConfiguration
```

### List
```json
kafka:ListConfigurations
```

