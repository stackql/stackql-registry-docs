---
title: artifact_stores_network_fabric_controller_private_end_points
hide_title: false
hide_table_of_contents: false
keywords:
  - artifact_stores_network_fabric_controller_private_end_points
  - hybrid_network
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

Creates, updates, deletes, gets or lists a <code>artifact_stores_network_fabric_controller_private_end_points</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>artifact_stores_network_fabric_controller_private_end_points</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hybrid_network.artifact_stores_network_fabric_controller_private_end_points" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="networkFabricControllerIds" /> | `array` | list of network fabric controllers. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="artifactStoreName, publisherName, resourceGroupName, subscriptionId" /> | List network fabric controllers to artifact stores |

## `SELECT` examples

List network fabric controllers to artifact stores


```sql
SELECT
networkFabricControllerIds
FROM azure.hybrid_network.artifact_stores_network_fabric_controller_private_end_points
WHERE artifactStoreName = '{{ artifactStoreName }}'
AND publisherName = '{{ publisherName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```