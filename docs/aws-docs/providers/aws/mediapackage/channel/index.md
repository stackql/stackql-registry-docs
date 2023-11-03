---
title: channel
hide_title: false
hide_table_of_contents: false
keywords:
  - channel
  - mediapackage
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>channel</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>channel</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.mediapackage.channel</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) assigned to the Channel.</td></tr><tr><td><code>Id</code></td><td><code>string</code></td><td>The ID of the Channel.</td></tr><tr><td><code>Description</code></td><td><code>string</code></td><td>A short text description of the Channel.</td></tr><tr><td><code>HlsIngest</code></td><td><code>undefined</code></td><td>An HTTP Live Streaming (HLS) ingest resource configuration.</td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td>A collection of tags associated with a resource</td></tr><tr><td><code>EgressAccessLogs</code></td><td><code>undefined</code></td><td>The configuration parameters for egress access logging.</td></tr><tr><td><code>IngressAccessLogs</code></td><td><code>undefined</code></td><td>The configuration parameters for egress access logging.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.mediapackage.channel
WHERE region = 'us-east-1' AND data__Identifier = '{Id}'
</pre>
