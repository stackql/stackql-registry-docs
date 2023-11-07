---
title: route
hide_title: false
hide_table_of_contents: false
keywords:
  - route
  - refactorspaces
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>route</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>route</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.refactorspaces.route</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>PathResourceToId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ApplicationIdentifier</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>EnvironmentIdentifier</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>RouteIdentifier</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>RouteType</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>ServiceIdentifier</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>DefaultRoute</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>UriPathRoute</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td>Metadata that you can assign to help organize the frameworks that you create. Each tag is a key-value pair.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.refactorspaces.route
WHERE region = 'us-east-1' AND data__Identifier = '&lt;EnvironmentIdentifier&gt;' AND data__Identifier = '&lt;ApplicationIdentifier&gt;' AND data__Identifier = '&lt;RouteIdentifier&gt;'
</pre>
