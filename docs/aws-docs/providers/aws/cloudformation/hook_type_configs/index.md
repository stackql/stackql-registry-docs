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


Used to retrieve a list of <code>hook_type_configs</code> in a region or to create or delete a <code>hook_type_configs</code> resource, use <code>hook_type_config</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>hook_type_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Specifies the configuration data for a registered hook in CloudFormation Registry.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cloudformation.hook_type_configs" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="configuration_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for the configuration data, in this account and region.</td></tr>
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
configuration_arn
FROM aws.cloudformation.hook_type_configs
WHERE region = 'us-east-1';
```

## `INSERT` Example

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
-- hook_type_config.iql (required properties only)
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
-- hook_type_config.iql (all properties)
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

## `DELETE` Example

```sql
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

### Delete
```json
cloudformation:SetTypeConfiguration
```

### List
```json
cloudformation:ListTypes,
cloudformation:BatchDescribeTypeConfigurations
```

