---
title: user_pool
hide_title: false
hide_table_of_contents: false
keywords:
  - user_pool
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
Gets an individual <code>user_pool</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user_pool</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>user_pool</td></tr>
<tr><td><b>Id</b></td><td><code>aws.cognito.user_pool</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>user_pool_tags</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>policies</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>schema</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>admin_create_user_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>username_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>user_pool_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>sms_verification_message</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>user_attribute_update_settings</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>email_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>sms_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>email_verification_subject</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>account_recovery_setting</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>verification_message_template</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>provider_ur_l</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>mfa_configuration</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>deletion_protection</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>sms_authentication_message</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>provider_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>user_pool_add_ons</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>alias_attributes</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>enabled_mfas</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>lambda_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>username_attributes</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>auto_verified_attributes</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>device_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>email_verification_message</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
user_pool_tags,
policies,
schema,
admin_create_user_config,
username_configuration,
user_pool_name,
sms_verification_message,
user_attribute_update_settings,
email_configuration,
sms_configuration,
email_verification_subject,
account_recovery_setting,
verification_message_template,
provider_ur_l,
mfa_configuration,
deletion_protection,
sms_authentication_message,
provider_name,
user_pool_add_ons,
alias_attributes,
enabled_mfas,
lambda_config,
id,
arn,
username_attributes,
auto_verified_attributes,
device_configuration,
email_verification_message
FROM aws.cognito.user_pool
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```
