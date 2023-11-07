---
title: app
hide_title: false
hide_table_of_contents: false
keywords:
  - app
  - opsworks
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
null
<tr><td><b>Id</b></td><td><code>aws.opsworks.app</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>AppSource</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Attributes</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>DataSources</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Domains</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>EnableSsl</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>Environment</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Shortname</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>SslConfiguration</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>StackId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Type</code></td><td><code>string</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.opsworks.app
WHERE region = 'us-east-1' AND data__Identifier = '&lt;Id&gt;'
</pre>
