---
title: extension
hide_title: false
hide_table_of_contents: false
keywords:
  - extension
  - appconfig
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>extension</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>extension</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>extension</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.appconfig.extension</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>version_number</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>Name of the extension.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>Description of the extension.</td></tr>
<tr><td><code>actions</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>parameters</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>latest_version_number</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value tags to apply to this resource.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>extension</code> resource, the following permissions are required:

### Read
```json
appconfig:GetExtension
```

### Update
```json
appconfig:UpdateExtension,
appconfig:TagResource,
appconfig:UntagResource
```

### Delete
```json
appconfig:DeleteExtension,
appconfig:UntagResource
```


## Example
```sql
SELECT
region,
id,
arn,
version_number,
name,
description,
actions,
parameters,
latest_version_number,
tags
FROM awscc.appconfig.extension
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```
