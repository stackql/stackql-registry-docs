---
title: server_capabilities
hide_title: false
hide_table_of_contents: false
keywords:
  - server_capabilities
  - postgresql
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

Creates, updates, deletes, gets or lists a <code>server_capabilities</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>server_capabilities</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.postgresql.server_capabilities" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Name of flexible servers capability |
| <CopyableCode code="fastProvisioningSupported" /> | `string` | Gets a value indicating whether fast provisioning is supported. "Enabled" means fast provisioning is supported. "Disabled" stands for fast provisioning is not supported. |
| <CopyableCode code="geoBackupSupported" /> | `string` | Determines if geo-backup is supported in this region. "Enabled" means geo-backup is supported. "Disabled" stands for geo-back is not supported. |
| <CopyableCode code="onlineResizeSupported" /> | `string` | A value indicating whether online resize is supported in this region for the given subscription. "Enabled" means storage online resize is supported. "Disabled" means storage online resize is not supported. |
| <CopyableCode code="reason" /> | `string` | The reason for the capability not being available. |
| <CopyableCode code="restricted" /> | `string` | A value indicating whether this region is restricted. "Enabled" means region is restricted. "Disabled" stands for region is not restricted. |
| <CopyableCode code="status" /> | `string` | The status of the capability. |
| <CopyableCode code="storageAutoGrowthSupported" /> | `string` | A value indicating whether storage auto-grow is supported in this region. "Enabled" means storage auto-grow is supported. "Disabled" stands for storage auto-grow is not supported. |
| <CopyableCode code="supportedFastProvisioningEditions" /> | `array` | List of supported server editions for fast provisioning |
| <CopyableCode code="supportedServerEditions" /> | `array` | List of supported flexible server editions |
| <CopyableCode code="supportedServerVersions" /> | `array` | The list of server versions supported for this capability. |
| <CopyableCode code="zoneRedundantHaAndGeoBackupSupported" /> | `string` | A value indicating whether Zone Redundant HA and Geo-backup is supported in this region. "Enabled" means zone redundant HA and geo-backup is supported. "Disabled" stands for zone redundant HA and geo-backup is not supported. |
| <CopyableCode code="zoneRedundantHaSupported" /> | `string` | A value indicating whether Zone Redundant HA is supported in this region. "Enabled" means zone redundant HA is supported. "Disabled" stands for zone redundant HA is not supported. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Get capabilities for a flexible server. |

## `SELECT` examples

Get capabilities for a flexible server.


```sql
SELECT
name,
fastProvisioningSupported,
geoBackupSupported,
onlineResizeSupported,
reason,
restricted,
status,
storageAutoGrowthSupported,
supportedFastProvisioningEditions,
supportedServerEditions,
supportedServerVersions,
zoneRedundantHaAndGeoBackupSupported,
zoneRedundantHaSupported
FROM azure.postgresql.server_capabilities
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```