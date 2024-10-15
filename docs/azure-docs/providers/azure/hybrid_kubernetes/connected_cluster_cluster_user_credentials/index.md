---
title: connected_cluster_cluster_user_credentials
hide_title: false
hide_table_of_contents: false
keywords:
  - connected_cluster_cluster_user_credentials
  - hybrid_kubernetes
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

Creates, updates, deletes, gets or lists a <code>connected_cluster_cluster_user_credentials</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connected_cluster_cluster_user_credentials</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hybrid_kubernetes.connected_cluster_cluster_user_credentials" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="hybridConnectionConfig" /> | `object` | Contains the REP (rendezvous endpoint) and “Sender” access token. |
| <CopyableCode code="kubeconfigs" /> | `array` | Base64-encoded Kubernetes configuration file. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId, data__authenticationMethod, data__clientProxy" /> | Gets cluster user credentials of the connected cluster with a specified resource group and name. |

## `SELECT` examples

Gets cluster user credentials of the connected cluster with a specified resource group and name.


```sql
SELECT
hybridConnectionConfig,
kubeconfigs
FROM azure.hybrid_kubernetes.connected_cluster_cluster_user_credentials
WHERE clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND data__authenticationMethod = '{{ data__authenticationMethod }}'
AND data__clientProxy = '{{ data__clientProxy }}';
```