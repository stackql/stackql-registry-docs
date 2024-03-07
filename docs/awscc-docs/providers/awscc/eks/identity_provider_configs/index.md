---
title: identity_provider_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - identity_provider_configs
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
Retrieves a list of <code>identity_provider_configs</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>identity_provider_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>identity_provider_configs</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.eks.identity_provider_configs</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>identity_provider_config_name</code></td><td><code>string</code></td><td>The name of the OIDC provider configuration.</td></tr>
<tr><td><code>cluster_name</code></td><td><code>string</code></td><td>The name of the identity provider configuration.</td></tr>
<tr><td><code>type</code></td><td><code>string</code></td><td>The type of the identity provider configuration.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>identity_provider_configs</code> resource, the following permissions are required:

### Create
<pre>
eks:DescribeUpdate,
eks:AssociateIdentityProviderConfig,
eks:DescribeIdentityProviderConfig,
eks:TagResource</pre>

### List
<pre>
eks:ListIdentityProviderConfigs</pre>


## Example
```sql
SELECT
region,
identity_provider_config_name,
cluster_name,
type
FROM awscc.eks.identity_provider_configs
WHERE region = 'us-east-1'
```
