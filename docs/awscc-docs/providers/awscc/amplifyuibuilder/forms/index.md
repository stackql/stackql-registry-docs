---
title: forms
hide_title: false
hide_table_of_contents: false
keywords:
  - forms
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
Retrieves a list of <code>forms</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>forms</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>forms</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.amplifyuibuilder.forms</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>app_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>environment_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>forms</code> resource, the following permissions are required:

### Create
<pre>
amplify:GetApp,
amplifyuibuilder:CreateForm,
amplifyuibuilder:GetForm,
amplifyuibuilder:TagResource,
amplifyuibuilder:UntagResource</pre>

### List
<pre>
amplify:GetApp,
amplifyuibuilder:ListForms</pre>


## Example
```sql
SELECT
region,
app_id,
environment_name,
id
FROM awscc.amplifyuibuilder.forms
WHERE region = 'us-east-1'
```
