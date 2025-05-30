---
title: artifact_stores_network_fabric_controller_end_points
hide_title: false
hide_table_of_contents: false
keywords:
  - artifact_stores_network_fabric_controller_end_points
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

Creates, updates, deletes, gets or lists a <code>artifact_stores_network_fabric_controller_end_points</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>artifact_stores_network_fabric_controller_end_points</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hybrid_network.artifact_stores_network_fabric_controller_end_points" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="artifactStoreName, publisherName, resourceGroupName, subscriptionId" /> | Delete network fabric controllers on artifact stores |

## `DELETE` example

Deletes the specified <code>artifact_stores_network_fabric_controller_end_points</code> resource.

```sql
/*+ delete */
DELETE FROM azure.hybrid_network.artifact_stores_network_fabric_controller_end_points
WHERE artifactStoreName = '{{ artifactStoreName }}'
AND publisherName = '{{ publisherName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
