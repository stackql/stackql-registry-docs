---
title: in_app_template
hide_title: false
hide_table_of_contents: false
keywords:
  - in_app_template
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Gets or operates on an individual <code>in_app_template</code> resource, use <code>in_app_templates</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>in_app_template</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Pinpoint::InAppTemplate</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.pinpoint.in_app_template" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="content" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="custom_config" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="layout" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="template_description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="template_name" /></td><td><code>string</code></td><td></td></tr>
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
arn,
content,
custom_config,
layout,
tags,
template_description,
template_name
FROM aws.pinpoint.in_app_template
WHERE data__Identifier = '<TemplateName>';
```

## Permissions

To operate on the <code>in_app_template</code> resource, the following permissions are required:

### Delete
```json
mobiletargeting:DeleteInAppTemplate,
mobiletargeting:GetInAppTemplate
```

### Read
```json
mobiletargeting:GetInAppTemplate,
mobiletargeting:ListTemplates
```

### Update
```json
mobiletargeting:UpdateInAppTemplate,
mobiletargeting:GetInAppTemplate
```

