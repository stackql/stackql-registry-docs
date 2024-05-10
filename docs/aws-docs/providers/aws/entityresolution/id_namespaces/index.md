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


Used to retrieve a list of <code>id_namespaces</code> in a region or to create or delete a <code>id_namespaces</code> resource, use <code>id_namespace</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>id_namespaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>IdNamespace defined in AWS Entity Resolution service</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.entityresolution.id_namespaces" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="id_namespace_name" /></td><td><code>undefined</code></td><td></td></tr>
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
id_namespace_name
FROM aws.entityresolution.id_namespaces
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
 "IdNamespaceName": "{{ IdNamespaceName }}",
 "Type": "{{ Type }}"
}
>>>
--required properties only
INSERT INTO aws.entityresolution.id_namespaces (
 IdNamespaceName,
 Type,
 region
)
SELECT 
{{ .IdNamespaceName }},
 {{ .Type }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "IdNamespaceName": "{{ IdNamespaceName }}",
 "Description": "{{ Description }}",
 "InputSourceConfig": [
  {
   "InputSourceARN": "{{ InputSourceARN }}",
   "SchemaName": null
  }
 ],
 "IdMappingWorkflowProperties": [
  {
   "IdMappingType": "{{ IdMappingType }}",
   "ProviderProperties": {
    "ProviderServiceArn": "{{ ProviderServiceArn }}",
    "ProviderConfiguration": {}
   }
  }
 ],
 "Type": "{{ Type }}",
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
 {{ .IdNamespaceName }},
 {{ .Description }},
 {{ .InputSourceConfig }},
 {{ .IdMappingWorkflowProperties }},
 {{ .Type }},
 {{ .RoleArn }},
 {{ .Tags }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
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

