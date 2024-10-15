---
title: firewall_policy_idps_signatures
hide_title: false
hide_table_of_contents: false
keywords:
  - firewall_policy_idps_signatures
  - network
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

Creates, updates, deletes, gets or lists a <code>firewall_policy_idps_signatures</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>firewall_policy_idps_signatures</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.firewall_policy_idps_signatures" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="matchingRecordsCount" /> | `integer` | Number of total records matching the query. |
| <CopyableCode code="signatures" /> | `array` | Array containing the results of the query |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="firewallPolicyName, resourceGroupName, subscriptionId" /> | Retrieves the current status of IDPS signatures for the relevant policy. Maximal amount of returned signatures is 1000. |

## `SELECT` examples

Retrieves the current status of IDPS signatures for the relevant policy. Maximal amount of returned signatures is 1000.


```sql
SELECT
matchingRecordsCount,
signatures
FROM azure.network.firewall_policy_idps_signatures
WHERE firewallPolicyName = '{{ firewallPolicyName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```