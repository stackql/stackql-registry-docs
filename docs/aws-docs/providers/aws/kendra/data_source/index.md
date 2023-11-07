---
title: data_source
hide_title: false
hide_table_of_contents: false
keywords:
  - data_source
  - kendra
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>data_source</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_source</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>data_source</td></tr>
<tr><td><b>Id</b></td><td><code>aws.kendra.data_source</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Id</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Arn</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Name</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>IndexId</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Type</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>DataSourceConfiguration</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Description</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Schedule</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>RoleArn</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Tags</code></td><td><code>undefined</code></td><td>Tags for labeling the data source</td></tr>
<tr><td><code>CustomDocumentEnrichmentConfiguration</code></td><td><code>undefined</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.kendra.data_source<br/>WHERE region = 'us-east-1'<br/>AND data__Identifier = '&lt;Id&gt;'<br/>AND data__Identifier = '&lt;IndexId&gt;'
</pre>
