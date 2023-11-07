---
title: containers
hide_title: false
hide_table_of_contents: false
keywords:
  - containers
  - mediastore
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>containers</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>containers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.mediastore.containers</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Policy</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>MetricPolicy</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Endpoint</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ContainerName</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>CorsPolicy</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>LifecyclePolicy</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>AccessLoggingEnabled</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.mediastore.containers
WHERE region = 'us-east-1'
</pre>
