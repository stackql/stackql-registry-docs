---
title: user_pools_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - user_pools_list_only
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

Lists <code>user_pools</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/user_pools/"><code>user_pools</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user_pools_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Cognito::UserPool</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cognito.user_pools_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="user_pool_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="policies" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="account_recovery_setting" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="admin_create_user_config" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="alias_attributes" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="username_attributes" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="auto_verified_attributes" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="device_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="email_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="email_verification_message" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="email_verification_subject" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="deletion_protection" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="lambda_config" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="mfa_configuration" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="enabled_mfas" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="sms_authentication_message" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="sms_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="sms_verification_message" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="schema" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="username_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="user_attribute_update_settings" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="user_pool_tags" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="verification_message_template" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="user_pool_add_ons" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="provider_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="provider_url" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="user_pool_id" /></td><td><code>string</code></td><td></td></tr>
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
Lists all <code>user_pools</code> in a region.
```sql
SELECT
region,
user_pool_id
FROM aws.cognito.user_pools_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>user_pools_list_only</code> resource, see <a href="/providers/aws/cognito/user_pools/#permissions"><code>user_pools</code></a>


