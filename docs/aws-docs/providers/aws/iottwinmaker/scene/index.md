---
title: scene
hide_title: false
hide_table_of_contents: false
keywords:
  - scene
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
Gets an individual <code>scene</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>scene</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.iottwinmaker.scene</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>SceneId</code></td><td><code>string</code></td><td>The ID of the scene.</td></tr><tr><td><code>Arn</code></td><td><code>string</code></td><td>The ARN of the scene.</td></tr><tr><td><code>Description</code></td><td><code>string</code></td><td>The description of the scene.</td></tr><tr><td><code>ContentLocation</code></td><td><code>string</code></td><td>The relative path that specifies the location of the content definition file.</td></tr><tr><td><code>CreationDateTime</code></td><td><code>undefined</code></td><td>The date and time when the scene was created.</td></tr><tr><td><code>UpdateDateTime</code></td><td><code>undefined</code></td><td>The date and time of the current update.</td></tr><tr><td><code>Tags</code></td><td><code>object</code></td><td>A key-value pair to associate with a resource.</td></tr><tr><td><code>WorkspaceId</code></td><td><code>string</code></td><td>The ID of the scene.</td></tr><tr><td><code>Capabilities</code></td><td><code>array</code></td><td>A list of capabilities that the scene uses to render.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.iottwinmaker.scene
WHERE region = 'us-east-1' AND data__Identifier = '{WorkspaceId}' AND data__Identifier = '{SceneId}'
</pre>
