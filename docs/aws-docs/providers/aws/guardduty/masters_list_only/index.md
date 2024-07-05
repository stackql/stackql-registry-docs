---
title: masters_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - masters_list_only
  - guardduty
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

Lists <code>masters</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/masters/"><code>masters</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>masters_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>GuardDuty Master resource schema</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.guardduty.masters_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="master_id" /></td><td><code>string</code></td><td>ID of the account used as the master account.</td></tr>
<tr><td><CopyableCode code="invitation_id" /></td><td><code>string</code></td><td>Value used to validate the master account to the member account.</td></tr>
<tr><td><CopyableCode code="detector_id" /></td><td><code>string</code></td><td>Unique ID of the detector of the GuardDuty member account.</td></tr>
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
Lists all <code>masters</code> in a region.
```sql
SELECT
region,
detector_id,
master_id
FROM aws.guardduty.masters_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>masters_list_only</code> resource, see <a href="/providers/aws/guardduty/masters/#permissions"><code>masters</code></a>


