---
title: identity_provider_config
hide_title: false
hide_table_of_contents: false
keywords:
  - identity_provider_config
  - eks
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>identity_provider_config</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>identity_provider_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>identity_provider_config</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.eks.identity_provider_config</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>cluster_name</code></td><td><code>string</code></td><td>The name of the identity provider configuration.</td></tr>
<tr><td><code>type</code></td><td><code>string</code></td><td>The type of the identity provider configuration.</td></tr>
<tr><td><code>identity_provider_config_name</code></td><td><code>string</code></td><td>The name of the OIDC provider configuration.</td></tr>
<tr><td><code>oidc</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>identity_provider_config_arn</code></td><td><code>string</code></td><td>The ARN of the configuration.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>identity_provider_config</code> resource, the following permissions are required:

### Read
```json
eks:DescribeIdentityProviderConfig
```

### Update
```json
eks:DescribeIdentityProviderConfig,
eks:TagResource,
eks:UntagResource
```

### Delete
```json
eks:DisassociateIdentityProviderConfig,
eks:DescribeIdentityProviderConfig
```


## Example
```sql
SELECT
region,
cluster_name,
type,
identity_provider_config_name,
oidc,
tags,
identity_provider_config_arn
FROM awscc.eks.identity_provider_config
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;IdentityProviderConfigName&gt;'
AND data__Identifier = '&lt;ClusterName&gt;'
AND data__Identifier = '&lt;Type&gt;'
```
