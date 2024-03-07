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
Retrieves a list of <code>identity_pool_principal_tags</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>identity_pool_principal_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>identity_pool_principal_tags</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.cognito.identity_pool_principal_tags</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>identity_pool_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>identity_provider_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>identity_pool_principal_tags</code> resource, the following permissions are required:

### Create
<pre>
cognito-identity:GetPrincipalTagAttributeMap,
cognito-identity:SetPrincipalTagAttributeMap</pre>

### List
<pre>
cognito-identity:GetPrincipalTagAttributeMap</pre>


## Example
```sql
SELECT
region,
identity_pool_id,
identity_provider_name
FROM awscc.cognito.identity_pool_principal_tags
WHERE region = 'us-east-1'
```
