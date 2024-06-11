---
title: hook_type_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - hook_type_configs
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

Creates, updates, deletes or gets a <code>hook_type_config</code> resource or lists <code>hook_type_configs</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>hook_type_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Specifies the configuration data for a registered hook in CloudFormation Registry.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cloudformation.hook_type_configs" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="type_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the type without version number.</td></tr>
<tr><td><CopyableCode code="type_name" /></td><td><code>string</code></td><td>The name of the type being registered. We recommend that type names adhere to the following pattern: company_or_organization::service::type.</td></tr>
<tr><td><CopyableCode code="configuration_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for the configuration data, in this account and region.</td></tr>
<tr><td><CopyableCode code="configuration" /></td><td><code>string</code></td><td>The configuration data for the extension, in this account and region.</td></tr>
<tr><td><CopyableCode code="configuration_alias" /></td><td><code>string</code></td><td>An alias by which to refer to this extension configuration data.</td></tr>
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
List all <code>hook_type_configs</code> in a region.
```sql
SELECT
region,
configuration_arn
FROM aws.cloudformation.hook_type_configs
WHERE region = 'us-east-1';
```
Gets all properties from a <code>hook_type_config</code>.
```sql
SELECT
region,
type_arn,
type_name,
configuration_arn,
configuration,
configuration_alias
FROM aws.cloudformation.hook_type_configs
WHERE region = 'us-east-1' AND data__Identifier = '<ConfigurationArn>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>hook_type_config</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.cloudformation.hook_type_configs (
 TypeArn,
 TypeName,
 Configuration,
 ConfigurationAlias,
 region
)
SELECT 
'{{ TypeArn }}',
 '{{ TypeName }}',
 '{{ Configuration }}',
 '{{ ConfigurationAlias }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.cloudformation.hook_type_configs (
 TypeArn,
 TypeName,
 Configuration,
 ConfigurationAlias,
 region
)
SELECT 
 '{{ TypeArn }}',
 '{{ TypeName }}',
 '{{ Configuration }}',
 '{{ ConfigurationAlias }}',
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
  - name: hook_type_config
    props:
      - name: TypeArn
        value: '{{ TypeArn }}'
      - name: TypeName
        value: '{{ TypeName }}'
      - name: Configuration
        value: '{{ Configuration }}'
      - name: ConfigurationAlias
        value: '{{ ConfigurationAlias }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.cloudformation.hook_type_configs
WHERE data__Identifier = '<ConfigurationArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>hook_type_configs</code> resource, the following permissions are required:

### Create
```json
cloudformation:SetTypeConfiguration
```

### Read
```json
cloudformation:BatchDescribeTypeConfigurations
```

### Update
```json
cloudformation:SetTypeConfiguration
```

### Delete
```json
cloudformation:SetTypeConfiguration
```

### List
```json
cloudformation:ListTypes,
cloudformation:BatchDescribeTypeConfigurations
```

