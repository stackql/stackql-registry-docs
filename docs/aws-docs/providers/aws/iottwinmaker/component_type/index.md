---
title: component_type
hide_title: false
hide_table_of_contents: false
keywords:
  - component_type
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
Gets an individual <code>component_type</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>component_type</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.iottwinmaker.component_type</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>WorkspaceId</code></td><td><code>string</code></td><td>The ID of the workspace that contains the component type.</td></tr>
<tr><td><code>ComponentTypeId</code></td><td><code>string</code></td><td>The ID of the component type.</td></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td>The description of the component type.</td></tr>
<tr><td><code>ExtendsFrom</code></td><td><code>array</code></td><td>Specifies the parent component type to extend.</td></tr>
<tr><td><code>Functions</code></td><td><code>object</code></td><td>a Map of functions in the component type. Each function's key must be unique to this map.</td></tr>
<tr><td><code>IsSingleton</code></td><td><code>boolean</code></td><td>A Boolean value that specifies whether an entity can have more than one component of this type.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;</td></tr>
<tr><td><code>PropertyDefinitions</code></td><td><code>object</code></td><td>An map of the property definitions in the component type. Each property definition's key must be unique to this map.</td></tr>
<tr><td><code>PropertyGroups</code></td><td><code>object</code></td><td>An map of the property groups in the component type. Each property group's key must be unique to this map.</td></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td>The ARN of the component type.</td></tr>
<tr><td><code>CreationDateTime</code></td><td><code>undefined</code></td><td>The date and time when the component type was created.</td></tr>
<tr><td><code>UpdateDateTime</code></td><td><code>undefined</code></td><td>The last date and time when the component type was updated.</td></tr>
<tr><td><code>Status</code></td><td><code>undefined</code></td><td>The current status of the component type.</td></tr>
<tr><td><code>IsAbstract</code></td><td><code>boolean</code></td><td>A Boolean value that specifies whether the component type is abstract.</td></tr>
<tr><td><code>IsSchemaInitialized</code></td><td><code>boolean</code></td><td>A Boolean value that specifies whether the component type has a schema initializer and that the schema initializer has run.</td></tr>
<tr><td><code>Tags</code></td><td><code>object</code></td><td>A map of key-value pairs to associate with a resource.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.iottwinmaker.component_type
WHERE region = 'us-east-1' AND data__Identifier = '&lt;WorkspaceId&gt;' AND data__Identifier = '&lt;ComponentTypeId&gt;'
</pre>
