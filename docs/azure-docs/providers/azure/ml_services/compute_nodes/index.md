---
title: compute_nodes
hide_title: false
hide_table_of_contents: false
keywords:
  - compute_nodes
  - ml_services
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

Creates, updates, deletes, gets or lists a <code>compute_nodes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>compute_nodes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ml_services.compute_nodes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="nextLink" /> | `string` | The continuation token. |
| <CopyableCode code="nodes" /> | `array` | The collection of returned AmlCompute nodes details. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="computeName, resourceGroupName, subscriptionId, workspaceName" /> | Get the details (e.g IP address, port etc) of all the compute nodes in the compute. |

## `SELECT` examples

Get the details (e.g IP address, port etc) of all the compute nodes in the compute.


```sql
SELECT
nextLink,
nodes
FROM azure.ml_services.compute_nodes
WHERE computeName = '{{ computeName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```