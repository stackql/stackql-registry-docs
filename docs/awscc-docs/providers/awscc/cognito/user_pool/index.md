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
<tr><td><b>Id</b></td><td><code>awscc.cognito.user_pool</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>user_pool_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>policies</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>account_recovery_setting</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>admin_create_user_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>alias_attributes</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>username_attributes</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>auto_verified_attributes</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>device_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>email_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>email_verification_message</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>email_verification_subject</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>deletion_protection</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>lambda_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>mfa_configuration</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>enabled_mfas</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>sms_authentication_message</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>sms_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>sms_verification_message</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>schema</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>username_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>user_attribute_update_settings</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>user_pool_tags</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>verification_message_template</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>user_pool_add_ons</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>provider_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>provider_url</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>user_pool_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
user_pool_name,
policies,
account_recovery_setting,
admin_create_user_config,
alias_attributes,
username_attributes,
auto_verified_attributes,
device_configuration,
email_configuration,
email_verification_message,
email_verification_subject,
deletion_protection,
lambda_config,
mfa_configuration,
enabled_mfas,
sms_authentication_message,
sms_configuration,
sms_verification_message,
schema,
username_configuration,
user_attribute_update_settings,
user_pool_tags,
verification_message_template,
user_pool_add_ons,
provider_name,
provider_url,
arn,
user_pool_id
FROM awscc.cognito.user_pool
WHERE region = 'us-east-1'
AND data__Identifier = '{UserPoolId}';
```

## Permissions

To operate on the <code>user_pool</code> resource, the following permissions are required:

### Read
```json
cognito-idp:DescribeUserPool
```

### Update
```json
cognito-idp:UpdateUserPool,
cognito-idp:ListTagsForResource,
cognito-idp:UntagResource,
cognito-idp:TagResource,
cognito-idp:SetUserPoolMfaConfig,
cognito-idp:AddCustomAttributes,
cognito-idp:DescribeUserPool,
iam:PassRole
```

### Delete
```json
cognito-idp:DeleteUserPool
```

