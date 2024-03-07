---
title: oidc_provider
hide_title: false
hide_table_of_contents: false
keywords:
  - oidc_provider
  - iam
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>oidc_provider</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>oidc_provider</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>oidc_provider</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.iam.oidc_provider</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>client_id_list</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>url</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>thumbprint_list</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>Amazon Resource Name (ARN) of the OIDC provider</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
client_id_list,
url,
thumbprint_list,
arn,
tags
FROM awscc.iam.oidc_provider
WHERE data__Identifier = '{Arn}';
```

## Permissions

To operate on the <code>oidc_provider</code> resource, the following permissions are required:

### Read
```json
iam:GetOpenIDConnectProvider
```

### Update
```json
iam:UpdateOpenIDConnectProviderThumbprint,
iam:RemoveClientIDFromOpenIDConnectProvider,
iam:AddClientIDToOpenIDConnectProvider,
iam:GetOpenIDConnectProvider,
iam:TagOpenIDConnectProvider,
iam:UntagOpenIDConnectProvider,
iam:ListOpenIDConnectProviderTags
```

### Delete
```json
iam:DeleteOpenIDConnectProvider
```

