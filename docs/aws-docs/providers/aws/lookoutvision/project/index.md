---
title: project
hide_title: false
hide_table_of_contents: false
keywords:
  - project
  - lookoutvision
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>project</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>project</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>project</td></tr>
<tr><td><b>Id</b></td><td><code>aws.lookoutvision.project</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ProjectName</code></td><td><code>string</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.lookoutvision.project<br/>WHERE region = 'us-east-1'<br/>AND data__Identifier = '&lt;ProjectName&gt;'
</pre>
