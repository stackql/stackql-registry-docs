---
title: query_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - query_definitions
  - logs
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>query_definitions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>query_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.logs.query_definitions</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td>A name for the saved query definition</td></tr><tr><td><code>QueryString</code></td><td><code>string</code></td><td>The query string to use for this definition</td></tr><tr><td><code>LogGroupNames</code></td><td><code>array</code></td><td>Optionally define specific log groups as part of your query definition</td></tr><tr><td><code>QueryDefinitionId</code></td><td><code>string</code></td><td>Unique identifier of a query definition</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.logs.query_definitions
WHERE region = 'us-east-1'
</pre>
