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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Gets or updates an individual <code>oidc_provider</code> resource, use <code>oidc_providers</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>oidc_provider</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::IAM::OIDCProvider</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iam.oidc_provider" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="client_id_list" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="url" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="thumbprint_list" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Amazon Resource Name (ARN) of the OIDC provider</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
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
client_id_list,
url,
thumbprint_list,
arn,
tags
FROM aws.iam.oidc_provider
WHERE data__Identifier = '<Arn>';
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

