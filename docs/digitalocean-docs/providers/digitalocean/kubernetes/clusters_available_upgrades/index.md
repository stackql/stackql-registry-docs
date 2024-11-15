---
title: clusters_available_upgrades
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters_available_upgrades
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

Creates, updates, deletes, gets or lists a <code>clusters_available_upgrades</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>clusters_available_upgrades</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.kubernetes.clusters_available_upgrades" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="kubernetes_version" /> | `string` | The upstream version string for the version of Kubernetes provided by a given slug. |
| <CopyableCode code="slug" /> | `string` | The slug identifier for an available version of Kubernetes for use when creating or updating a cluster. The string contains both the upstream version of Kubernetes as well as the DigitalOcean revision. |
| <CopyableCode code="supported_features" /> | `array` | The features available with the version of Kubernetes provided by a given slug. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="kubernetes_get_available_upgrades" /> | `SELECT` | <CopyableCode code="cluster_id" /> | To determine whether a cluster can be upgraded, and the versions to which it can be upgraded, send a GET request to `/v2/kubernetes/clusters/$K8S_CLUSTER_ID/upgrades`. |

## `SELECT` examples

To determine whether a cluster can be upgraded, and the versions to which it can be upgraded, send a GET request to `/v2/kubernetes/clusters/$K8S_CLUSTER_ID/upgrades`.


```sql
SELECT
kubernetes_version,
slug,
supported_features
FROM digitalocean.kubernetes.clusters_available_upgrades
WHERE cluster_id = '{{ cluster_id }}';
```