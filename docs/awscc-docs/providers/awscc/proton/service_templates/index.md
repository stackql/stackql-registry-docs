---
title: service_templates
hide_title: false
hide_table_of_contents: false
keywords:
  - service_templates
  - proton
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>service_templates</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service_templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>service_templates</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.proton.service_templates</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>&lt;p&gt;The Amazon Resource Name (ARN) of the service template.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>service_templates</code> resource, the following permissions are required:

### Create
<pre>
proton:CreateServiceTemplate,
proton:TagResource,
kms:*,
proton:GetServiceTemplate</pre>

### List
<pre>
proton:ListServiceTemplates</pre>


## Example
```sql
SELECT
region,
arn
FROM awscc.proton.service_templates
WHERE region = 'us-east-1'
```
