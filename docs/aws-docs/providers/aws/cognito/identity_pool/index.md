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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Gets or updates an individual <code>identity_pool</code> resource, use <code>identity_pools</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>identity_pool</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Cognito::IdentityPool</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cognito.identity_pool" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="push_sync" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="cognito_identity_providers" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="developer_provider_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="cognito_streams" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="supported_login_providers" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="cognito_events" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="identity_pool_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="allow_unauthenticated_identities" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="saml_provider_arns" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="open_id_connect_provider_arns" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="allow_classic_flow" /></td><td><code>boolean</code></td><td></td></tr>
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
saml_provider_arns,
open_id_connect_provider_arns,
allow_classic_flow
FROM aws.cognito.identity_pool
WHERE region = 'us-east-1' AND data__Identifier = '<Id>';
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

