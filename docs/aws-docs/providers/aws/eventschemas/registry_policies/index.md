---
title: registry_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - registry_policies
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

Creates, updates, deletes or gets a <code>registry_policy</code> resource or lists <code>registry_policies</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>registry_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EventSchemas::RegistryPolicy</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.eventschemas.registry_policies" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="policy" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="registry_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="revision_id" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="RegistryName, Policy, region" /></td>
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
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples

Gets all properties from an individual <code>registry_policy</code>.
```sql
SELECT
region,
id,
policy,
registry_name,
revision_id
FROM aws.eventschemas.registry_policies
WHERE region = 'us-east-1' AND data__Identifier = '<Id>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>registry_policy</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.eventschemas.registry_policies (
 Policy,
 RegistryName,
 region
)
SELECT 
'{{ Policy }}',
 '{{ RegistryName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.eventschemas.registry_policies (
 Policy,
 RegistryName,
 RevisionId,
 region
)
SELECT 
 '{{ Policy }}',
 '{{ RegistryName }}',
 '{{ RevisionId }}',
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
  - name: registry_policy
    props:
      - name: Policy
        value: {}
      - name: RegistryName
        value: '{{ RegistryName }}'
      - name: RevisionId
        value: '{{ RevisionId }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.eventschemas.registry_policies
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>registry_policies</code> resource, the following permissions are required:

### Create
```json
schemas:PutResourcePolicy,
schemas:GetResourcePolicy,
schemas:DescribeRegistry
```

### Delete
```json
schemas:DeleteResourcePolicy,
schemas:GetResourcePolicy
```

### Update
```json
schemas:PutResourcePolicy,
schemas:GetResourcePolicy
```

### Read
```json
schemas:GetResourcePolicy
```

