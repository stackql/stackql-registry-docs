---
title: registries
hide_title: false
hide_table_of_contents: false
keywords:
  - registries
  - eventschemas
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

Creates, updates, deletes or gets a <code>registry</code> resource or lists <code>registries</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>registries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EventSchemas::Registry</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.eventschemas.registries" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="registry_name" /></td><td><code>string</code></td><td>The name of the schema registry.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A description of the registry to be created.</td></tr>
<tr><td><CopyableCode code="registry_arn" /></td><td><code>string</code></td><td>The ARN of the registry.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>Tags associated with the resource.</td></tr>
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
Gets all <code>registries</code> in a region.
```sql
SELECT
region,
registry_name,
description,
registry_arn,
tags
FROM aws.eventschemas.registries
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>registry</code>.
```sql
SELECT
region,
registry_name,
description,
registry_arn,
tags
FROM aws.eventschemas.registries
WHERE region = 'us-east-1' AND data__Identifier = '<RegistryArn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>registry</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.eventschemas.registries (
 RegistryName,
 Description,
 Tags,
 region
)
SELECT 
'{{ RegistryName }}',
 '{{ Description }}',
 '{{ Tags }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.eventschemas.registries (
 RegistryName,
 Description,
 Tags,
 region
)
SELECT 
 '{{ RegistryName }}',
 '{{ Description }}',
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
  - name: registry
    props:
      - name: RegistryName
        value: '{{ RegistryName }}'
      - name: Description
        value: '{{ Description }}'
      - name: Tags
        value:
          - Value: '{{ Value }}'
            Key: '{{ Key }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.eventschemas.registries
WHERE data__Identifier = '<RegistryArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>registries</code> resource, the following permissions are required:

### Create
```json
schemas:DescribeRegistry,
schemas:CreateRegistry,
schemas:TagResource
```

### Read
```json
schemas:DescribeRegistry
```

### Update
```json
schemas:DescribeRegistry,
schemas:UpdateRegistry,
schemas:TagResource,
schemas:UntagResource,
schemas:ListTagsForResource
```

### Delete
```json
schemas:DescribeRegistry,
schemas:DeleteRegistry
```

### List
```json
schemas:ListRegistries
```

