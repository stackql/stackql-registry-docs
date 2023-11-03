---
title: authorizer
hide_title: false
hide_table_of_contents: false
keywords:
  - authorizer
  - iot
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>authorizer</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>authorizer</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.iot.authorizer</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>AuthorizerFunctionArn</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Arn</code></td><td><code>string</code></td><td></td></tr><tr><td><code>AuthorizerName</code></td><td><code>string</code></td><td></td></tr><tr><td><code>SigningDisabled</code></td><td><code>boolean</code></td><td></td></tr><tr><td><code>Status</code></td><td><code>string</code></td><td></td></tr><tr><td><code>TokenKeyName</code></td><td><code>string</code></td><td></td></tr><tr><td><code>TokenSigningPublicKeys</code></td><td><code>object</code></td><td></td></tr><tr><td><code>EnableCachingForHttp</code></td><td><code>boolean</code></td><td></td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.iot.authorizer
WHERE region = 'us-east-1' AND data__Identifier = '{AuthorizerName}'
</pre>
