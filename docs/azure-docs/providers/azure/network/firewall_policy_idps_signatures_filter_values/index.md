---
title: firewall_policy_idps_signatures_filter_values
hide_title: false
hide_table_of_contents: false
keywords:
  - firewall_policy_idps_signatures_filter_values
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

Creates, updates, deletes, gets or lists a <code>firewall_policy_idps_signatures_filter_values</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>firewall_policy_idps_signatures_filter_values</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.firewall_policy_idps_signatures_filter_values" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="filterValues" /> | `array` | Describes the possible values |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="firewallPolicyName, resourceGroupName, subscriptionId" /> | Retrieves the current filter values for the signatures overrides |

## `SELECT` examples

Retrieves the current filter values for the signatures overrides


```sql
SELECT
filterValues
FROM azure.network.firewall_policy_idps_signatures_filter_values
WHERE firewallPolicyName = '{{ firewallPolicyName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```