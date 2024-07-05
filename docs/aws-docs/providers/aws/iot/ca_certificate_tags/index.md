---
title: ca_certificate_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - ca_certificate_tags
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

Expands all tag keys and values for <code>ca_certificates</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ca_certificate_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Registers a CA Certificate in IoT.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iot.ca_certificate_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="ca_certificate_pem" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="verification_certificate_pem" /></td><td><code>string</code></td><td>The private key verification certificate.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="certificate_mode" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="auto_registration_status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="remove_auto_registration" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="registration_config" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tag_key" /></td><td><code>string</code></td><td>Tag key.</td></tr>
<tr><td><CopyableCode code="tag_value" /></td><td><code>string</code></td><td>Tag value.</td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Expands tags for all <code>ca_certificates</code> in a region.
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
tag_key,
tag_value
FROM aws.iot.ca_certificate_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>ca_certificate_tags</code> resource, see <a href="/providers/aws/iot/ca_certificates/#permissions"><code>ca_certificates</code></a>


