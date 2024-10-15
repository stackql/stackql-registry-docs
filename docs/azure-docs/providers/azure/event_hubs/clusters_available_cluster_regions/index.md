---
title: clusters_available_cluster_regions
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters_available_cluster_regions
  - event_hubs
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

Creates, updates, deletes, gets or lists a <code>clusters_available_cluster_regions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>clusters_available_cluster_regions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.event_hubs.clusters_available_cluster_regions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | Location fo the Available Cluster |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List the quantity of available pre-provisioned Event Hubs Clusters, indexed by Azure region. |

## `SELECT` examples

List the quantity of available pre-provisioned Event Hubs Clusters, indexed by Azure region.


```sql
SELECT
location
FROM azure.event_hubs.clusters_available_cluster_regions
WHERE subscriptionId = '{{ subscriptionId }}';
```