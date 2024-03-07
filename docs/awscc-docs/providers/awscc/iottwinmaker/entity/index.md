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
<tr><td><b>Description</b></td><td>entity</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.iottwinmaker.entity</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>entity_id</code></td><td><code>string</code></td><td>The ID of the entity.</td></tr>
<tr><td><code>entity_name</code></td><td><code>string</code></td><td>The name of the entity.</td></tr>
<tr><td><code>status</code></td><td><code>object</code></td><td>The current status of the entity.</td></tr>
<tr><td><code>has_child_entities</code></td><td><code>boolean</code></td><td>A Boolean value that specifies whether the entity has child entities or not.</td></tr>
<tr><td><code>parent_entity_id</code></td><td><code>string</code></td><td>The ID of the parent entity.</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The ARN of the entity.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>The description of the entity.</td></tr>
<tr><td><code>creation_date_time</code></td><td><code>string</code></td><td>The date and time when the entity was created.</td></tr>
<tr><td><code>update_date_time</code></td><td><code>string</code></td><td>The last date and time when the entity was updated.</td></tr>
<tr><td><code>tags</code></td><td><code>object</code></td><td>A key-value pair to associate with a resource.</td></tr>
<tr><td><code>workspace_id</code></td><td><code>string</code></td><td>The ID of the workspace.</td></tr>
<tr><td><code>components</code></td><td><code>object</code></td><td>A map that sets information about a component type.</td></tr>
<tr><td><code>composite_components</code></td><td><code>object</code></td><td>A map that sets information about a composite component.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>entity</code> resource, the following permissions are required:

### Read
<pre>
iottwinmaker:GetComponentType,
iottwinmaker:GetEntity,
iottwinmaker:ListComponents,
iottwinmaker:ListProperties,
iottwinmaker:GetWorkspace,
iottwinmaker:ListEntities,
iottwinmaker:ListTagsForResource</pre>

### Update
<pre>
iottwinmaker:GetComponentType,
iottwinmaker:GetEntity,
iottwinmaker:ListComponents,
iottwinmaker:ListProperties,
iottwinmaker:GetWorkspace,
iottwinmaker:ListTagsForResource,
iottwinmaker:TagResource,
iottwinmaker:UntagResource,
iottwinmaker:UpdateEntity,
iottwinmaker:UpdateComponentType</pre>

### Delete
<pre>
iottwinmaker:GetEntity,
iottwinmaker:GetWorkspace,
iottwinmaker:DeleteEntity</pre>


## Example
```sql
SELECT
region,
entity_id,
entity_name,
status,
has_child_entities,
parent_entity_id,
arn,
description,
creation_date_time,
update_date_time,
tags,
workspace_id,
components,
composite_components
FROM awscc.iottwinmaker.entity
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;WorkspaceId&gt;'
AND data__Identifier = '&lt;EntityId&gt;'
```
