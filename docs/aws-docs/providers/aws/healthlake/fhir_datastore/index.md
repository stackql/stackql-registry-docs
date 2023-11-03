---
title: fhir_datastore
hide_title: false
hide_table_of_contents: false
keywords:
  - fhir_datastore
  - healthlake
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>fhir_datastore</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>fhir_datastore</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.healthlake.fhir_datastore</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>CreatedAt</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>DatastoreArn</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>DatastoreEndpoint</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>DatastoreId</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>DatastoreName</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>DatastoreStatus</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>DatastoreTypeVersion</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>PreloadDataConfig</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>SseConfiguration</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.healthlake.fhir_datastore
WHERE region = 'us-east-1' AND data__Identifier = '{DatastoreId}'
</pre>
