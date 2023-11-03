---
title: application_instance
hide_title: false
hide_table_of_contents: false
keywords:
  - application_instance
  - panorama
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>application_instance</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>application_instance</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.panorama.application_instance</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Name</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>Description</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>ManifestPayload</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>ManifestOverridesPayload</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>RuntimeRoleArn</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>DefaultRuntimeContextDevice</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>DefaultRuntimeContextDeviceName</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>ApplicationInstanceId</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>ApplicationInstanceIdToReplace</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>DeviceId</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>StatusFilter</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>Status</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>HealthStatus</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>StatusDescription</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>CreatedTime</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>LastUpdatedTime</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>Arn</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>Tags</code></td><td><code>undefined</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.panorama.application_instance
WHERE region = 'us-east-1' AND data__Identifier = '{ApplicationInstanceId}'
</pre>
