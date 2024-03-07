---
title: saml_providers
hide_title: false
hide_table_of_contents: false
keywords:
  - saml_providers
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
Retrieves a list of <code>saml_providers</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>saml_providers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>saml_providers</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.iam.saml_providers</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>Amazon Resource Name (ARN) of the SAML provider</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>saml_providers</code> resource, the following permissions are required:

### Create
```json
iam:CreateSAMLProvider,
iam:GetSAMLProvider,
iam:TagSAMLProvider
```

### List
```json
iam:ListSAMLProviders,
iam:GetSAMLProvider
```


## Example
```sql
SELECT
region,
arn
FROM awscc.iam.saml_providers

```
