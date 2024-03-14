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
Gets an individual <code>form</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>form</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>form</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.amplifyuibuilder.form</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>app_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>cta</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>data_type</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>environment_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>fields</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>form_action_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>label_decorator</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>schema_version</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>sectional_elements</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>style</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
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
FROM awscc.amplifyuibuilder.form
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

