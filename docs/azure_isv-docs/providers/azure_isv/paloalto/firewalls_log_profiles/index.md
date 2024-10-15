---
title: firewalls_log_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - firewalls_log_profiles
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

Creates, updates, deletes, gets or lists a <code>firewalls_log_profiles</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>firewalls_log_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.paloalto.firewalls_log_profiles" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="applicationInsights" /> | `object` | Application Insights key |
| <CopyableCode code="commonDestination" /> | `object` | Log Destination |
| <CopyableCode code="decryptLogDestination" /> | `object` | Log Destination |
| <CopyableCode code="logOption" /> | `string` | Log options possible |
| <CopyableCode code="logType" /> | `string` | Possible log types |
| <CopyableCode code="threatLogDestination" /> | `object` | Log Destination |
| <CopyableCode code="trafficLogDestination" /> | `object` | Log Destination |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="firewallName, resourceGroupName, subscriptionId" /> | Log Profile for Firewall |

## `SELECT` examples

Log Profile for Firewall


```sql
SELECT
applicationInsights,
commonDestination,
decryptLogDestination,
logOption,
logType,
threatLogDestination,
trafficLogDestination
FROM azure_isv.paloalto.firewalls_log_profiles
WHERE firewallName = '{{ firewallName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```