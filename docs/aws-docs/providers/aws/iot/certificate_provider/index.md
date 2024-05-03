---
title: certificate_provider
hide_title: false
hide_table_of_contents: false
keywords:
  - certificate_provider
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

Gets or operates on an individual <code>certificate_provider</code> resource, use <code>certificate_providers</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>certificate_provider</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Use the AWS::IoT::CertificateProvider resource to declare an AWS IoT Certificate Provider.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iot.certificate_provider" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="certificate_provider_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="lambda_function_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="account_default_for_operations" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
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
certificate_provider_name,
lambda_function_arn,
account_default_for_operations,
tags,
arn
FROM aws.iot.certificate_provider
WHERE data__Identifier = '<CertificateProviderName>';
```

## Permissions

To operate on the <code>certificate_provider</code> resource, the following permissions are required:

### Read
```json
iot:DescribeCertificateProvider,
iot:ListTagsForResource
```

### Update
```json
iot:UpdateCertificateProvider,
iot:DescribeCertificateProvider,
iot:TagResource,
iot:UntagResource,
iot:ListTagsForResource
```

### Delete
```json
iot:DeleteCertificateProvider,
iot:DescribeCertificateProvider
```
