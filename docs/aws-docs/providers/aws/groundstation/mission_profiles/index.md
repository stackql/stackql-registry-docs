---
title: mission_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - mission_profiles
  - groundstation
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>mission_profiles</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>mission_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.groundstation.mission_profiles</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td>A name used to identify a mission profile.</td></tr><tr><td><code>ContactPrePassDurationSeconds</code></td><td><code>integer</code></td><td>Pre-pass time needed before the contact.</td></tr><tr><td><code>ContactPostPassDurationSeconds</code></td><td><code>integer</code></td><td>Post-pass time needed after the contact.</td></tr><tr><td><code>MinimumViableContactDurationSeconds</code></td><td><code>integer</code></td><td>Visibilities with shorter duration than the specified minimum viable contact duration will be ignored when searching for available contacts.</td></tr><tr><td><code>StreamsKmsKey</code></td><td><code>undefined</code></td><td>The ARN of a KMS Key used for encrypting data during transmission from the source to destination locations.</td></tr><tr><td><code>StreamsKmsRole</code></td><td><code>string</code></td><td>The ARN of the KMS Key or Alias Key role used to define permissions on KMS Key usage.</td></tr><tr><td><code>DataflowEdges</code></td><td><code>array</code></td><td></td></tr><tr><td><code>TrackingConfigArn</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr><tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Arn</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Region</code></td><td><code>string</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.groundstation.mission_profiles
WHERE region = 'us-east-1'
</pre>
