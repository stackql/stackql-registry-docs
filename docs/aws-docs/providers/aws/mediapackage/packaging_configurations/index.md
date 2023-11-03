---
title: packaging_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - packaging_configurations
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
Retrieves a list of <code>packaging_configurations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>packaging_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.mediapackage.packaging_configurations</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td>The ID of the PackagingConfiguration.</td></tr><tr><td><code>PackagingGroupId</code></td><td><code>string</code></td><td>The ID of a PackagingGroup.</td></tr><tr><td><code>Arn</code></td><td><code>string</code></td><td>The ARN of the PackagingConfiguration.</td></tr><tr><td><code>CmafPackage</code></td><td><code>undefined</code></td><td>A CMAF packaging configuration.</td></tr><tr><td><code>DashPackage</code></td><td><code>undefined</code></td><td>A Dynamic Adaptive Streaming over HTTP (DASH) packaging configuration.</td></tr><tr><td><code>HlsPackage</code></td><td><code>undefined</code></td><td>An HTTP Live Streaming (HLS) packaging configuration.</td></tr><tr><td><code>MssPackage</code></td><td><code>undefined</code></td><td>A Microsoft Smooth Streaming (MSS) PackagingConfiguration.</td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td>A collection of tags associated with a resource</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.mediapackage.packaging_configurations
WHERE region = 'us-east-1'
</pre>
