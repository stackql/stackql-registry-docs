---
title: certificate_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - certificate_tags
  - transfer
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

Expands all tag keys and values for <code>certificates</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>certificate_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Transfer::Certificate</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.transfer.certificate_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="usage" /></td><td><code>string</code></td><td>Specifies the usage type for the certificate.</td></tr>
<tr><td><CopyableCode code="certificate" /></td><td><code>string</code></td><td>Specifies the certificate body to be imported.</td></tr>
<tr><td><CopyableCode code="certificate_chain" /></td><td><code>string</code></td><td>Specifies the certificate chain to be imported.</td></tr>
<tr><td><CopyableCode code="private_key" /></td><td><code>string</code></td><td>Specifies the private key for the certificate.</td></tr>
<tr><td><CopyableCode code="active_date" /></td><td><code>string</code></td><td>Specifies the active date for the certificate.</td></tr>
<tr><td><CopyableCode code="inactive_date" /></td><td><code>string</code></td><td>Specifies the inactive date for the certificate.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A textual description for the certificate.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Specifies the unique Amazon Resource Name (ARN) for the agreement.</td></tr>
<tr><td><CopyableCode code="certificate_id" /></td><td><code>string</code></td><td>A unique identifier for the certificate.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>A status description for the certificate.</td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>Describing the type of certificate. With or without a private key.</td></tr>
<tr><td><CopyableCode code="serial" /></td><td><code>string</code></td><td>Specifies Certificate's serial.</td></tr>
<tr><td><CopyableCode code="not_before_date" /></td><td><code>string</code></td><td>Specifies the not before date for the certificate.</td></tr>
<tr><td><CopyableCode code="not_after_date" /></td><td><code>string</code></td><td>Specifies the not after date for the certificate.</td></tr>
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
Expands tags for all <code>certificates</code> in a region.
```sql
SELECT
region,
usage,
certificate,
certificate_chain,
private_key,
active_date,
inactive_date,
description,
arn,
certificate_id,
status,
type,
serial,
not_before_date,
not_after_date,
tag_key,
tag_value
FROM aws.transfer.certificate_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>certificate_tags</code> resource, see <a href="/providers/aws/transfer/certificates/#permissions"><code>certificates</code></a>

