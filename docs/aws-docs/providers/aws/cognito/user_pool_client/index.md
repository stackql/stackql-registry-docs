---
title: user_pool_client
hide_title: false
hide_table_of_contents: false
keywords:
  - user_pool_client
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
Gets an individual <code>user_pool_client</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user_pool_client</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>user_pool_client</td></tr>
<tr><td><b>Id</b></td><td><code>aws.cognito.user_pool_client</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>AnalyticsConfiguration</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>GenerateSecret</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>CallbackURLs</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>IdTokenValidity</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>TokenValidityUnits</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>ReadAttributes</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>AllowedOAuthFlowsUserPoolClient</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>DefaultRedirectURI</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ClientName</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ExplicitAuthFlows</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>AccessTokenValidity</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>EnableTokenRevocation</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>EnablePropagateAdditionalUserContextData</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>AuthSessionValidity</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>AllowedOAuthScopes</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>SupportedIdentityProviders</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>UserPoolId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>AllowedOAuthFlows</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>ClientSecret</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>LogoutURLs</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>RefreshTokenValidity</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>WriteAttributes</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>PreventUserExistenceErrors</code></td><td><code>string</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.cognito.user_pool_client<br/>WHERE region = 'us-east-1'<br/>AND data__Identifier = '&lt;Id&gt;'
</pre>
