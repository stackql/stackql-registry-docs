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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Gets or updates an individual <code>identity_provider</code> resource, use <code>identity_providers</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>identity_provider</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::WorkSpacesWeb::IdentityProvider Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.workspacesweb.identity_provider" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="identity_provider_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="identity_provider_details" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="identity_provider_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="identity_provider_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="portal_arn" /></td><td><code>string</code></td><td></td></tr>
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
identity_provider_arn,
identity_provider_details,
identity_provider_name,
identity_provider_type,
portal_arn
FROM aws.workspacesweb.identity_provider
WHERE region = 'us-east-1' AND data__Identifier = '<IdentityProviderArn>';
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

