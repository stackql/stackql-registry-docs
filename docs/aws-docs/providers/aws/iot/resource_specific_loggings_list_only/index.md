---
title: resource_specific_loggings_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_specific_loggings_list_only
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

Lists <code>resource_specific_loggings</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/resource_specific_loggings/"><code>resource_specific_loggings</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resource_specific_loggings_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource-specific logging allows you to specify a logging level for a specific thing group.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iot.resource_specific_loggings_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="target_type" /></td><td><code>string</code></td><td>The target type. Value must be THING_GROUP, CLIENT_ID, SOURCE_IP, PRINCIPAL_ID, or EVENT_TYPE.</td></tr>
<tr><td><CopyableCode code="target_name" /></td><td><code>string</code></td><td>The target name.</td></tr>
<tr><td><CopyableCode code="log_level" /></td><td><code>string</code></td><td>The log level for a specific target. Valid values are: ERROR, WARN, INFO, DEBUG, or DISABLED.</td></tr>
<tr><td><CopyableCode code="target_id" /></td><td><code>string</code></td><td>Unique Id for a Target (TargetType:TargetName), this will be internally built to serve as primary identifier for a log target.</td></tr>
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
Lists all <code>resource_specific_loggings</code> in a region.
```sql
SELECT
region,
target_id
FROM aws.iot.resource_specific_loggings_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>resource_specific_loggings_list_only</code> resource, see <a href="/providers/aws/iot/resource_specific_loggings/#permissions"><code>resource_specific_loggings</code></a>


