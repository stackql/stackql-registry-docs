---
title: api_keys_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - api_keys_list_only
  - location
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

Lists <code>api_keys</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/api_keys/"><code>api_keys</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>api_keys_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Location::APIKey Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.location.api_keys_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="create_time" /></td><td><code>string</code></td><td>The datetime value in ISO 8601 format. The timezone is always UTC. (YYYY-MM-DDThh:mm:ss.sssZ)</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="expire_time" /></td><td><code>string</code></td><td>The datetime value in ISO 8601 format. The timezone is always UTC. (YYYY-MM-DDThh:mm:ss.sssZ)</td></tr>
<tr><td><CopyableCode code="force_update" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="key_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="key_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="no_expiry" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="restrictions" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="update_time" /></td><td><code>string</code></td><td>The datetime value in ISO 8601 format. The timezone is always UTC. (YYYY-MM-DDThh:mm:ss.sssZ)</td></tr>
<tr><td><CopyableCode code="force_delete" /></td><td><code>boolean</code></td><td></td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Lists all <code>api_keys</code> in a region.
```sql
SELECT
region,
key_name
FROM aws.location.api_keys_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>api_keys_list_only</code> resource, see <a href="/providers/aws/location/api_keys/#permissions"><code>api_keys</code></a>


