---
title: component_types_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - component_types_list_only
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Lists <code>component_types</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/component_types/"><code>component_types</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>component_types_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::IoTTwinMaker::ComponentType</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iottwinmaker.component_types_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="workspace_id" /></td><td><code>string</code></td><td>The ID of the workspace that contains the component type.</td></tr>
<tr><td><CopyableCode code="component_type_id" /></td><td><code>string</code></td><td>The ID of the component type.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the component type.</td></tr>
<tr><td><CopyableCode code="extends_from" /></td><td><code>array</code></td><td>Specifies the parent component type to extend.</td></tr>
<tr><td><CopyableCode code="functions" /></td><td><code>object</code></td><td>a Map of functions in the component type. Each function's key must be unique to this map.</td></tr>
<tr><td><CopyableCode code="is_singleton" /></td><td><code>boolean</code></td><td>A Boolean value that specifies whether an entity can have more than one component of this type.</td></tr>
<tr><td><CopyableCode code="property_definitions" /></td><td><code>object</code></td><td>An map of the property definitions in the component type. Each property definition's key must be unique to this map.</td></tr>
<tr><td><CopyableCode code="property_groups" /></td><td><code>object</code></td><td>An map of the property groups in the component type. Each property group's key must be unique to this map.</td></tr>
<tr><td><CopyableCode code="composite_component_types" /></td><td><code>object</code></td><td>An map of the composite component types in the component type. Each composite component type's key must be unique to this map.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The ARN of the component type.</td></tr>
<tr><td><CopyableCode code="creation_date_time" /></td><td><code>string</code></td><td>The date and time when the component type was created.</td></tr>
<tr><td><CopyableCode code="update_date_time" /></td><td><code>string</code></td><td>The last date and time when the component type was updated.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>object</code></td><td>The current status of the component type.</td></tr>
<tr><td><CopyableCode code="is_abstract" /></td><td><code>boolean</code></td><td>A Boolean value that specifies whether the component type is abstract.</td></tr>
<tr><td><CopyableCode code="is_schema_initialized" /></td><td><code>boolean</code></td><td>A Boolean value that specifies whether the component type has a schema initializer and that the schema initializer has run.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td>A map of key-value pairs to associate with a resource.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Lists all <code>component_types</code> in a region.
```sql
SELECT
region,
workspace_id,
component_type_id
FROM aws.iottwinmaker.component_types_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>component_types_list_only</code> resource, see <a href="/providers/aws/iottwinmaker/component_types/#permissions"><code>component_types</code></a>


