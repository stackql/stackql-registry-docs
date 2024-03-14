---
title: identity_pool_principal_tag
hide_title: false
hide_table_of_contents: false
keywords:
  - identity_pool_principal_tag
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
Gets an individual <code>identity_pool_principal_tag</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>identity_pool_principal_tag</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>identity_pool_principal_tag</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.cognito.identity_pool_principal_tag</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>identity_pool_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>identity_provider_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>use_defaults</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>principal_tags</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
identity_pool_id,
identity_provider_name,
use_defaults,
principal_tags
FROM awscc.cognito.identity_pool_principal_tag
WHERE data__Identifier = '<IdentityPoolId>|<IdentityProviderName>';
```

## Permissions

To operate on the <code>identity_pool_principal_tag</code> resource, the following permissions are required:

### Read
```json
cognito-identity:GetPrincipalTagAttributeMap
```

### Update
```json
cognito-identity:GetPrincipalTagAttributeMap,
cognito-identity:SetPrincipalTagAttributeMap
```

### Delete
```json
cognito-identity:GetPrincipalTagAttributeMap,
cognito-identity:SetPrincipalTagAttributeMap
```

