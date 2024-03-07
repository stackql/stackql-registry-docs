---
title: environment_template
hide_title: false
hide_table_of_contents: false
keywords:
  - environment_template
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
Gets an individual <code>environment_template</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>environment_template</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>environment_template</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.proton.environment_template</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>&lt;p&gt;The Amazon Resource Name (ARN) of the environment template.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>&lt;p&gt;A description of the environment template.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>display_name</code></td><td><code>string</code></td><td>&lt;p&gt;The environment template name as displayed in the developer interface.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>encryption_key</code></td><td><code>string</code></td><td>&lt;p&gt;A customer provided encryption key that Proton uses to encrypt data.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>provisioning</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>&lt;p&gt;An optional list of metadata items that you can associate with the Proton environment template. A tag is a key-value pair.&lt;&#x2F;p&gt;&lt;br&#x2F;&gt;         &lt;p&gt;For more information, see &lt;a href="https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;proton&#x2F;latest&#x2F;userguide&#x2F;resources.html"&gt;Proton resources and tagging&lt;&#x2F;a&gt; in the&lt;br&#x2F;&gt;        &lt;i&gt;Proton User Guide&lt;&#x2F;i&gt;.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
arn,
description,
display_name,
encryption_key,
name,
provisioning,
tags
FROM awscc.proton.environment_template
WHERE region = 'us-east-1'
AND data__Identifier = '{Arn}';
```

## Permissions

To operate on the <code>environment_template</code> resource, the following permissions are required:

### Read
```json
proton:GetEnvironmentTemplate,
proton:ListTagsForResource,
kms:*
```

### Update
```json
proton:CreateEnvironmentTemplate,
proton:ListTagsForResource,
proton:TagResource,
proton:UntagResource,
proton:UpdateEnvironmentTemplate,
proton:GetEnvironmentTemplate,
kms:*
```

### Delete
```json
proton:DeleteEnvironmentTemplate,
proton:GetEnvironmentTemplate,
kms:*
```

