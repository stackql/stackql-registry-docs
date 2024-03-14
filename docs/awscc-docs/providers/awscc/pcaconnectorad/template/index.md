---
title: template
hide_title: false
hide_table_of_contents: false
keywords:
  - template
  - pcaconnectorad
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>template</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>template</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>template</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.pcaconnectorad.template</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>connector_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>definition</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>reenroll_all_certificate_holders</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>template_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
connector_arn,
definition,
name,
reenroll_all_certificate_holders,
tags,
template_arn
FROM awscc.pcaconnectorad.template
WHERE data__Identifier = '<TemplateArn>';
```

## Permissions

To operate on the <code>template</code> resource, the following permissions are required:

### Read
```json
pca-connector-ad:GetTemplate,
pca-connector-ad:ListTagsForResource
```

### Update
```json
pca-connector-ad:ListTagsForResource,
pca-connector-ad:TagResource,
pca-connector-ad:UntagResource,
pca-connector-ad:UpdateTemplate
```

### Delete
```json
pca-connector-ad:GetTemplate,
pca-connector-ad:DeleteTemplate
```

