---
title: vpn_server_configurations_associated_with_virtual_wans
hide_title: false
hide_table_of_contents: false
keywords:
  - vpn_server_configurations_associated_with_virtual_wans
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

Creates, updates, deletes, gets or lists a <code>vpn_server_configurations_associated_with_virtual_wans</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpn_server_configurations_associated_with_virtual_wans</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.vpn_server_configurations_associated_with_virtual_wans" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="vpnServerConfigurationResourceIds" /> | `array` | List of VpnServerConfigurations associated with VirtualWan. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, virtualWANName" /> | Gives the list of VpnServerConfigurations associated with Virtual Wan in a resource group. |

## `SELECT` examples

Gives the list of VpnServerConfigurations associated with Virtual Wan in a resource group.


```sql
SELECT
vpnServerConfigurationResourceIds
FROM azure.network.vpn_server_configurations_associated_with_virtual_wans
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND virtualWANName = '{{ virtualWANName }}';
```