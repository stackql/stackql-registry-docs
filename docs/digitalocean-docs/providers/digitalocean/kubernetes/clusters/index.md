---
title: clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters
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

Creates, updates, deletes, gets or lists a <code>clusters</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.kubernetes.clusters" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="column_anon" /> | `` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="kubernetes_get_cluster" /> | `SELECT` | <CopyableCode code="cluster_id" /> | To show information about an existing Kubernetes cluster, send a GET request to `/v2/kubernetes/clusters/$K8S_CLUSTER_ID`. |
| <CopyableCode code="kubernetes_list_clusters" /> | `SELECT` | <CopyableCode code="" /> | To list all of the Kubernetes clusters on your account, send a GET request to `/v2/kubernetes/clusters`. |
| <CopyableCode code="kubernetes_create_cluster" /> | `INSERT` | <CopyableCode code="data__name, data__node_pools, data__region, data__version" /> | To create a new Kubernetes cluster, send a POST request to `/v2/kubernetes/clusters`. The request must contain at least one node pool with at least one worker. The request may contain a maintenance window policy describing a time period when disruptive maintenance tasks may be carried out. Omitting the policy implies that a window will be chosen automatically. See [here](https://docs.digitalocean.com/products/kubernetes/how-to/upgrade-cluster/) for details. |
| <CopyableCode code="kubernetes_delete_cluster" /> | `DELETE` | <CopyableCode code="cluster_id" /> | To delete a Kubernetes cluster and all services deployed to it, send a DELETE request to `/v2/kubernetes/clusters/$K8S_CLUSTER_ID`. A 204 status code with no body will be returned in response to a successful request. |
| <CopyableCode code="kubernetes_destroy_associated_resources_dangerous" /> | `EXEC` | <CopyableCode code="cluster_id" /> | To delete a Kubernetes cluster with all of its associated resources, send a DELETE request to `/v2/kubernetes/clusters/$K8S_CLUSTER_ID/destroy_with_associated_resources/dangerous`. A 204 status code with no body will be returned in response to a successful request. |
| <CopyableCode code="kubernetes_destroy_associated_resources_selective" /> | `EXEC` | <CopyableCode code="cluster_id" /> | To delete a Kubernetes cluster along with a subset of its associated resources, send a DELETE request to `/v2/kubernetes/clusters/$K8S_CLUSTER_ID/destroy_with_associated_resources/selective`. The JSON body of the request should include `load_balancers`, `volumes`, or `volume_snapshots` keys each set to an array of IDs for the associated resources to be destroyed. The IDs can be found by querying the cluster's associated resources endpoint. Any associated resource not included in the request will remain and continue to accrue changes on your account. |
| <CopyableCode code="kubernetes_get_kubeconfig" /> | `EXEC` | <CopyableCode code="cluster_id" /> | This endpoint returns a kubeconfig file in YAML format. It can be used to connect to and administer the cluster using the Kubernetes command line tool, `kubectl`, or other programs supporting kubeconfig files (e.g., client libraries). The resulting kubeconfig file uses token-based authentication for clusters supporting it, and certificate-based authentication otherwise. For a list of supported versions and more information, see "[How to Connect to a DigitalOcean Kubernetes Cluster](https://docs.digitalocean.com/products/kubernetes/how-to/connect-to-cluster/)". To retrieve a kubeconfig file for use with a Kubernetes cluster, send a GET request to `/v2/kubernetes/clusters/$K8S_CLUSTER_ID/kubeconfig`. Clusters supporting token-based authentication may define an expiration by passing a duration in seconds as a query parameter to `/v2/kubernetes/clusters/$K8S_CLUSTER_ID/kubeconfig?expiry_seconds=$DURATION_IN_SECONDS`. If not set or 0, then the token will have a 7 day expiry. The query parameter has no impact in certificate-based authentication. |
| <CopyableCode code="kubernetes_update_cluster" /> | `EXEC` | <CopyableCode code="cluster_id, data__name" /> | To update a Kubernetes cluster, send a PUT request to `/v2/kubernetes/clusters/$K8S_CLUSTER_ID` and specify one or more of the attributes below. |
| <CopyableCode code="kubernetes_upgrade_cluster" /> | `EXEC` | <CopyableCode code="cluster_id" /> | To immediately upgrade a Kubernetes cluster to a newer patch release of Kubernetes, send a POST request to `/v2/kubernetes/clusters/$K8S_CLUSTER_ID/upgrade`. The body of the request must specify a version attribute. Available upgrade versions for a cluster can be fetched from `/v2/kubernetes/clusters/$K8S_CLUSTER_ID/upgrades`. |

## `SELECT` examples

To list all of the Kubernetes clusters on your account, send a GET request to `/v2/kubernetes/clusters`.


```sql
SELECT
column_anon
FROM digitalocean.kubernetes.clusters
;
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>clusters</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'Required Properties', value: 'required' },
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO digitalocean.kubernetes.clusters (
data__name,
data__region,
data__version,
data__cluster_subnet,
data__service_subnet,
data__vpc_uuid,
data__tags,
data__node_pools,
data__maintenance_policy,
data__auto_upgrade,
data__surge_upgrade,
data__ha,
data__control_plane_firewall
)
SELECT 
'{{ name }}',
'{{ region }}',
'{{ version }}',
'{{ cluster_subnet }}',
'{{ service_subnet }}',
'{{ vpc_uuid }}',
'{{ tags }}',
'{{ node_pools }}',
'{{ maintenance_policy }}',
'{{ auto_upgrade }}',
'{{ surge_upgrade }}',
'{{ ha }}',
'{{ control_plane_firewall }}'
;
```
</TabItem>

<TabItem value="required">

```sql
/*+ create */
INSERT INTO digitalocean.kubernetes.clusters (
data__name,
data__region,
data__version,
data__node_pools
)
SELECT 
'{{ name }}',
'{{ region }}',
'{{ version }}',
'{{ node_pools }}'
;
```
</TabItem>

<TabItem value="manifest">

```yaml
- name: clusters
  props:
    - name: data__name
      value: string
    - name: data__node_pools
      value: string
    - name: data__region
      value: string
    - name: data__version
      value: string
    - name: name
      value: string
    - name: region
      value: string
    - name: version
      value: string
    - name: cluster_subnet
      value: string
    - name: service_subnet
      value: string
    - name: vpc_uuid
      value: string
    - name: tags
      value: array
    - name: node_pools
      value: array
      props:
        - name: size
          value: string
        - name: name
          value: string
        - name: count
          value: integer
        - name: tags
          value: array
        - name: labels
          value: object
        - name: taints
          value: array
          props:
            - name: key
              value: string
            - name: value
              value: string
            - name: effect
              value: string
        - name: auto_scale
          value: boolean
        - name: min_nodes
          value: integer
        - name: max_nodes
          value: integer
    - name: maintenance_policy
      props:
        - name: start_time
          value: string
        - name: day
          value: string
    - name: auto_upgrade
      value: boolean
    - name: surge_upgrade
      value: boolean
    - name: ha
      value: boolean
    - name: control_plane_firewall
      props:
        - name: enable
          value: boolean
        - name: allowed_addresses
          value: array

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>clusters</code> resource.

```sql
/*+ delete */
DELETE FROM digitalocean.kubernetes.clusters
WHERE cluster_id = '{{ cluster_id }}';
```
