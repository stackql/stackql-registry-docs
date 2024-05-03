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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Used to retrieve a list of <code>identity_provider_configs</code> in a region or create a <code>identity_provider_configs</code> resource, use <code>identity_provider_config</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>identity_provider_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An object representing an Amazon EKS IdentityProviderConfig.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.eks.identity_provider_configs" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="identity_provider_config_name" /></td><td><code>string</code></td><td>The name of the OIDC provider configuration.</td></tr>
<tr><td><CopyableCode code="cluster_name" /></td><td><code>string</code></td><td>The name of the identity provider configuration.</td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>The type of the identity provider configuration.</td></tr>
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
identity_provider_config_name,
cluster_name,
type
FROM aws.eks.identity_provider_configs
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>identity_provider_configs</code> resource, the following permissions are required:

### Create
```json
eks:DescribeUpdate,
eks:AssociateIdentityProviderConfig,
eks:DescribeIdentityProviderConfig,
eks:TagResource
```

### List
```json
eks:ListIdentityProviderConfigs
```

