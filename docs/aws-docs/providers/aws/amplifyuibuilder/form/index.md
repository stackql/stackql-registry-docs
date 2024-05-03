---
title: form
hide_title: false
hide_table_of_contents: false
keywords:
  - form
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

Gets or operates on an individual <code>form</code> resource, use <code>forms</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>form</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::AmplifyUIBuilder::Form Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.amplifyuibuilder.form" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="app_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="cta" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="data_type" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="environment_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="fields" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="form_action_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="label_decorator" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="schema_version" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="sectional_elements" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="style" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td></td></tr>
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
cta,
data_type,
environment_name,
fields,
form_action_type,
id,
label_decorator,
name,
schema_version,
sectional_elements,
style,
tags
FROM aws.amplifyuibuilder.form
WHERE data__Identifier = '<AppId>|<EnvironmentName>|<Id>';
```

## Permissions

To operate on the <code>form</code> resource, the following permissions are required:

### Read
```json
amplify:GetApp,
amplifyuibuilder:GetForm,
amplifyuibuilder:TagResource
```

### Update
```json
amplify:GetApp,
amplifyuibuilder:GetForm,
amplifyuibuilder:TagResource,
amplifyuibuilder:UntagResource,
amplifyuibuilder:UpdateForm
```

### Delete
```json
amplify:GetApp,
amplifyuibuilder:DeleteForm,
amplifyuibuilder:TagResource,
amplifyuibuilder:UntagResource
```

