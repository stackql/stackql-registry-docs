---
title: trust_anchor
hide_title: false
hide_table_of_contents: false
keywords:
  - trust_anchor
  - rolesanywhere
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>trust_anchor</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>trust_anchor</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>trust_anchor</td></tr>
<tr><td><b>Id</b></td><td><code>aws.rolesanywhere.trust_anchor</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Enabled</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Source</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>TrustAnchorId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>TrustAnchorArn</code></td><td><code>string</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.rolesanywhere.trust_anchor<br/>WHERE region = 'us-east-1'<br/>AND data__Identifier = '&lt;TrustAnchorId&gt;'
</pre>
