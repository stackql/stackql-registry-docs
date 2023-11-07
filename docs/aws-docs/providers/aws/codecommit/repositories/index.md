---
title: repositories
hide_title: false
hide_table_of_contents: false
keywords:
  - repositories
  - codecommit
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>repositories</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>repositories</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.codecommit.repositories</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>CloneUrlHttp</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>CloneUrlSsh</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>RepositoryName</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Triggers</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Code</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>RepositoryDescription</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.codecommit.repositories
WHERE region = 'us-east-1'
</pre>
