---
title: aliases
hide_title: false
hide_table_of_contents: false
keywords:
  - aliases
  - gamelift
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


Used to retrieve a list of <code>aliases</code> in a region or to create or delete a <code>aliases</code> resource, use <code>alias</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>aliases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::GameLift::Alias resource creates an alias for an Amazon GameLift (GameLift) fleet destination.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.gamelift.aliases" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="alias_id" /></td><td><code>string</code></td><td>Unique alias ID</td></tr>
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
alias_id
FROM aws.gamelift.aliases
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
 "RoutingStrategy": {
  "Message": "{{ Message }}",
  "FleetId": "{{ FleetId }}",
  "Type": "{{ Type }}"
 }
}
>>>
--required properties only
INSERT INTO aws.gamelift.aliases (
 Name,
 RoutingStrategy,
 region
)
SELECT 
{{ .Name }},
 {{ .RoutingStrategy }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Description": "{{ Description }}",
 "Name": "{{ Name }}",
 "RoutingStrategy": {
  "Message": "{{ Message }}",
  "FleetId": "{{ FleetId }}",
  "Type": "{{ Type }}"
 }
}
>>>
--all properties
INSERT INTO aws.gamelift.aliases (
 Description,
 Name,
 RoutingStrategy,
 region
)
SELECT 
 {{ .Description }},
 {{ .Name }},
 {{ .RoutingStrategy }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.gamelift.aliases
WHERE data__Identifier = '<AliasId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>aliases</code> resource, the following permissions are required:

### Create
```json
gamelift:CreateAlias
```

### Delete
```json
gamelift:DeleteAlias
```

### List
```json
gamelift:ListAliases
```

