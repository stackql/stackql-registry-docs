---
title: key_signing_keys_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - key_signing_keys_list_only
  - route53
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

Lists <code>key_signing_keys</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/key_signing_keys/"><code>key_signing_keys</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>key_signing_keys_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Represents a key signing key (KSK) associated with a hosted zone. You can only have two KSKs per hosted zone.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.route53.key_signing_keys_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="hosted_zone_id" /></td><td><code>string</code></td><td>The unique string (ID) used to identify a hosted zone.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>An alphanumeric string used to identify a key signing key (KSK). Name must be unique for each key signing key in the same hosted zone.</td></tr>
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
Lists all <code>key_signing_keys</code> in a region.
```sql
SELECT
region,
hosted_zone_id,
name
FROM aws.route53.key_signing_keys_list_only
;
```


## Permissions

For permissions required to operate on the <code>key_signing_keys_list_only</code> resource, see <a href="/providers/aws/route53/key_signing_keys/#permissions"><code>key_signing_keys</code></a>

