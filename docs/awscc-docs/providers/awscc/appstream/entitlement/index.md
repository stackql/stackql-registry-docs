---
title: entitlement
hide_title: false
hide_table_of_contents: false
keywords:
  - entitlement
  - appstream
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>entitlement</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>entitlement</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>entitlement</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.appstream.entitlement</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>stack_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>app_visibility</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>attributes</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>created_time</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>last_modified_time</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>entitlement</code> resource, the following permissions are required:

### Read
```json
appstream:DescribeEntitlements
```

### Update
```json
appstream:UpdateEntitlement
```

### Delete
```json
appstream:DeleteEntitlement
```


## Example
```sql
SELECT
region,
name,
stack_name,
description,
app_visibility,
attributes,
created_time,
last_modified_time
FROM awscc.appstream.entitlement
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;StackName&gt;'
AND data__Identifier = '&lt;Name&gt;'
```
