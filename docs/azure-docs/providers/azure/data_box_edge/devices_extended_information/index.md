---
title: devices_extended_information
hide_title: false
hide_table_of_contents: false
keywords:
  - devices_extended_information
  - data_box_edge
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

Creates, updates, deletes, gets or lists a <code>devices_extended_information</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>devices_extended_information</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_box_edge.devices_extended_information" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The path ID that uniquely identifies the object. |
| <CopyableCode code="name" /> | `string` | The object name. |
| <CopyableCode code="properties" /> | `object` | The properties of the Data Box Edge/Gateway device extended info. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The hierarchical type of the object. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="deviceName, resourceGroupName, subscriptionId" /> | Gets additional information for the specified Azure Stack Edge/Data Box Gateway device. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="deviceName, resourceGroupName, subscriptionId" /> | Gets additional information for the specified Data Box Edge/Data Box Gateway device. |

## `SELECT` examples

Gets additional information for the specified Azure Stack Edge/Data Box Gateway device.


```sql
SELECT
id,
name,
properties,
systemData,
type
FROM azure.data_box_edge.devices_extended_information
WHERE deviceName = '{{ deviceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```