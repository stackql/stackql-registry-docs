---
title: predefined_attribute
hide_title: false
hide_table_of_contents: false
keywords:
  - predefined_attribute
  - connect
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>predefined_attribute</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>predefined_attribute</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>predefined_attribute</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.connect.predefined_attribute</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>instance_arn</code></td><td><code>string</code></td><td>The identifier of the Amazon Connect instance.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the predefined attribute.</td></tr>
<tr><td><code>values</code></td><td><code>object</code></td><td>The values of a predefined attribute.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
instance_arn,
name,
values
FROM awscc.connect.predefined_attribute
WHERE data__Identifier = '<InstanceArn>|<Name>';
```

## Permissions

To operate on the <code>predefined_attribute</code> resource, the following permissions are required:

### Read
```json
connect:DescribePredefinedAttribute
```

### Delete
```json
connect:DeletePredefinedAttribute
```

### Update
```json
connect:UpdatePredefinedAttribute
```

