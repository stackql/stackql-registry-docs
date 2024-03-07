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
Retrieves a list of <code>identity_sources</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>identity_sources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>identity_sources</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.verifiedpermissions.identity_sources</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>identity_source_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>policy_store_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>identity_sources</code> resource, the following permissions are required:

### Create
<pre>
verifiedpermissions:CreateIdentitySource,
verifiedpermissions:GetIdentitySource,
verifiedpermissions:UpdateIdentitySource,
verifiedpermissions:DeleteIdentitySource,
verifiedpermissions:ListIdentitySources,
cognito-idp:DescribeUserPool,
cognito-idp:ListUserPoolClients</pre>

### List
<pre>
verifiedpermissions:CreateIdentitySource,
verifiedpermissions:GetIdentitySource,
verifiedpermissions:UpdateIdentitySource,
verifiedpermissions:DeleteIdentitySource,
verifiedpermissions:ListIdentitySources,
cognito-idp:DescribeUserPool,
cognito-idp:ListUserPoolClients</pre>


## Example
```sql
SELECT
region,
identity_source_id,
policy_store_id
FROM awscc.verifiedpermissions.identity_sources
WHERE region = 'us-east-1'
```
