---
title: approved_origins_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - approved_origins_list_only
  - connect
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

Lists <code>approved_origins</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/approved_origins/"><code>approved_origins</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>approved_origins_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Connect::ApprovedOrigin</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.connect.approved_origins_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="origin" /></td><td><code>string</code></td><td>Domain name to be added to the allowlist of instance</td></tr>
<tr><td><CopyableCode code="instance_id" /></td><td><code>string</code></td><td>Amazon Connect instance identifier</td></tr>
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
Lists all <code>approved_origins</code> in a region.
```sql
SELECT
region,
instance_id,
origin
FROM aws.connect.approved_origins_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>approved_origins_list_only</code> resource, see <a href="/providers/aws/connect/approved_origins/#permissions"><code>approved_origins</code></a>

