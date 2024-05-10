---
title: identity_pool_principal_tag
hide_title: false
hide_table_of_contents: false
keywords:
  - identity_pool_principal_tag
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Gets or updates an individual <code>identity_pool_principal_tag</code> resource, use <code>identity_pool_principal_tags</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>identity_pool_principal_tag</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Cognito::IdentityPoolPrincipalTag</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cognito.identity_pool_principal_tag" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="identity_pool_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="identity_provider_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="use_defaults" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="principal_tags" /></td><td><code>object</code></td><td></td></tr>
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
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
identity_pool_id,
identity_provider_name,
use_defaults,
principal_tags
FROM aws.cognito.identity_pool_principal_tag
WHERE region = 'us-east-1' AND data__Identifier = '<IdentityPoolId>|<IdentityProviderName>';
```


## Permissions

To operate on the <code>identity_pool_principal_tag</code> resource, the following permissions are required:

### Read
```json
cognito-identity:GetPrincipalTagAttributeMap
```

### Update
```json
cognito-identity:GetPrincipalTagAttributeMap,
cognito-identity:SetPrincipalTagAttributeMap
```

