---
title: account_aliases
hide_title: false
hide_table_of_contents: false
keywords:
  - account_aliases
  - supportapp
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

Creates, updates, deletes or gets an <code>account_alias</code> resource or lists <code>account_aliases</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>account_aliases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An AWS Support App resource that creates, updates, reads, and deletes a customer's account alias.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.supportapp.account_aliases" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="account_alias" /></td><td><code>string</code></td><td>An account alias associated with a customer's account.</td></tr>
<tr><td><CopyableCode code="account_alias_resource_id" /></td><td><code>string</code></td><td>Unique identifier representing an alias tied to an account</td></tr>
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
    <td><CopyableCode code="AccountAlias, region" /></td>
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
List all <code>account_aliases</code> in a region.
```sql
SELECT
region,
account_alias_resource_id
FROM aws.supportapp.account_aliases
WHERE region = 'us-east-1';
```
Gets all properties from an <code>account_alias</code>.
```sql
SELECT
region,
account_alias,
account_alias_resource_id
FROM aws.supportapp.account_aliases
WHERE region = 'us-east-1' AND data__Identifier = '<AccountAliasResourceId>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>account_alias</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.supportapp.account_aliases (
 AccountAlias,
 region
)
SELECT 
'{{ AccountAlias }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.supportapp.account_aliases (
 AccountAlias,
 region
)
SELECT 
 '{{ AccountAlias }}',
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
  - name: account_alias
    props:
      - name: AccountAlias
        value: '{{ AccountAlias }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.supportapp.account_aliases
WHERE data__Identifier = '<AccountAliasResourceId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>account_aliases</code> resource, the following permissions are required:

### Create
```json
supportapp:PutAccountAlias,
supportapp:GetAccountAlias
```

### Read
```json
supportapp:GetAccountAlias
```

### Update
```json
supportapp:PutAccountAlias,
supportapp:GetAccountAlias
```

### Delete
```json
supportapp:DeleteAccountAlias,
supportapp:GetAccountAlias
```

### List
```json
supportapp:GetAccountAlias
```

