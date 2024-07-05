---
title: loggings_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - loggings_list_only
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

Lists <code>loggings</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/loggings/"><code>loggings</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>loggings_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Logging Options enable you to configure your IoT V2 logging role and default logging level so that you can monitor progress events logs as it passes from your devices through Iot core service.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iot.loggings_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="account_id" /></td><td><code>string</code></td><td>Your 12-digit account ID (used as the primary identifier for the CloudFormation resource).</td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td>The ARN of the role that allows IoT to write to Cloudwatch logs.</td></tr>
<tr><td><CopyableCode code="default_log_level" /></td><td><code>string</code></td><td>The log level to use. Valid values are: ERROR, WARN, INFO, DEBUG, or DISABLED.</td></tr>
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
Lists all <code>loggings</code> in a region.
```sql
SELECT
region,
account_id
FROM aws.iot.loggings_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>loggings_list_only</code> resource, see <a href="/providers/aws/iot/loggings/#permissions"><code>loggings</code></a>


