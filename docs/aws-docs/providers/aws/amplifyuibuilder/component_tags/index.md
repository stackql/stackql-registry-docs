---
title: component_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - component_tags
  - amplifyuibuilder
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

Expands all tag keys and values for <code>components</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>component_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::AmplifyUIBuilder::Component Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.amplifyuibuilder.component_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="app_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="binding_properties" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="children" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="collection_properties" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="component_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="environment_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="events" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="modified_at" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="overrides" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="properties" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="schema_version" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="source_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="variants" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="tag_key" /></td><td><code>string</code></td><td>Tag key.</td></tr>
<tr><td><CopyableCode code="tag_value" /></td><td><code>string</code></td><td>Tag value.</td></tr>
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
Expands tags for all <code>components</code> in a region.
```sql
SELECT
region,
app_id,
binding_properties,
children,
collection_properties,
component_type,
created_at,
environment_name,
events,
id,
modified_at,
name,
overrides,
properties,
schema_version,
source_id,
variants,
tag_key,
tag_value
FROM aws.amplifyuibuilder.component_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>component_tags</code> resource, see <a href="/providers/aws/amplifyuibuilder/components/#permissions"><code>components</code></a>

