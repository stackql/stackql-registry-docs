---
title: service_template
hide_title: false
hide_table_of_contents: false
keywords:
  - service_template
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Gets or operates on an individual <code>service_template</code> resource, use <code>service_templates</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service_template</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Proton::ServiceTemplate Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.proton.service_template" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>&lt;p&gt;The Amazon Resource Name (ARN) of the service template.&lt;&#x2F;p&gt;</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>&lt;p&gt;A description of the service template.&lt;&#x2F;p&gt;</td></tr>
<tr><td><CopyableCode code="display_name" /></td><td><code>string</code></td><td>&lt;p&gt;The name of the service template as displayed in the developer interface.&lt;&#x2F;p&gt;</td></tr>
<tr><td><CopyableCode code="encryption_key" /></td><td><code>string</code></td><td>&lt;p&gt;A customer provided encryption key that's used to encrypt data.&lt;&#x2F;p&gt;</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="pipeline_provisioning" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>&lt;p&gt;An optional list of metadata items that you can associate with the Proton service template. A tag is a key-value pair.&lt;&#x2F;p&gt;&lt;br&#x2F;&gt;         &lt;p&gt;For more information, see &lt;a href="https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;proton&#x2F;latest&#x2F;userguide&#x2F;resources.html"&gt;Proton resources and tagging&lt;&#x2F;a&gt; in the&lt;br&#x2F;&gt;        &lt;i&gt;Proton User Guide&lt;&#x2F;i&gt;.&lt;&#x2F;p&gt;</td></tr>
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
description,
display_name,
encryption_key,
name,
pipeline_provisioning,
tags
FROM aws.proton.service_template
WHERE data__Identifier = '<Arn>';
```

## Permissions

To operate on the <code>service_template</code> resource, the following permissions are required:

### Read
```json
proton:GetServiceTemplate,
proton:ListTagsForResource,
kms:*
```

### Update
```json
proton:GetServiceTemplate,
proton:CreateServiceTemplate,
proton:ListTagsForResource,
proton:TagResource,
proton:UntagResource,
proton:UpdateServiceTemplate,
kms:*
```

### Delete
```json
proton:DeleteServiceTemplate,
proton:UntagResource,
kms:*,
proton:GetServiceTemplate
```

