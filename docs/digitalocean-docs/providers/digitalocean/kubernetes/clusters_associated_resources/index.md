---
title: clusters_associated_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters_associated_resources
  - kubernetes
  - digitalocean
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage digitalocean resources using SQL
custom_edit_url: null
image: /img/providers/digitalocean/stackql-digitalocean-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>clusters_associated_resources</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>clusters_associated_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.kubernetes.clusters_associated_resources" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="load_balancers" /> | `array` | A list of names and IDs for associated load balancers that can be destroyed along with the cluster. |
| <CopyableCode code="volume_snapshots" /> | `array` | A list of names and IDs for associated volume snapshots that can be destroyed along with the cluster. |
| <CopyableCode code="volumes" /> | `array` | A list of names and IDs for associated volumes that can be destroyed along with the cluster. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="kubernetes_list_associated_resources" /> | `SELECT` | <CopyableCode code="cluster_id" /> | To list the associated billable resources that can be destroyed along with a cluster, send a GET request to the `/v2/kubernetes/clusters/$K8S_CLUSTER_ID/destroy_with_associated_resources` endpoint. |

## `SELECT` examples

To list the associated billable resources that can be destroyed along with a cluster, send a GET request to the `/v2/kubernetes/clusters/$K8S_CLUSTER_ID/destroy_with_associated_resources` endpoint.


```sql
SELECT
load_balancers,
volume_snapshots,
volumes
FROM digitalocean.kubernetes.clusters_associated_resources
WHERE cluster_id = '{{ cluster_id }}';
```