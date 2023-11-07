---
title: crawler
hide_title: false
hide_table_of_contents: false
keywords:
  - crawler
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
Gets an individual <code>crawler</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>crawler</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>crawler</td></tr>
<tr><td><b>Id</b></td><td><code>aws.glue.crawler</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Classifiers</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>SchemaChangePolicy</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>Configuration</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>RecrawlPolicy</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>DatabaseName</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Targets</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>CrawlerSecurityConfiguration</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Role</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Schedule</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>TablePrefix</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Tags</code></td><td><code>object</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.glue.crawler<br/>WHERE region = 'us-east-1'<br/>AND data__Identifier = '&lt;Id&gt;'
</pre>
