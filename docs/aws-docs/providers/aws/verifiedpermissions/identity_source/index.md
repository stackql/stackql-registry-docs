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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Gets or operates on an individual <code>identity_source</code> resource, use <code>identity_sources</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>identity_source</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::VerifiedPermissions::IdentitySource Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.verifiedpermissions.identity_source" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="details" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="identity_source_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="policy_store_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="principal_entity_type" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
configuration,
details,
identity_source_id,
policy_store_id,
principal_entity_type
FROM aws.verifiedpermissions.identity_source
WHERE data__Identifier = '<IdentitySourceId>|<PolicyStoreId>';
```

## Permissions

To operate on the <code>identity_source</code> resource, the following permissions are required:

### Read
```json
verifiedpermissions:GetIdentitySource,
cognito-idp:DescribeUserPool,
cognito-idp:ListUserPoolClients
```

### Update
```json
verifiedpermissions:UpdateIdentitySource,
verifiedpermissions:GetIdentitySource,
cognito-idp:DescribeUserPool,
cognito-idp:ListUserPoolClients
```

### Delete
```json
verifiedpermissions:DeleteIdentitySource,
verifiedpermissions:GetIdentitySource,
cognito-idp:DescribeUserPool,
cognito-idp:ListUserPoolClients
```
