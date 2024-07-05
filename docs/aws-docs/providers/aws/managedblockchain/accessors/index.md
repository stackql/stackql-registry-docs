---
title: accessors
hide_title: false
hide_table_of_contents: false
keywords:
  - accessors
  - managedblockchain
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

Creates, updates, deletes or gets an <code>accessor</code> resource or lists <code>accessors</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>accessors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::ManagedBlockchain::com.amazonaws.taiga.webservice.api#Accessor Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.managedblockchain.accessors" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="billing_token" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="creation_date" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="accessor_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="network_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
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
    <td><CopyableCode code="AccessorType, region" /></td>
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
Gets all <code>accessors</code> in a region.
```sql
SELECT
region,
arn,
billing_token,
creation_date,
id,
status,
accessor_type,
network_type,
tags
FROM aws.managedblockchain.accessors
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>accessor</code>.
```sql
SELECT
region,
arn,
billing_token,
creation_date,
id,
status,
accessor_type,
network_type,
tags
FROM aws.managedblockchain.accessors
WHERE region = 'us-east-1' AND data__Identifier = '<Id>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>accessor</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.managedblockchain.accessors (
 AccessorType,
 region
)
SELECT 
'{{ AccessorType }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.managedblockchain.accessors (
 AccessorType,
 NetworkType,
 Tags,
 region
)
SELECT 
 '{{ AccessorType }}',
 '{{ NetworkType }}',
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
  - name: accessor
    props:
      - name: AccessorType
        value: '{{ AccessorType }}'
      - name: NetworkType
        value: '{{ NetworkType }}'
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
DELETE FROM aws.managedblockchain.accessors
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>accessors</code> resource, the following permissions are required:

### Create
```json
managedblockchain:CreateAccessor,
managedblockchain:TagResource,
managedblockchain:GetAccessor
```

### Read
```json
managedblockchain:GetAccessor
```

### Update
```json
managedblockchain:GetAccessor,
managedblockchain:CreateAccessor,
managedblockchain:TagResource,
managedblockchain:UntagResource
```

### Delete
```json
managedblockchain:DeleteAccessor
```

### List
```json
managedblockchain:ListAccessors
```

