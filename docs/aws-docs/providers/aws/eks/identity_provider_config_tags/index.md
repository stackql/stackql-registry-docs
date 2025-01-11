---
title: identity_provider_config_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - identity_provider_config_tags
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Expands all tag keys and values for <code>identity_provider_configs</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>identity_provider_config_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An object representing an Amazon EKS IdentityProviderConfig.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.eks.identity_provider_config_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="cluster_name" /></td><td><code>string</code></td><td>The name of the identity provider configuration.</td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>The type of the identity provider configuration.</td></tr>
<tr><td><CopyableCode code="identity_provider_config_name" /></td><td><code>string</code></td><td>The name of the OIDC provider configuration.</td></tr>
<tr><td><CopyableCode code="oidc" /></td><td><code>object</code></td><td>An object representing an OpenID Connect (OIDC) configuration.</td></tr>
<tr><td><CopyableCode code="identity_provider_config_arn" /></td><td><code>string</code></td><td>The ARN of the configuration.</td></tr>
<tr><td><CopyableCode code="tag_key" /></td><td><code>string</code></td><td>Tag key.</td></tr>
<tr><td><CopyableCode code="tag_value" /></td><td><code>string</code></td><td>Tag value.</td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Expands tags for all <code>identity_provider_configs</code> in a region.
```sql
SELECT
region,
cluster_name,
type,
identity_provider_config_name,
oidc,
identity_provider_config_arn,
tag_key,
tag_value
FROM aws.eks.identity_provider_config_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>identity_provider_config_tags</code> resource, see <a href="/providers/aws/eks/identity_provider_configs/#permissions"><code>identity_provider_configs</code></a>

