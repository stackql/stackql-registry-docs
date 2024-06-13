---
title: resource_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_sets
  - fms
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

Creates, updates, deletes or gets a <code>resource_set</code> resource or lists <code>resource_sets</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resource_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Creates an AWS Firewall Manager resource set.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.fms.resource_sets" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>A Base62 ID</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="resource_type_list" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="resources" /></td><td><code>array</code></td><td></td></tr>
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
    <td><CopyableCode code="Name, ResourceTypeList, region" /></td>
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
List all <code>resource_sets</code> in a region.
```sql
SELECT
region,
id
FROM aws.fms.resource_sets
WHERE region = 'us-east-1';
```
Gets all properties from a <code>resource_set</code>.
```sql
SELECT
region,
id,
name,
description,
resource_type_list,
resources,
tags
FROM aws.fms.resource_sets
WHERE region = 'us-east-1' AND data__Identifier = '<Id>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>resource_set</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.fms.resource_sets (
 Name,
 ResourceTypeList,
 region
)
SELECT 
'{{ Name }}',
 '{{ ResourceTypeList }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.fms.resource_sets (
 Name,
 Description,
 ResourceTypeList,
 Resources,
 Tags,
 region
)
SELECT 
 '{{ Name }}',
 '{{ Description }}',
 '{{ ResourceTypeList }}',
 '{{ Resources }}',
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
  - name: resource_set
    props:
      - name: Name
        value: '{{ Name }}'
      - name: Description
        value: '{{ Description }}'
      - name: ResourceTypeList
        value:
          - '{{ ResourceTypeList[0] }}'
      - name: Resources
        value:
          - '{{ Resources[0] }}'
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
DELETE FROM aws.fms.resource_sets
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>resource_sets</code> resource, the following permissions are required:

### Create
```json
fms:PutResourceSet,
fms:BatchAssociateResource,
fms:ListResourceSetResources,
fms:TagResource
```

### Update
```json
fms:PutResourceSet,
fms:BatchAssociateResource,
fms:BatchDisassociateResource,
fms:GetResourceSet,
fms:ListResourceSetResources,
fms:TagResource,
fms:UntagResource,
fms:ListTagsForResource
```

### Read
```json
fms:GetResourceSet,
fms:ListResourceSetResources,
fms:ListTagsForResource
```

### Delete
```json
fms:DeleteResourceSet
```

### List
```json
fms:ListResourceSets
```

