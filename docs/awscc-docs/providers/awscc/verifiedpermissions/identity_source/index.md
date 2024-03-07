---
title: identity_source
hide_title: false
hide_table_of_contents: false
keywords:
  - identity_source
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
Gets an individual <code>identity_source</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>identity_source</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>identity_source</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.verifiedpermissions.identity_source</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>details</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>identity_source_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>policy_store_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>principal_entity_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
configuration,
details,
identity_source_id,
policy_store_id,
principal_entity_type
FROM awscc.verifiedpermissions.identity_source
WHERE region = 'us-east-1'
AND data__Identifier = '{IdentitySourceId}';
AND data__Identifier = '{PolicyStoreId}';
```

## Permissions

To operate on the <code>identity_source</code> resource, the following permissions are required:

### Read
```json
verifiedpermissions:CreateIdentitySource,
verifiedpermissions:GetIdentitySource,
verifiedpermissions:UpdateIdentitySource,
verifiedpermissions:DeleteIdentitySource,
verifiedpermissions:ListIdentitySources,
cognito-idp:DescribeUserPool,
cognito-idp:ListUserPoolClients
```

### Update
```json
verifiedpermissions:CreateIdentitySource,
verifiedpermissions:GetIdentitySource,
verifiedpermissions:UpdateIdentitySource,
verifiedpermissions:DeleteIdentitySource,
verifiedpermissions:ListIdentitySources,
cognito-idp:DescribeUserPool,
cognito-idp:ListUserPoolClients
```

### Delete
```json
verifiedpermissions:CreateIdentitySource,
verifiedpermissions:GetIdentitySource,
verifiedpermissions:UpdateIdentitySource,
verifiedpermissions:DeleteIdentitySource,
verifiedpermissions:ListIdentitySources,
cognito-idp:DescribeUserPool,
cognito-idp:ListUserPoolClients
```

