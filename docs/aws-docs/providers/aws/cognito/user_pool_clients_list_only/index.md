---
title: user_pool_clients_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - user_pool_clients_list_only
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

Lists <code>user_pool_clients</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/user_pool_clients/"><code>user_pool_clients</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user_pool_clients_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Cognito::UserPoolClient</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cognito.user_pool_clients_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="client_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="explicit_auth_flows" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="generate_secret" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="read_attributes" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="auth_session_validity" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="refresh_token_validity" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="access_token_validity" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="id_token_validity" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="token_validity_units" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="user_pool_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="write_attributes" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="allowed_oauth_flows" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="allowed_oauth_flows_user_pool_client" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="allowed_oauth_scopes" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="callback_urls" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="default_redirect_uri" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="logout_urls" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="supported_identity_providers" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="analytics_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="prevent_user_existence_errors" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="enable_token_revocation" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="enable_propagate_additional_user_context_data" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="client_secret" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="client_id" /></td><td><code>string</code></td><td></td></tr>
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
Lists all <code>user_pool_clients</code> in a region.
```sql
SELECT
region,
user_pool_id,
client_id
FROM aws.cognito.user_pool_clients_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>user_pool_clients_list_only</code> resource, see <a href="/providers/aws/cognito/user_pool_clients/#permissions"><code>user_pool_clients</code></a>


