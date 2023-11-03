---
title: workspaces
hide_title: false
hide_table_of_contents: false
keywords:
  - workspaces
  - iottwinmaker
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>workspaces</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workspaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.iottwinmaker.workspaces</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>WorkspaceId</code></td><td><code>string</code></td><td>The ID of the workspace.</td></tr><tr><td><code>Arn</code></td><td><code>string</code></td><td>The ARN of the workspace.</td></tr><tr><td><code>Description</code></td><td><code>string</code></td><td>The description of the workspace.</td></tr><tr><td><code>Role</code></td><td><code>string</code></td><td>The ARN of the execution role associated with the workspace.</td></tr><tr><td><code>S3Location</code></td><td><code>string</code></td><td>The ARN of the S3 bucket where resources associated with the workspace are stored.</td></tr><tr><td><code>CreationDateTime</code></td><td><code>undefined</code></td><td>The date and time when the workspace was created.</td></tr><tr><td><code>UpdateDateTime</code></td><td><code>undefined</code></td><td>The date and time of the current update.</td></tr><tr><td><code>Tags</code></td><td><code>object</code></td><td>A map of key-value pairs to associate with a resource.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.iottwinmaker.workspaces
WHERE region = 'us-east-1'
</pre>
