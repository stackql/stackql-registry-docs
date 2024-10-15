---
title: post_rules_counters
hide_title: false
hide_table_of_contents: false
keywords:
  - post_rules_counters
  - paloalto
  - google
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>post_rules_counters</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>post_rules_counters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.paloalto.post_rules_counters" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="appSeen" /> | `object` | Data Type for App Seen |
| <CopyableCode code="firewallName" /> | `string` | firewall name |
| <CopyableCode code="hitCount" /> | `integer` | hit count |
| <CopyableCode code="lastUpdatedTimestamp" /> | `string` | last updated timestamp |
| <CopyableCode code="priority" /> | `string` | priority number |
| <CopyableCode code="requestTimestamp" /> | `string` | timestamp of request |
| <CopyableCode code="ruleListName" /> | `string` | rule list name |
| <CopyableCode code="ruleName" /> | `string` | rule name |
| <CopyableCode code="ruleStackName" /> | `string` | rule Stack Name |
| <CopyableCode code="timestamp" /> | `string` | timestamp of response |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="globalRulestackName, priority" /> | Get counters |

## `SELECT` examples

Get counters


```sql
SELECT
appSeen,
firewallName,
hitCount,
lastUpdatedTimestamp,
priority,
requestTimestamp,
ruleListName,
ruleName,
ruleStackName,
timestamp
FROM azure_isv.paloalto.post_rules_counters
WHERE globalRulestackName = '{{ globalRulestackName }}'
AND priority = '{{ priority }}';
```