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

Creates, updates, deletes or gets an <code>environment_account_connection</code> resource or lists <code>environment_account_connections</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>environment_account_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Schema describing various properties for AWS Proton Environment Account Connections resources.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.proton.environment_account_connections" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the environment account connection.</td></tr>
<tr><td><CopyableCode code="codebuild_role_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of an IAM service role in the environment account. AWS Proton uses this role to provision infrastructure resources using CodeBuild-based provisioning in the associated environment account.</td></tr>
<tr><td><CopyableCode code="component_role_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the IAM service role that AWS Proton uses when provisioning directly defined components in the associated environment account. It determines the scope of infrastructure that a component can provision in the account.</td></tr>
<tr><td><CopyableCode code="environment_account_id" /></td><td><code>string</code></td><td>The environment account that's connected to the environment account connection.</td></tr>
<tr><td><CopyableCode code="environment_name" /></td><td><code>string</code></td><td>The name of the AWS Proton environment that's created in the associated management account.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The ID of the environment account connection.</td></tr>
<tr><td><CopyableCode code="management_account_id" /></td><td><code>string</code></td><td>The ID of the management account that accepts or rejects the environment account connection. You create an manage the AWS Proton environment in this account. If the management account accepts the environment account connection, AWS Proton can use the associated IAM role to provision environment infrastructure resources in the associated environment account.</td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the IAM service role that's created in the environment account. AWS Proton uses this role to provision infrastructure resources in the associated environment account.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>The status of the environment account connection.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td><p>An optional list of metadata items that you can associate with the Proton environment account connection. A tag is a key-value pair.</p><br /><p>For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/resources.html">Proton resources and tagging</a> in the<br /><i>Proton User Guide</i>.</p></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-proton-environmentaccountconnection.html"><code>AWS::Proton::EnvironmentAccountConnection</code></a>.

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
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Gets all <code>environment_account_connections</code> in a region.
```sql
SELECT
region,
arn,
codebuild_role_arn,
component_role_arn,
environment_account_id,
environment_name,
id,
management_account_id,
role_arn,
status,
tags
FROM aws.proton.environment_account_connections
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>environment_account_connection</code>.
```sql
SELECT
region,
arn,
codebuild_role_arn,
component_role_arn,
environment_account_id,
environment_name,
id,
management_account_id,
role_arn,
status,
tags
FROM aws.proton.environment_account_connections
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>environment_account_connection</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
/*+ create */
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
/*+ create */
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

## `DELETE` example

```sql
/*+ delete */
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

### Read
```json
proton:GetEnvironmentAccountConnection,
proton:ListTagsForResource,
iam:PassRole,
proton:GetEnvironmentAccountConnection
```

### Update
```json
proton:CreateEnvironmentAccountConnection,
proton:ListTagsForResource,
proton:TagResource,
proton:UntagResource,
proton:UpdateEnvironmentAccountConnection,
iam:PassRole,
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
