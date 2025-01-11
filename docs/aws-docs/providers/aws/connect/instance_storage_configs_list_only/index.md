---
title: instance_storage_configs_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - instance_storage_configs_list_only
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

Lists <code>instance_storage_configs</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/instance_storage_configs/"><code>instance_storage_configs</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instance_storage_configs_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Connect::InstanceStorageConfig</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.connect.instance_storage_configs_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="instance_arn" /></td><td><code>string</code></td><td>Connect Instance ID with which the storage config will be associated</td></tr>
<tr><td><CopyableCode code="resource_type" /></td><td><code>string</code></td><td>Specifies the type of storage resource available for the instance</td></tr>
<tr><td><CopyableCode code="association_id" /></td><td><code>string</code></td><td>An associationID is automatically generated when a storage config is associated with an instance</td></tr>
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
Lists all <code>instance_storage_configs</code> in a region.
```sql
SELECT
region,
instance_arn,
association_id,
resource_type
FROM aws.connect.instance_storage_configs_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>instance_storage_configs_list_only</code> resource, see <a href="/providers/aws/connect/instance_storage_configs/#permissions"><code>instance_storage_configs</code></a>

