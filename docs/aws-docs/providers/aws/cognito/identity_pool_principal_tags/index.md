---
title: identity_pool_principal_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - identity_pool_principal_tags
  - cognito
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


Used to retrieve a list of <code>identity_pool_principal_tags</code> in a region or to create or delete a <code>identity_pool_principal_tags</code> resource, use <code>identity_pool_principal_tag</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>identity_pool_principal_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Cognito::IdentityPoolPrincipalTag</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cognito.identity_pool_principal_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="identity_pool_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="identity_provider_name" /></td><td><code>string</code></td><td></td></tr>
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
identity_pool_id,
identity_provider_name
FROM aws.cognito.identity_pool_principal_tags
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
 "IdentityPoolId": "{{ IdentityPoolId }}",
 "IdentityProviderName": "{{ IdentityProviderName }}"
}
>>>
--required properties only
INSERT INTO aws.cognito.identity_pool_principal_tags (
 IdentityPoolId,
 IdentityProviderName,
 region
)
SELECT 
{{ IdentityPoolId }},
 {{ IdentityProviderName }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "IdentityPoolId": "{{ IdentityPoolId }}",
 "IdentityProviderName": "{{ IdentityProviderName }}",
 "UseDefaults": "{{ UseDefaults }}",
 "PrincipalTags": {}
}
>>>
--all properties
INSERT INTO aws.cognito.identity_pool_principal_tags (
 IdentityPoolId,
 IdentityProviderName,
 UseDefaults,
 PrincipalTags,
 region
)
SELECT 
 {{ IdentityPoolId }},
 {{ IdentityProviderName }},
 {{ UseDefaults }},
 {{ PrincipalTags }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.cognito.identity_pool_principal_tags
WHERE data__Identifier = '<IdentityPoolId|IdentityProviderName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>identity_pool_principal_tags</code> resource, the following permissions are required:

### Create
```json
cognito-identity:GetPrincipalTagAttributeMap,
cognito-identity:SetPrincipalTagAttributeMap
```

### Delete
```json
cognito-identity:GetPrincipalTagAttributeMap,
cognito-identity:SetPrincipalTagAttributeMap
```

### List
```json
cognito-identity:GetPrincipalTagAttributeMap
```

