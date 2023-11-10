---
title: packaging_configuration
hide_title: false
hide_table_of_contents: false
keywords:
  - packaging_configuration
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
Gets an individual <code>packaging_configuration</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>packaging_configuration</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>packaging_configuration</td></tr>
<tr><td><b>Id</b></td><td><code>aws.mediapackage.packaging_configuration</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>The ID of the PackagingConfiguration.</td></tr>
<tr><td><code>packaging_group_id</code></td><td><code>string</code></td><td>The ID of a PackagingGroup.</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The ARN of the PackagingConfiguration.</td></tr>
<tr><td><code>cmaf_package</code></td><td><code>object</code></td><td>A CMAF packaging configuration.</td></tr>
<tr><td><code>dash_package</code></td><td><code>object</code></td><td>A Dynamic Adaptive Streaming over HTTP (DASH) packaging configuration.</td></tr>
<tr><td><code>hls_package</code></td><td><code>object</code></td><td>An HTTP Live Streaming (HLS) packaging configuration.</td></tr>
<tr><td><code>mss_package</code></td><td><code>object</code></td><td>A Microsoft Smooth Streaming (MSS) PackagingConfiguration.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>A collection of tags associated with a resource</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
id,
packaging_group_id,
arn,
cmaf_package,
dash_package,
hls_package,
mss_package,
tags
FROM aws.mediapackage.packaging_configuration
WHERE region = 'us-east-1'
AND data__Identifier = '<Id>'
```
