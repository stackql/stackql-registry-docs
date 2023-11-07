---
title: entity
hide_title: false
hide_table_of_contents: false
keywords:
  - entity
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
Gets an individual <code>entity</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>entity</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.iottwinmaker.entity</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>EntityId</code></td><td><code>string</code></td><td>The ID of the entity.</td></tr>
<tr><td><code>EntityName</code></td><td><code>string</code></td><td>The name of the entity.</td></tr>
<tr><td><code>Status</code></td><td><code>undefined</code></td><td>The current status of the entity.</td></tr>
<tr><td><code>HasChildEntities</code></td><td><code>boolean</code></td><td>A Boolean value that specifies whether the entity has child entities or not.</td></tr>
<tr><td><code>ParentEntityId</code></td><td><code>string</code></td><td>The ID of the parent entity.</td></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td>The ARN of the entity.</td></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td>The description of the entity.</td></tr>
<tr><td><code>CreationDateTime</code></td><td><code>undefined</code></td><td>The date and time when the entity was created.</td></tr>
<tr><td><code>UpdateDateTime</code></td><td><code>undefined</code></td><td>The last date and time when the entity was updated.</td></tr>
<tr><td><code>Tags</code></td><td><code>object</code></td><td>A key-value pair to associate with a resource.</td></tr>
<tr><td><code>WorkspaceId</code></td><td><code>string</code></td><td>The ID of the workspace.</td></tr>
<tr><td><code>Components</code></td><td><code>object</code></td><td>A map that sets information about a component type.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.iottwinmaker.entity
WHERE region = 'us-east-1' AND data__Identifier = '&lt;WorkspaceId&gt;' AND data__Identifier = '&lt;EntityId&gt;'
</pre>
