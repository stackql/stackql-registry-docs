---
title: connection_aliases
hide_title: false
hide_table_of_contents: false
keywords:
  - connection_aliases
  - workspaces
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


Used to retrieve a list of <code>connection_aliases</code> in a region or to create or delete a <code>connection_aliases</code> resource, use <code>connection_alias</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connection_aliases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::WorkSpaces::ConnectionAlias</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.workspaces.connection_aliases" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="alias_id" /></td><td><code>string</code></td><td></td></tr>
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
FROM aws.workspaces.connection_aliases
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
 "ConnectionString": "{{ ConnectionString }}"
}
>>>
--required properties only
INSERT INTO aws.workspaces.connection_aliases (
 ConnectionString,
 region
)
SELECT 
{{ .ConnectionString }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "ConnectionString": "{{ ConnectionString }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.workspaces.connection_aliases (
 ConnectionString,
 Tags,
 region
)
SELECT 
 {{ .ConnectionString }},
 {{ .Tags }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.workspaces.connection_aliases
WHERE data__Identifier = '<AliasId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>connection_aliases</code> resource, the following permissions are required:

### Create
```json
workspaces:CreateConnectionAlias
```

### Delete
```json
workspaces:DeleteConnectionAlias
```

