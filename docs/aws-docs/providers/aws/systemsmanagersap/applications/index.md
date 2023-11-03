---
title: applications
hide_title: false
hide_table_of_contents: false
keywords:
  - applications
  - systemsmanagersap
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>applications</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>applications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.systemsmanagersap.applications</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>ApplicationId</code></td><td><code>string</code></td><td></td></tr><tr><td><code>ApplicationType</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Arn</code></td><td><code>string</code></td><td>The ARN of the Helix application</td></tr><tr><td><code>Credentials</code></td><td><code>array</code></td><td></td></tr><tr><td><code>Instances</code></td><td><code>array</code></td><td></td></tr><tr><td><code>SapInstanceNumber</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Sid</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td>The tags of a SystemsManagerSAP application.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.systemsmanagersap.applications
WHERE region = 'us-east-1'
</pre>
