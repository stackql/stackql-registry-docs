---
title: identity_pool
hide_title: false
hide_table_of_contents: false
keywords:
  - identity_pool
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
Gets an individual <code>identity_pool</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>identity_pool</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>identity_pool</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.cognito.identity_pool</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>push_sync</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>cognito_identity_providers</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>developer_provider_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>cognito_streams</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>supported_login_providers</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>cognito_events</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>identity_pool_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>allow_unauthenticated_identities</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>saml_provider_ar_ns</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>open_id_connect_provider_ar_ns</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>allow_classic_flow</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
push_sync,
cognito_identity_providers,
developer_provider_name,
cognito_streams,
supported_login_providers,
name,
cognito_events,
id,
identity_pool_name,
allow_unauthenticated_identities,
saml_provider_ar_ns,
open_id_connect_provider_ar_ns,
allow_classic_flow
FROM awscc.cognito.identity_pool
WHERE region = 'us-east-1'
AND data__Identifier = '{Id}';
```

## Permissions

To operate on the <code>identity_pool</code> resource, the following permissions are required:

### Read
```json
cognito-identity:DescribeIdentityPool
```

### Update
```json
cognito-identity:UpdateIdentityPool,
cognito-identity:DescribeIdentityPool,
cognito-sync:SetIdentityPoolConfiguration,
cognito-sync:SetCognitoEvents,
iam:PassRole
```

### Delete
```json
cognito-identity:DeleteIdentityPool
```

