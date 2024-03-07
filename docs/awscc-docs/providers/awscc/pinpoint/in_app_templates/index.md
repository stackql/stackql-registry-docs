---
title: in_app_templates
hide_title: false
hide_table_of_contents: false
keywords:
  - in_app_templates
  - pinpoint
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>in_app_templates</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>in_app_templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>in_app_templates</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.pinpoint.in_app_templates</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>template_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>in_app_templates</code> resource, the following permissions are required:

### Create
```json
mobiletargeting:CreateInAppTemplate,
mobiletargeting:GetInAppTemplate,
mobiletargeting:TagResource
```

### List
```json
mobiletargeting:GetInAppTemplate,
mobiletargeting:ListTemplates
```


## Example
```sql
SELECT
region,
template_name
FROM awscc.pinpoint.in_app_templates
WHERE region = 'us-east-1'
```
