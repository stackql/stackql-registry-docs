---
title: provisioning_template
hide_title: false
hide_table_of_contents: false
keywords:
  - provisioning_template
  - iot
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

Gets or operates on an individual <code>provisioning_template</code> resource, use <code>provisioning_templates</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>provisioning_template</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Creates a fleet provisioning template.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iot.provisioning_template" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="template_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="template_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="enabled" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="provisioning_role_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="template_body" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="template_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="pre_provisioning_hook" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
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
template_arn,
template_name,
description,
enabled,
provisioning_role_arn,
template_body,
template_type,
pre_provisioning_hook,
tags
FROM aws.iot.provisioning_template
WHERE data__Identifier = '<TemplateName>';
```

## Permissions

To operate on the <code>provisioning_template</code> resource, the following permissions are required:

### Read
```json
iot:DescribeProvisioningTemplate,
iot:ListTagsForResource
```

### Update
```json
iam:GetRole,
iam:PassRole,
iot:UpdateProvisioningTemplate,
iot:CreateProvisioningTemplateVersion,
iot:ListProvisioningTemplateVersions,
iot:DeleteProvisioningTemplateVersion,
iot:DescribeProvisioningTemplate,
iot:TagResource,
iot:UntagResource,
iot:ListTagsForResource
```

### Delete
```json
iot:DeleteProvisioningTemplate,
iot:DescribeProvisioningTemplate
```

