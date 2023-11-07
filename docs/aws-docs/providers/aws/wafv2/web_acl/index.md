---
title: web_acl
hide_title: false
hide_table_of_contents: false
keywords:
  - web_acl
  - wafv2
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>web_acl</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>web_acl</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.wafv2.web_acl</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Arn</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Capacity</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>DefaultAction</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Description</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Name</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Id</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Scope</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Rules</code></td><td><code>array</code></td><td>Collection of Rules.</td></tr>
<tr><td><code>VisibilityConfig</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>LabelNamespace</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>CustomResponseBodies</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>CaptchaConfig</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>ChallengeConfig</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>TokenDomains</code></td><td><code>undefined</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.wafv2.web_acl
WHERE region = 'us-east-1' AND data__Identifier = '&lt;Name&gt;' AND data__Identifier = '&lt;Id&gt;' AND data__Identifier = '&lt;Scope&gt;'
</pre>
