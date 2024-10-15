---
title: firewall_status
hide_title: false
hide_table_of_contents: false
keywords:
  - firewall_status
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

Creates, updates, deletes, gets or lists a <code>firewall_status</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>firewall_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.paloalto.firewall_status" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Firewall Status |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="firewallName, resourceGroupName, subscriptionId" /> | Get a FirewallStatusResource |
| <CopyableCode code="list_by_firewalls" /> | `SELECT` | <CopyableCode code="firewallName, resourceGroupName, subscriptionId" /> | List FirewallStatusResource resources by Firewalls |

## `SELECT` examples

Get a FirewallStatusResource


```sql
SELECT
properties,
systemData
FROM azure_isv.paloalto.firewall_status
WHERE firewallName = '{{ firewallName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```