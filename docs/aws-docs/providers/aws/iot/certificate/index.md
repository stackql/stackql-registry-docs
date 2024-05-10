---
title: certificate
hide_title: false
hide_table_of_contents: false
keywords:
  - certificate
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Gets or updates an individual <code>certificate</code> resource, use <code>certificates</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>certificate</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Use the AWS::IoT::Certificate resource to declare an AWS IoT X.509 certificate.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iot.certificate" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="ca_certificate_pem" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="certificate_pem" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="certificate_signing_request" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="certificate_mode" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
ca_certificate_pem,
certificate_pem,
certificate_signing_request,
certificate_mode,
status,
id,
arn
FROM aws.iot.certificate
WHERE region = 'us-east-1' AND data__Identifier = '<Id>';
```


## Permissions

To operate on the <code>certificate</code> resource, the following permissions are required:

### Read
```json
iot:DescribeCertificate
```

### Update
```json
iot:UpdateCertificate,
iot:DescribeCertificate
```

