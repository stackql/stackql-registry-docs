---
title: meshes
hide_title: false
hide_table_of_contents: false
keywords:
  - meshes
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
Retrieves a list of <code>meshes</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>meshes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>meshes</td></tr>
<tr><td><b>Id</b></td><td><code>aws.appmesh.meshes</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Uid</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>MeshName</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>MeshOwner</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ResourceOwner</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Spec</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.appmesh.meshes<br/>WHERE region = 'us-east-1'
</pre>
