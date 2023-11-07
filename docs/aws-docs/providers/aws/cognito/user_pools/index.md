---
title: user_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - user_pools
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
Retrieves a list of <code>user_pools</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.cognito.user_pools</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>UserPoolTags</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>Policies</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Schema</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>AdminCreateUserConfig</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>UsernameConfiguration</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>UserPoolName</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>SmsVerificationMessage</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>UserAttributeUpdateSettings</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>EmailConfiguration</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>SmsConfiguration</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>EmailVerificationSubject</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>AccountRecoverySetting</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>VerificationMessageTemplate</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>ProviderURL</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>MfaConfiguration</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>DeletionProtection</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>SmsAuthenticationMessage</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ProviderName</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>UserPoolAddOns</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>AliasAttributes</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>EnabledMfas</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>LambdaConfig</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>UsernameAttributes</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>AutoVerifiedAttributes</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>DeviceConfiguration</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>EmailVerificationMessage</code></td><td><code>string</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.cognito.user_pools
WHERE region = 'us-east-1'
</pre>
