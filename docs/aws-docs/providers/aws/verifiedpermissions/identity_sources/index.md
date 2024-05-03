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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Used to retrieve a list of <code>identity_sources</code> in a region or create a <code>identity_sources</code> resource, use <code>identity_source</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>identity_sources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::VerifiedPermissions::IdentitySource Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.verifiedpermissions.identity_sources" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="identity_source_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="policy_store_id" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
identity_source_id,
policy_store_id
FROM aws.verifiedpermissions.identity_sources
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>identity_sources</code> resource, the following permissions are required:

### Create
```json
verifiedpermissions:CreateIdentitySource,
verifiedpermissions:GetIdentitySource,
cognito-idp:DescribeUserPool,
cognito-idp:ListUserPoolClients
```

### List
```json
verifiedpermissions:ListIdentitySources,
verifiedpermissions:GetIdentitySource,
cognito-idp:DescribeUserPool,
cognito-idp:ListUserPoolClients
```
