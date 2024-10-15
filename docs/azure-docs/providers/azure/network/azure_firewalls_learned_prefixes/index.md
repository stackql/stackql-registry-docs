---
title: azure_firewalls_learned_prefixes
hide_title: false
hide_table_of_contents: false
keywords:
  - azure_firewalls_learned_prefixes
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

Creates, updates, deletes, gets or lists a <code>azure_firewalls_learned_prefixes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>azure_firewalls_learned_prefixes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.azure_firewalls_learned_prefixes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="ipPrefixes" /> | `array` | IP Prefix value. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="azureFirewallName, resourceGroupName, subscriptionId" /> | Retrieves a list of all IP prefixes that azure firewall has learned to not SNAT. |

## `SELECT` examples

Retrieves a list of all IP prefixes that azure firewall has learned to not SNAT.


```sql
SELECT
ipPrefixes
FROM azure.network.azure_firewalls_learned_prefixes
WHERE azureFirewallName = '{{ azureFirewallName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```