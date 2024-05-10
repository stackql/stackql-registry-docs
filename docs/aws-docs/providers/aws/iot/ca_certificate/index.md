---
title: ca_certificate
hide_title: false
hide_table_of_contents: false
keywords:
  - ca_certificate
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


Gets or updates an individual <code>ca_certificate</code> resource, use <code>ca_certificates</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ca_certificate</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Registers a CA Certificate in IoT.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iot.ca_certificate" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="ca_certificate_pem" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="verification_certificate_pem" /></td><td><code>string</code></td><td>The private key verification certificate.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="certificate_mode" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="auto_registration_status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="remove_auto_registration" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="registration_config" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
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
verification_certificate_pem,
status,
certificate_mode,
auto_registration_status,
remove_auto_registration,
registration_config,
id,
arn,
tags
FROM aws.iot.ca_certificate
WHERE region = 'us-east-1' AND data__Identifier = '<Id>';
```


## Permissions

To operate on the <code>ca_certificate</code> resource, the following permissions are required:

### Read
```json
iot:DescribeCACertificate,
iot:ListTagsForResource
```

### Update
```json
iam:GetRole,
iam:PassRole,
iot:UpdateCACertificate,
iot:DescribeCACertificate,
iot:TagResource,
iot:UntagResource,
iot:ListTagsForResource
```

