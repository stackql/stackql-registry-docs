---
title: default_view_associations
hide_title: false
hide_table_of_contents: false
keywords:
  - default_view_associations
  - resourceexplorer2
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>default_view_associations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>default_view_associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>default_view_associations</td></tr>
<tr><td><b>Id</b></td><td><code>aws.resourceexplorer2.default_view_associations</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>ViewArn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>AssociatedAwsPrincipal</code></td><td><code>string</code></td><td>The AWS principal that the default view is associated with, used as the unique identifier for this resource.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.resourceexplorer2.default_view_associations
WHERE region = 'us-east-1'
</pre>
