---
title: identity_sources
hide_title: false
hide_table_of_contents: false
keywords:
  - identity_sources
  - verifiedpermissions
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

Creates, updates, deletes or gets an <code>identity_source</code> resource or lists <code>identity_sources</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>identity_sources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::VerifiedPermissions::IdentitySource Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.verifiedpermissions.identity_sources" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="configuration" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="details" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="identity_source_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="policy_store_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="principal_entity_type" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="Configuration, PolicyStoreId, region" /></td>
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
List all <code>identity_sources</code> in a region.
```sql
SELECT
region,
identity_source_id,
policy_store_id
FROM aws.verifiedpermissions.identity_sources
WHERE region = 'us-east-1';
```
Gets all properties from an <code>identity_source</code>.
```sql
SELECT
region,
configuration,
details,
identity_source_id,
policy_store_id,
principal_entity_type
FROM aws.verifiedpermissions.identity_sources
WHERE region = 'us-east-1' AND data__Identifier = '<IdentitySourceId>|<PolicyStoreId>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>identity_source</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.verifiedpermissions.identity_sources (
 Configuration,
 PolicyStoreId,
 region
)
SELECT 
'{{ Configuration }}',
 '{{ PolicyStoreId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.verifiedpermissions.identity_sources (
 Configuration,
 PolicyStoreId,
 PrincipalEntityType,
 region
)
SELECT 
 '{{ Configuration }}',
 '{{ PolicyStoreId }}',
 '{{ PrincipalEntityType }}',
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
  - name: identity_source
    props:
      - name: Configuration
        value: null
      - name: PolicyStoreId
        value: '{{ PolicyStoreId }}'
      - name: PrincipalEntityType
        value: '{{ PrincipalEntityType }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.verifiedpermissions.identity_sources
WHERE data__Identifier = '<IdentitySourceId|PolicyStoreId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>identity_sources</code> resource, the following permissions are required:

### Create
```json
verifiedpermissions:CreateIdentitySource,
verifiedpermissions:GetIdentitySource,
cognito-idp:DescribeUserPool,
cognito-idp:ListUserPoolClients
```

### Read
```json
verifiedpermissions:GetIdentitySource,
cognito-idp:DescribeUserPool,
cognito-idp:ListUserPoolClients
```

### Update
```json
verifiedpermissions:UpdateIdentitySource,
verifiedpermissions:GetIdentitySource,
cognito-idp:DescribeUserPool,
cognito-idp:ListUserPoolClients
```

### Delete
```json
verifiedpermissions:DeleteIdentitySource,
verifiedpermissions:GetIdentitySource,
cognito-idp:DescribeUserPool,
cognito-idp:ListUserPoolClients
```

### List
```json
verifiedpermissions:ListIdentitySources,
verifiedpermissions:GetIdentitySource,
cognito-idp:DescribeUserPool,
cognito-idp:ListUserPoolClients
```

