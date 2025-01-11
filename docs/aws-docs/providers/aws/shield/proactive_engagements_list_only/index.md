---
title: proactive_engagements_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - proactive_engagements_list_only
  - shield
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

Lists <code>proactive_engagements</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/proactive_engagements/"><code>proactive_engagements</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>proactive_engagements_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Authorizes the Shield Response Team (SRT) to use email and phone to notify contacts about escalations to the SRT and to initiate proactive customer support.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.shield.proactive_engagements_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="account_id" /></td><td><code>string</code></td><td></td></tr>
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
Lists all <code>proactive_engagements</code> in a region.
```sql
SELECT
region,
account_id
FROM aws.shield.proactive_engagements_list_only
;
```


## Permissions

For permissions required to operate on the <code>proactive_engagements_list_only</code> resource, see <a href="/providers/aws/shield/proactive_engagements/#permissions"><code>proactive_engagements</code></a>

