---
title: environment_account_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - environment_account_connections
  - proton
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


Used to retrieve a list of <code>environment_account_connections</code> in a region or to create or delete a <code>environment_account_connections</code> resource, use <code>environment_account_connection</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>environment_account_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Schema describing various properties for AWS Proton Environment Account Connections resources.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.proton.environment_account_connections" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the environment account connection.</td></tr>
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
FROM aws.proton.environment_account_connections
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
 "CodebuildRoleArn": "{{ CodebuildRoleArn }}",
 "ComponentRoleArn": "{{ ComponentRoleArn }}",
 "EnvironmentAccountId": "{{ EnvironmentAccountId }}",
 "EnvironmentName": "{{ EnvironmentName }}",
 "ManagementAccountId": "{{ ManagementAccountId }}",
 "RoleArn": "{{ RoleArn }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--required properties only
INSERT INTO aws.proton.environment_account_connections (
 CodebuildRoleArn,
 ComponentRoleArn,
 EnvironmentAccountId,
 EnvironmentName,
 ManagementAccountId,
 RoleArn,
 Tags,
 region
)
SELECT 
{{ .CodebuildRoleArn }},
 {{ .ComponentRoleArn }},
 {{ .EnvironmentAccountId }},
 {{ .EnvironmentName }},
 {{ .ManagementAccountId }},
 {{ .RoleArn }},
 {{ .Tags }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "CodebuildRoleArn": "{{ CodebuildRoleArn }}",
 "ComponentRoleArn": "{{ ComponentRoleArn }}",
 "EnvironmentAccountId": "{{ EnvironmentAccountId }}",
 "EnvironmentName": "{{ EnvironmentName }}",
 "ManagementAccountId": "{{ ManagementAccountId }}",
 "RoleArn": "{{ RoleArn }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.proton.environment_account_connections (
 CodebuildRoleArn,
 ComponentRoleArn,
 EnvironmentAccountId,
 EnvironmentName,
 ManagementAccountId,
 RoleArn,
 Tags,
 region
)
SELECT 
 {{ .CodebuildRoleArn }},
 {{ .ComponentRoleArn }},
 {{ .EnvironmentAccountId }},
 {{ .EnvironmentName }},
 {{ .ManagementAccountId }},
 {{ .RoleArn }},
 {{ .Tags }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.proton.environment_account_connections
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>environment_account_connections</code> resource, the following permissions are required:

### Create
```json
proton:CreateEnvironmentAccountConnection,
proton:TagResource,
iam:PassRole,
proton:ListTagsForResource,
proton:GetEnvironmentAccountConnection
```

### Delete
```json
proton:DeleteEnvironmentAccountConnection,
proton:UntagResource,
iam:PassRole,
proton:ListTagsForResource,
proton:GetEnvironmentAccountConnection
```

### List
```json
proton:ListEnvironmentAccountConnections
```

