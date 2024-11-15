---
title: clusters_clusterlints
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters_clusterlints
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

Creates, updates, deletes, gets or lists a <code>clusters_clusterlints</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>clusters_clusterlints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.kubernetes.clusters_clusterlints" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="completed_at" /> | `string` | A time value given in ISO8601 combined date and time format that represents when the schedule clusterlint run request was completed. |
| <CopyableCode code="diagnostics" /> | `array` | An array of diagnostics reporting potential problems for the given cluster. |
| <CopyableCode code="requested_at" /> | `string` | A time value given in ISO8601 combined date and time format that represents when the schedule clusterlint run request was made. |
| <CopyableCode code="run_id" /> | `string` | Id of the clusterlint run that can be used later to fetch the diagnostics. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="kubernetes_get_cluster_lint_results" /> | `SELECT` | <CopyableCode code="cluster_id" /> | To request clusterlint diagnostics for your cluster, send a GET request to `/v2/kubernetes/clusters/$K8S_CLUSTER_ID/clusterlint`. If the `run_id` query parameter is provided, then the diagnostics for the specific run is fetched. By default, the latest results are shown. To find out how to address clusterlint feedback, please refer to [the clusterlint check documentation](https://github.com/digitalocean/clusterlint/blob/master/checks.md). |
| <CopyableCode code="kubernetes_run_cluster_lint" /> | `EXEC` | <CopyableCode code="cluster_id" /> | Clusterlint helps operators conform to Kubernetes best practices around resources, security and reliability to avoid common problems while operating or upgrading the clusters. To request a clusterlint run on your cluster, send a POST request to `/v2/kubernetes/clusters/$K8S_CLUSTER_ID/clusterlint`. This will run all checks present in the `doks` group by default, if a request body is not specified. Optionally specify the below attributes. For information about the available checks, please refer to [the clusterlint check documentation](https://github.com/digitalocean/clusterlint/blob/master/checks.md). |

## `SELECT` examples

To request clusterlint diagnostics for your cluster, send a GET request to `/v2/kubernetes/clusters/$K8S_CLUSTER_ID/clusterlint`. If the `run_id` query parameter is provided, then the diagnostics for the specific run is fetched. By default, the latest results are shown. To find out how to address clusterlint feedback, please refer to [the clusterlint check documentation](https://github.com/digitalocean/clusterlint/blob/master/checks.md).


```sql
SELECT
completed_at,
diagnostics,
requested_at,
run_id
FROM digitalocean.kubernetes.clusters_clusterlints
WHERE cluster_id = '{{ cluster_id }}';
```