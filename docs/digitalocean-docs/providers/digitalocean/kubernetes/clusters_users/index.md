---
title: clusters_users
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters_users
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

Creates, updates, deletes, gets or lists a <code>clusters_users</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>clusters_users</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.kubernetes.clusters_users" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="groups" /> | `array` | A list of in-cluster groups that the user belongs to. |
| <CopyableCode code="username" /> | `string` | The username for the cluster admin user. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="kubernetes_get_cluster_user" /> | `SELECT` | <CopyableCode code="cluster_id" /> | To show information the user associated with a Kubernetes cluster, send a GET request to `/v2/kubernetes/clusters/$K8S_CLUSTER_ID/user`. |

## `SELECT` examples

To show information the user associated with a Kubernetes cluster, send a GET request to `/v2/kubernetes/clusters/$K8S_CLUSTER_ID/user`.


```sql
SELECT
groups,
username
FROM digitalocean.kubernetes.clusters_users
WHERE cluster_id = '{{ cluster_id }}';
```