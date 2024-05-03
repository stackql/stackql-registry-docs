---
title: certificates
hide_title: false
hide_table_of_contents: false
keywords:
  - certificates
  - acmpca
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

Used to retrieve a list of <code>certificates</code> in a region or create a <code>certificates</code> resource, use <code>certificate</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>certificates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The ``AWS::ACMPCA::Certificate`` resource is used to issue a certificate using your private certificate authority. For more information, see the &#91;IssueCertificate&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;privateca&#x2F;latest&#x2F;APIReference&#x2F;API_IssueCertificate.html) action.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.acmpca.certificates" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="certificate_authority_arn" /></td><td><code>undefined</code></td><td>The Amazon Resource Name (ARN) for the private CA issues the certificate.</td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
arn,
certificate_authority_arn
FROM aws.acmpca.certificates
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>certificates</code> resource, the following permissions are required:

### Create
```json
acm-pca:IssueCertificate,
acm-pca:GetCertificate
```

