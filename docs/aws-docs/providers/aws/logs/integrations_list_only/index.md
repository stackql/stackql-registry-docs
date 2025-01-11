---
title: integrations_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - integrations_list_only
  - logs
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

Lists <code>integrations</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/integrations/"><code>integrations</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>integrations_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Schema for Logs Integration Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.logs.integrations_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="integration_name" /></td><td><code>string</code></td><td>User provided identifier for integration, unique to the user account.</td></tr>
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
Lists all <code>integrations</code> in a region.
```sql
SELECT
region,
integration_name
FROM aws.logs.integrations_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>integrations_list_only</code> resource, see <a href="/providers/aws/logs/integrations/#permissions"><code>integrations</code></a>

