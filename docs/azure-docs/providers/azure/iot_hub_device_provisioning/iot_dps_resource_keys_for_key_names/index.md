---
title: iot_dps_resource_keys_for_key_names
hide_title: false
hide_table_of_contents: false
keywords:
  - iot_dps_resource_keys_for_key_names
  - iot_hub_device_provisioning
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

Creates, updates, deletes, gets or lists a <code>iot_dps_resource_keys_for_key_names</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>iot_dps_resource_keys_for_key_names</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.iot_hub_device_provisioning.iot_dps_resource_keys_for_key_names" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="keyName" /> | `string` | Name of the key. |
| <CopyableCode code="primaryKey" /> | `string` | Primary SAS key value. |
| <CopyableCode code="rights" /> | `string` | Rights that this key has. |
| <CopyableCode code="secondaryKey" /> | `string` | Secondary SAS key value. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="keyName, provisioningServiceName, resourceGroupName, subscriptionId" /> | List primary and secondary keys for a specific key name |

## `SELECT` examples

List primary and secondary keys for a specific key name


```sql
SELECT
keyName,
primaryKey,
rights,
secondaryKey
FROM azure.iot_hub_device_provisioning.iot_dps_resource_keys_for_key_names
WHERE keyName = '{{ keyName }}'
AND provisioningServiceName = '{{ provisioningServiceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```