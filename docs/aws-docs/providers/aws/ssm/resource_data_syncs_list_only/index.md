---
title: resource_data_syncs_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_data_syncs_list_only
  - ssm
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

Lists <code>resource_data_syncs</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/resource_data_syncs/"><code>resource_data_syncs</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resource_data_syncs_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SSM::ResourceDataSync</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ssm.resource_data_syncs_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="s3_destination" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="kms_key_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="sync_source" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="bucket_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="bucket_region" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="sync_format" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="sync_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="sync_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="bucket_prefix" /></td><td><code>string</code></td><td></td></tr>
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
Lists all <code>resource_data_syncs</code> in a region.
```sql
SELECT
region,
sync_name
FROM aws.ssm.resource_data_syncs_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>resource_data_syncs_list_only</code> resource, see <a href="/providers/aws/ssm/resource_data_syncs/#permissions"><code>resource_data_syncs</code></a>


