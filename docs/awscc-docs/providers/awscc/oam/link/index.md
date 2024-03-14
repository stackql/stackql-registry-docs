---
title: link
hide_title: false
hide_table_of_contents: false
keywords:
  - link
  - oam
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>link</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>link</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>link</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.oam.link</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>label</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>label_template</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>resource_types</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>sink_identifier</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>object</code></td><td>Tags to apply to the link</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
arn,
label,
label_template,
resource_types,
sink_identifier,
tags
FROM awscc.oam.link
WHERE data__Identifier = '<Arn>';
```

## Permissions

To operate on the <code>link</code> resource, the following permissions are required:

### Read
```json
oam:GetLink
```

### Update
```json
oam:GetLink,
oam:UpdateLink,
cloudwatch:Link,
logs:Link,
xray:Link,
applicationinsights:Link,
oam:TagResource,
oam:UntagResource
```

### Delete
```json
oam:DeleteLink,
oam:GetLink
```

