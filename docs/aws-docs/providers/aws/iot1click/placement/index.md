---
title: placement
hide_title: false
hide_table_of_contents: false
keywords:
  - placement
  - iot1click
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>placement</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>placement</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>placement</td></tr>
<tr><td><b>Id</b></td><td><code>aws.iot1click.placement</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>PlacementName</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ProjectName</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>AssociatedDevices</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>Attributes</code></td><td><code>object</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.iot1click.placement
WHERE region = 'us-east-1' AND data__Identifier = '&lt;Id&gt;'
</pre>
