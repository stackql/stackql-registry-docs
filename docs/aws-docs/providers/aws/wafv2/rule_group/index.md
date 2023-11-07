---
title: rule_group
hide_title: false
hide_table_of_contents: false
keywords:
  - rule_group
  - wafv2
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>rule_group</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>rule_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.wafv2.rule_group</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Arn</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Capacity</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>Description</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Name</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Id</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Scope</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Rules</code></td><td><code>array</code></td><td>Collection of Rules.</td></tr>
<tr><td><code>VisibilityConfig</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>LabelNamespace</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>CustomResponseBodies</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>AvailableLabels</code></td><td><code>array</code></td><td>Collection of Available Labels.</td></tr>
<tr><td><code>ConsumedLabels</code></td><td><code>array</code></td><td>Collection of Consumed Labels.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.wafv2.rule_group
WHERE region = 'us-east-1' AND data__Identifier = '&lt;Name&gt;' AND data__Identifier = '&lt;Id&gt;' AND data__Identifier = '&lt;Scope&gt;'
</pre>
