---
title: saml_provider
hide_title: false
hide_table_of_contents: false
keywords:
  - saml_provider
  - iam
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>saml_provider</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>saml_provider</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>saml_provider</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.iam.saml_provider</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>saml_metadata_document</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>Amazon Resource Name (ARN) of the SAML provider</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>saml_provider</code> resource, the following permissions are required:

### Read
<pre>
iam:GetSAMLProvider</pre>

### Update
<pre>
iam:UpdateSAMLProvider,
iam:GetSAMLProvider,
iam:TagSAMLProvider,
iam:ListSAMLProviderTags,
iam:UntagSAMLProvider</pre>

### Delete
<pre>
iam:DeleteSAMLProvider</pre>


## Example
```sql
SELECT
region,
name,
saml_metadata_document,
arn,
tags
FROM awscc.iam.saml_provider
WHERE data__Identifier = '&lt;Arn&gt;'
```
