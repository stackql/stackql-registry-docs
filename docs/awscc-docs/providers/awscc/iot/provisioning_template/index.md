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
Gets an individual <code>provisioning_template</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>provisioning_template</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>provisioning_template</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.iot.provisioning_template</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>template_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>template_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>enabled</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>provisioning_role_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>template_body</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>template_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>pre_provisioning_hook</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>provisioning_template</code> resource, the following permissions are required:

### Read
<pre>
iot:DescribeProvisioningTemplate,
iot:ListTagsForResource</pre>

### Update
<pre>
iam:GetRole,
iam:PassRole,
iot:UpdateProvisioningTemplate,
iot:CreateProvisioningTemplateVersion,
iot:ListProvisioningTemplateVersions,
iot:DeleteProvisioningTemplateVersion,
iot:DescribeProvisioningTemplate,
iot:TagResource,
iot:UntagResource,
iot:ListTagsForResource</pre>

### Delete
<pre>
iot:DeleteProvisioningTemplate,
iot:DescribeProvisioningTemplate</pre>


## Example
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
FROM awscc.iot.provisioning_template
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;TemplateName&gt;'
```
