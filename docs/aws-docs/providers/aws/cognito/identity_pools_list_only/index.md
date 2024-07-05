---
title: identity_pools_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - identity_pools_list_only
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

Lists <code>identity_pools</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/identity_pools/"><code>identity_pools</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>identity_pools_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Cognito::IdentityPool</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cognito.identity_pools_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="push_sync" /></td><td><code>object</code></td><td></td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Lists all <code>identity_pools</code> in a region.
```sql
SELECT
region,
id
FROM aws.cognito.identity_pools_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>identity_pools_list_only</code> resource, see <a href="/providers/aws/cognito/identity_pools/#permissions"><code>identity_pools</code></a>


