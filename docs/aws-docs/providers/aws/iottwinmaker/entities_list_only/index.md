---
title: entities_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - entities_list_only
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

Lists <code>entities</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/entities/"><code>entities</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>entities_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::IoTTwinMaker::Entity</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iottwinmaker.entities_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="entity_id" /></td><td><code>string</code></td><td>The ID of the entity.</td></tr>
<tr><td><CopyableCode code="entity_name" /></td><td><code>string</code></td><td>The name of the entity.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>object</code></td><td>The current status of the entity.</td></tr>
<tr><td><CopyableCode code="has_child_entities" /></td><td><code>boolean</code></td><td>A Boolean value that specifies whether the entity has child entities or not.</td></tr>
<tr><td><CopyableCode code="parent_entity_id" /></td><td><code>string</code></td><td>The ID of the parent entity.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The ARN of the entity.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the entity.</td></tr>
<tr><td><CopyableCode code="creation_date_time" /></td><td><code>string</code></td><td>The date and time when the entity was created.</td></tr>
<tr><td><CopyableCode code="update_date_time" /></td><td><code>string</code></td><td>The last date and time when the entity was updated.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td>A key-value pair to associate with a resource.</td></tr>
<tr><td><CopyableCode code="workspace_id" /></td><td><code>string</code></td><td>The ID of the workspace.</td></tr>
<tr><td><CopyableCode code="components" /></td><td><code>object</code></td><td>A map that sets information about a component type.</td></tr>
<tr><td><CopyableCode code="composite_components" /></td><td><code>object</code></td><td>A map that sets information about a composite component.</td></tr>
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
Lists all <code>entities</code> in a region.
```sql
SELECT
region,
workspace_id,
entity_id
FROM aws.iottwinmaker.entities_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>entities_list_only</code> resource, see <a href="/providers/aws/iottwinmaker/entities/#permissions"><code>entities</code></a>


