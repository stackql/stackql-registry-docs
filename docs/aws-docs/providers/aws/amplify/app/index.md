---
title: app
hide_title: false
hide_table_of_contents: false
keywords:
  - app
  - amplify
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>app</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>app</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>app</td></tr>
<tr><td><b>Id</b></td><td><code>aws.amplify.app</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>AccessToken</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>AppId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>AppName</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>AutoBranchCreationConfig</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>BasicAuthConfig</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>BuildSpec</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>CustomHeaders</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>CustomRules</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>DefaultDomain</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>EnableBranchAutoDeletion</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>EnvironmentVariables</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>IAMServiceRole</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>OauthToken</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Platform</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Repository</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.amplify.app<br/>WHERE region = 'us-east-1'<br/>AND data__Identifier = '&lt;Arn&gt;'
</pre>
