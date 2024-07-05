---
title: ca_certificates_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - ca_certificates_list_only
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

Lists <code>ca_certificates</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/ca_certificates/"><code>ca_certificates</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ca_certificates_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Registers a CA Certificate in IoT.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iot.ca_certificates_list_only" /></td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Lists all <code>ca_certificates</code> in a region.
```sql
SELECT
region,
id
FROM aws.iot.ca_certificates_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>ca_certificates_list_only</code> resource, see <a href="/providers/aws/iot/ca_certificates/#permissions"><code>ca_certificates</code></a>


