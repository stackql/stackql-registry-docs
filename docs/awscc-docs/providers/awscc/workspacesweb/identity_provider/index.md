---
title: identity_provider
hide_title: false
hide_table_of_contents: false
keywords:
  - identity_provider
  - workspacesweb
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>identity_provider</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>identity_provider</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>identity_provider</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.workspacesweb.identity_provider</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>identity_provider_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>identity_provider_details</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>identity_provider_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>identity_provider_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>portal_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
identity_provider_arn,
identity_provider_details,
identity_provider_name,
identity_provider_type,
portal_arn
FROM awscc.workspacesweb.identity_provider
WHERE data__Identifier = '<IdentityProviderArn>';
```

## Permissions

To operate on the <code>identity_provider</code> resource, the following permissions are required:

### Read
```json
workspaces-web:GetIdentityProvider,
workspaces-web:ListIdentityProviders,
workspaces-web:ListTagsForResource
```

### Update
```json
workspaces-web:UpdateIdentityProvider,
workspaces-web:TagResource,
workspaces-web:UntagResource,
workspaces-web:GetIdentityProvider,
workspaces-web:ListIdentityProviders,
workspaces-web:ListTagsForResource
```

### Delete
```json
workspaces-web:GetIdentityProvider,
workspaces-web:DeleteIdentityProvider
```

