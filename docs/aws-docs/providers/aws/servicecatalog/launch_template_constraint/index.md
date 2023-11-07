---
title: launch_template_constraint
hide_title: false
hide_table_of_contents: false
keywords:
  - launch_template_constraint
  - servicecatalog
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>launch_template_constraint</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>launch_template_constraint</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>launch_template_constraint</td></tr>
<tr><td><b>Id</b></td><td><code>aws.servicecatalog.launch_template_constraint</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>AcceptLanguage</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>PortfolioId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ProductId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Rules</code></td><td><code>string</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.servicecatalog.launch_template_constraint
WHERE region = 'us-east-1' AND data__Identifier = '&lt;Id&gt;'
</pre>
