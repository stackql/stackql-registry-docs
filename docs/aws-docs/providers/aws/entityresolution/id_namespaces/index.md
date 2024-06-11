---
title: id_namespaces
hide_title: false
hide_table_of_contents: false
keywords:
  - id_namespaces
  - entityresolution
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

Creates, updates, deletes or gets an <code>id_namespace</code> resource or lists <code>id_namespaces</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>id_namespaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>IdNamespace defined in AWS Entity Resolution service</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.entityresolution.id_namespaces" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="id_namespace_name" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="input_source_config" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="id_mapping_workflow_properties" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="id_namespace_arn" /></td><td><code>string</code></td><td>The arn associated with the IdNamespace</td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td>The date and time when the IdNamespace was created</td></tr>
<tr><td><CopyableCode code="updated_at" /></td><td><code>string</code></td><td>The date and time when the IdNamespace was updated</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
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
    <td><CopyableCode code="IdNamespaceName, Type, region" /></td>
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
List all <code>id_namespaces</code> in a region.
```sql
SELECT
region,
id_namespace_name
FROM aws.entityresolution.id_namespaces
WHERE region = 'us-east-1';
```
Gets all properties from an <code>id_namespace</code>.
```sql
SELECT
region,
id_namespace_name,
description,
input_source_config,
id_mapping_workflow_properties,
type,
role_arn,
id_namespace_arn,
created_at,
updated_at,
tags
FROM aws.entityresolution.id_namespaces
WHERE region = 'us-east-1' AND data__Identifier = '<IdNamespaceName>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>id_namespace</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.entityresolution.id_namespaces (
 IdNamespaceName,
 Type,
 region
)
SELECT 
'{{ IdNamespaceName }}',
 '{{ Type }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.entityresolution.id_namespaces (
 IdNamespaceName,
 Description,
 InputSourceConfig,
 IdMappingWorkflowProperties,
 Type,
 RoleArn,
 Tags,
 region
)
SELECT 
 '{{ IdNamespaceName }}',
 '{{ Description }}',
 '{{ InputSourceConfig }}',
 '{{ IdMappingWorkflowProperties }}',
 '{{ Type }}',
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
  - name: id_namespace
    props:
      - name: IdNamespaceName
        value: '{{ IdNamespaceName }}'
      - name: Description
        value: '{{ Description }}'
      - name: InputSourceConfig
        value:
          - InputSourceARN: '{{ InputSourceARN }}'
            SchemaName: null
      - name: IdMappingWorkflowProperties
        value:
          - IdMappingType: '{{ IdMappingType }}'
            ProviderProperties:
              ProviderServiceArn: '{{ ProviderServiceArn }}'
              ProviderConfiguration: {}
      - name: Type
        value: '{{ Type }}'
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
DELETE FROM aws.entityresolution.id_namespaces
WHERE data__Identifier = '<IdNamespaceName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>id_namespaces</code> resource, the following permissions are required:

### Create
```json
entityresolution:CreateIdNamespace,
entityresolution:TagResource,
iam:PassRole
```

### Read
```json
entityresolution:GetIdNamespace,
entityresolution:ListTagsForResource
```

### Update
```json
entityresolution:UpdateIdNamespace,
entityresolution:ListTagsForResource,
entityresolution:TagResource,
entityresolution:UntagResource,
iam:PassRole
```

### Delete
```json
entityresolution:DeleteIdNamespace,
entityresolution:GetIdNamespace,
entityresolution:UntagResource
```

### List
```json
entityresolution:ListIdNamespaces
```

