---
title: resource_keys_for_key_names
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_keys_for_key_names
  - iot_hub
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

Creates, updates, deletes, gets or lists a <code>resource_keys_for_key_names</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resource_keys_for_key_names</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.iot_hub.resource_keys_for_key_names" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="keyName" /> | `string` | The name of the shared access policy. |
| <CopyableCode code="primaryKey" /> | `string` | The primary key. |
| <CopyableCode code="rights" /> | `string` | The permissions assigned to the shared access policy. |
| <CopyableCode code="secondaryKey" /> | `string` | The secondary key. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="keyName, resourceGroupName, resourceName, subscriptionId" /> | Get a shared access policy by name from an IoT hub. For more information, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-security. |

## `SELECT` examples

Get a shared access policy by name from an IoT hub. For more information, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-security.


```sql
SELECT
keyName,
primaryKey,
rights,
secondaryKey
FROM azure.iot_hub.resource_keys_for_key_names
WHERE keyName = '{{ keyName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```