---
title: lifecycle_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - lifecycle_policies
  - opensearchserverless
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

Creates, updates, deletes or gets a <code>lifecycle_policy</code> resource or lists <code>lifecycle_policies</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>lifecycle_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Amazon OpenSearchServerless lifecycle policy resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.opensearchserverless.lifecycle_policies" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the policy</td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>The type of lifecycle policy</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the policy</td></tr>
<tr><td><CopyableCode code="policy" /></td><td><code>string</code></td><td>The JSON policy document that is the content for the policy</td></tr>
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
    <td><CopyableCode code="Type, Name, Policy, region" /></td>
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
List all <code>lifecycle_policies</code> in a region.
```sql
SELECT
region,
type,
name
FROM aws.opensearchserverless.lifecycle_policies
WHERE region = 'us-east-1';
```
Gets all properties from a <code>lifecycle_policy</code>.
```sql
SELECT
region,
name,
type,
description,
policy
FROM aws.opensearchserverless.lifecycle_policies
WHERE region = 'us-east-1' AND data__Identifier = '<Type>|<Name>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>lifecycle_policy</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.opensearchserverless.lifecycle_policies (
 Name,
 Type,
 Policy,
 region
)
SELECT 
'{{ Name }}',
 '{{ Type }}',
 '{{ Policy }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.opensearchserverless.lifecycle_policies (
 Name,
 Type,
 Description,
 Policy,
 region
)
SELECT 
 '{{ Name }}',
 '{{ Type }}',
 '{{ Description }}',
 '{{ Policy }}',
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
  - name: lifecycle_policy
    props:
      - name: Name
        value: '{{ Name }}'
      - name: Type
        value: '{{ Type }}'
      - name: Description
        value: '{{ Description }}'
      - name: Policy
        value: '{{ Policy }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.opensearchserverless.lifecycle_policies
WHERE data__Identifier = '<Type|Name>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>lifecycle_policies</code> resource, the following permissions are required:

### Create
```json
aoss:CreateLifecyclePolicy
```

### Read
```json
aoss:BatchGetLifecyclePolicy
```

### Update
```json
aoss:UpdateLifecyclePolicy,
aoss:BatchGetLifecyclePolicy
```

### Delete
```json
aoss:DeleteLifecyclePolicy
```

### List
```json
aoss:ListLifecyclePolicies
```

