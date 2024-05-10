---
title: certificate_authority_activation
hide_title: false
hide_table_of_contents: false
keywords:
  - certificate_authority_activation
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Gets or updates an individual <code>certificate_authority_activation</code> resource, use <code>certificate_authority_activations</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>certificate_authority_activation</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Used to install the certificate authority certificate and update the certificate authority status.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.acmpca.certificate_authority_activation" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="certificate_authority_arn" /></td><td><code>string</code></td><td>Arn of the Certificate Authority.</td></tr>
<tr><td><CopyableCode code="certificate" /></td><td><code>string</code></td><td>Certificate Authority certificate that will be installed in the Certificate Authority.</td></tr>
<tr><td><CopyableCode code="certificate_chain" /></td><td><code>string</code></td><td>Certificate chain for the Certificate Authority certificate.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>The status of the Certificate Authority.</td></tr>
<tr><td><CopyableCode code="complete_certificate_chain" /></td><td><code>string</code></td><td>The complete certificate chain, including the Certificate Authority certificate.</td></tr>
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
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
certificate_authority_arn,
certificate,
certificate_chain,
status,
complete_certificate_chain
FROM aws.acmpca.certificate_authority_activation
WHERE region = 'us-east-1' AND data__Identifier = '<CertificateAuthorityArn>';
```


## Permissions

To operate on the <code>certificate_authority_activation</code> resource, the following permissions are required:

### Read
```json
acm-pca:GetCertificateAuthorityCertificate,
acm-pca:DescribeCertificateAuthority
```

### Update
```json
acm-pca:ImportCertificateAuthorityCertificate,
acm-pca:UpdateCertificateAuthority
```

