---
title: route
hide_title: false
hide_table_of_contents: false
keywords:
  - route
  - appmesh
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
<tr><td><b>Id</b></td><td><code>aws.appmesh.route</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Uid</code></td><td><code>string</code></td><td></td></tr><tr><td><code>MeshName</code></td><td><code>string</code></td><td></td></tr><tr><td><code>VirtualRouterName</code></td><td><code>string</code></td><td></td></tr><tr><td><code>MeshOwner</code></td><td><code>string</code></td><td></td></tr><tr><td><code>ResourceOwner</code></td><td><code>string</code></td><td></td></tr><tr><td><code>RouteName</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Arn</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Spec</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.appmesh.route
WHERE region = 'us-east-1' AND data__Identifier = '{Id}'
</pre>
