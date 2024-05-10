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

Use the following StackQL query and manifest file to create a new <code>environment_account_connection</code> resource, using <a ref="https://pypi.org/project/stack-deploy/" target="_blank"><code><b>stack-deploy</b></code></a>.

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
-- environment_account_connection.iql (required properties only)
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
'{{ CodebuildRoleArn }}',
 '{{ ComponentRoleArn }}',
 '{{ EnvironmentAccountId }}',
 '{{ EnvironmentName }}',
 '{{ ManagementAccountId }}',
 '{{ RoleArn }}',
 '{{ Tags }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- environment_account_connection.iql (all properties)
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
 '{{ CodebuildRoleArn }}',
 '{{ ComponentRoleArn }}',
 '{{ EnvironmentAccountId }}',
 '{{ EnvironmentName }}',
 '{{ ManagementAccountId }}',
 '{{ RoleArn }}',
 '{{ Tags }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: environment_account_connection
    props:
      - name: CodebuildRoleArn
        value: '{{ CodebuildRoleArn }}'
      - name: ComponentRoleArn
        value: '{{ ComponentRoleArn }}'
      - name: EnvironmentAccountId
        value: '{{ EnvironmentAccountId }}'
      - name: EnvironmentName
        value: '{{ EnvironmentName }}'
      - name: ManagementAccountId
        value: '{{ ManagementAccountId }}'
      - name: RoleArn
        value: '{{ RoleArn }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

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

