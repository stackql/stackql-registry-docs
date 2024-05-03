---
title: component
hide_title: false
hide_table_of_contents: false
keywords:
  - component
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

Gets or operates on an individual <code>component</code> resource, use <code>components</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>component</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::AmplifyUIBuilder::Component Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.amplifyuibuilder.component" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="app_id" /></td><td><code>string</code></td><td></td></tr>
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
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="variants" /></td><td><code>array</code></td><td></td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
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
tags,
variants
FROM aws.amplifyuibuilder.component
WHERE data__Identifier = '<AppId>|<EnvironmentName>|<Id>';
```

## Permissions

To operate on the <code>component</code> resource, the following permissions are required:

### Read
```json
amplify:GetApp,
amplifyuibuilder:GetComponent
```

### Update
```json
amplify:GetApp,
amplifyuibuilder:GetComponent,
amplifyuibuilder:TagResource,
amplifyuibuilder:UntagResource,
amplifyuibuilder:UpdateComponent
```

### Delete
```json
amplify:GetApp,
amplifyuibuilder:DeleteComponent,
amplifyuibuilder:GetComponent,
amplifyuibuilder:UntagResource
```

