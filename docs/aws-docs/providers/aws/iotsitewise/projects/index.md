---
title: projects
hide_title: false
hide_table_of_contents: false
keywords:
  - projects
  - iotsitewise
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>projects</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>projects</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.iotsitewise.projects</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>PortalId</code></td><td><code>string</code></td><td>The ID of the portal in which to create the project.</td></tr><tr><td><code>ProjectId</code></td><td><code>string</code></td><td>The ID of the project.</td></tr><tr><td><code>ProjectName</code></td><td><code>string</code></td><td>A friendly name for the project.</td></tr><tr><td><code>ProjectDescription</code></td><td><code>string</code></td><td>A description for the project.</td></tr><tr><td><code>ProjectArn</code></td><td><code>string</code></td><td>The ARN of the project.</td></tr><tr><td><code>AssetIds</code></td><td><code>array</code></td><td>The IDs of the assets to be associated to the project.</td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td>A list of key-value pairs that contain metadata for the project.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.iotsitewise.projects
WHERE region = 'us-east-1'
</pre>
