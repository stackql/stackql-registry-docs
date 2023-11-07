---
title: crls
hide_title: false
hide_table_of_contents: false
keywords:
  - crls
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
Retrieves a list of <code>crls</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>crls</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>crls</td></tr>
<tr><td><b>Id</b></td><td><code>aws.rolesanywhere.crls</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>CrlData</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>CrlId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Enabled</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>TrustAnchorArn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.rolesanywhere.crls<br/>WHERE region = 'us-east-1'
</pre>
