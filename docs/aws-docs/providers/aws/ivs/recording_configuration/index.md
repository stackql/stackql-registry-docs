---
title: recording_configuration
hide_title: false
hide_table_of_contents: false
keywords:
  - recording_configuration
  - ivs
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>recording_configuration</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>recording_configuration</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>recording_configuration</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ivs.recording_configuration</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td>Recording Configuration ARN is automatically generated on creation and assigned as the unique identifier.</td></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td>Recording Configuration Name.</td></tr>
<tr><td><code>State</code></td><td><code>string</code></td><td>Recording Configuration State.</td></tr>
<tr><td><code>RecordingReconnectWindowSeconds</code></td><td><code>integer</code></td><td>Recording Reconnect Window Seconds. (0 means disabled)</td></tr>
<tr><td><code>DestinationConfiguration</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td>A list of key-value pairs that contain metadata for the asset model.</td></tr>
<tr><td><code>ThumbnailConfiguration</code></td><td><code>undefined</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.ivs.recording_configuration
WHERE region = 'us-east-1' AND data__Identifier = '&lt;Arn&gt;'
</pre>
