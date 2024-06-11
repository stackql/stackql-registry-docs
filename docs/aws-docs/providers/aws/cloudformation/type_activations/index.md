---
title: type_activations
hide_title: false
hide_table_of_contents: false
keywords:
  - type_activations
  - cloudformation
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

Creates, updates, deletes or gets a <code>type_activation</code> resource or lists <code>type_activations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>type_activations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Enable a resource that has been published in the CloudFormation Registry.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cloudformation.type_activations" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the extension.</td></tr>
<tr><td><CopyableCode code="execution_role_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the IAM execution role to use to register the type. If your resource type calls AWS APIs in any of its handlers, you must create an IAM execution role that includes the necessary permissions to call those AWS APIs, and provision that execution role in your account. CloudFormation then assumes that execution role to provide your resource type with the appropriate credentials.</td></tr>
<tr><td><CopyableCode code="publisher_id" /></td><td><code>string</code></td><td>The publisher id assigned by CloudFormation for publishing in this region.</td></tr>
<tr><td><CopyableCode code="logging_config" /></td><td><code>object</code></td><td>Specifies logging configuration information for a type.</td></tr>
<tr><td><CopyableCode code="public_type_arn" /></td><td><code>string</code></td><td>The Amazon Resource Number (ARN) assigned to the public extension upon publication</td></tr>
<tr><td><CopyableCode code="auto_update" /></td><td><code>boolean</code></td><td>Whether to automatically update the extension in this account and region when a new minor version is published by the extension publisher. Major versions released by the publisher must be manually updated.</td></tr>
<tr><td><CopyableCode code="type_name_alias" /></td><td><code>string</code></td><td>An alias to assign to the public extension in this account and region. If you specify an alias for the extension, you must then use the alias to refer to the extension in your templates.</td></tr>
<tr><td><CopyableCode code="version_bump" /></td><td><code>string</code></td><td>Manually updates a previously-enabled type to a new major or minor version, if available. You can also use this parameter to update the value of AutoUpdateEnabled</td></tr>
<tr><td><CopyableCode code="major_version" /></td><td><code>string</code></td><td>The Major Version of the type you want to enable</td></tr>
<tr><td><CopyableCode code="type_name" /></td><td><code>string</code></td><td>The name of the type being registered.<br/><br/>We recommend that type names adhere to the following pattern: company_or_organization::service::type.</td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>The kind of extension</td></tr>
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
    <td><CopyableCode code="list_resource" /></td>
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
List all <code>type_activations</code> in a region.
```sql
SELECT
region,
arn
FROM aws.cloudformation.type_activations
WHERE region = 'us-east-1';
```
Gets all properties from a <code>type_activation</code>.
```sql
SELECT
region,
arn,
execution_role_arn,
publisher_id,
logging_config,
public_type_arn,
auto_update,
type_name_alias,
version_bump,
major_version,
type_name,
type
FROM aws.cloudformation.type_activations
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>type_activation</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.cloudformation.type_activations (
 ExecutionRoleArn,
 PublisherId,
 LoggingConfig,
 PublicTypeArn,
 AutoUpdate,
 TypeNameAlias,
 VersionBump,
 MajorVersion,
 TypeName,
 Type,
 region
)
SELECT 
'{{ ExecutionRoleArn }}',
 '{{ PublisherId }}',
 '{{ LoggingConfig }}',
 '{{ PublicTypeArn }}',
 '{{ AutoUpdate }}',
 '{{ TypeNameAlias }}',
 '{{ VersionBump }}',
 '{{ MajorVersion }}',
 '{{ TypeName }}',
 '{{ Type }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.cloudformation.type_activations (
 ExecutionRoleArn,
 PublisherId,
 LoggingConfig,
 PublicTypeArn,
 AutoUpdate,
 TypeNameAlias,
 VersionBump,
 MajorVersion,
 TypeName,
 Type,
 region
)
SELECT 
 '{{ ExecutionRoleArn }}',
 '{{ PublisherId }}',
 '{{ LoggingConfig }}',
 '{{ PublicTypeArn }}',
 '{{ AutoUpdate }}',
 '{{ TypeNameAlias }}',
 '{{ VersionBump }}',
 '{{ MajorVersion }}',
 '{{ TypeName }}',
 '{{ Type }}',
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
  - name: type_activation
    props:
      - name: ExecutionRoleArn
        value: '{{ ExecutionRoleArn }}'
      - name: PublisherId
        value: '{{ PublisherId }}'
      - name: LoggingConfig
        value:
          LogGroupName: '{{ LogGroupName }}'
          LogRoleArn: '{{ LogRoleArn }}'
      - name: PublicTypeArn
        value: '{{ PublicTypeArn }}'
      - name: AutoUpdate
        value: '{{ AutoUpdate }}'
      - name: TypeNameAlias
        value: '{{ TypeNameAlias }}'
      - name: VersionBump
        value: '{{ VersionBump }}'
      - name: MajorVersion
        value: '{{ MajorVersion }}'
      - name: TypeName
        value: '{{ TypeName }}'
      - name: Type
        value: '{{ Type }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.cloudformation.type_activations
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>type_activations</code> resource, the following permissions are required:

### Create
```json
cloudformation:ActivateType,
cloudformation:DescribeType,
iam:PassRole
```

### Update
```json
cloudformation:ActivateType,
cloudformation:DescribeType,
iam:PassRole
```

### Read
```json
cloudformation:DescribeType
```

### Delete
```json
cloudformation:DeactivateType,
cloudformation:DescribeType
```

### List
```json
cloudformation:ListTypes
```

