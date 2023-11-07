---
title: trigger
hide_title: false
hide_table_of_contents: false
keywords:
  - trigger
  - glue
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>trigger</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>trigger</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>trigger</td></tr>
<tr><td><b>Id</b></td><td><code>aws.glue.trigger</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>StartOnCreation</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Actions</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>EventBatchingCondition</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>WorkflowName</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Schedule</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Tags</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Predicate</code></td><td><code>object</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.glue.trigger<br/>WHERE region = 'us-east-1'<br/>AND data__Identifier = '&lt;Id&gt;'
</pre>
