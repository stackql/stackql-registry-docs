---
title: clusters_kubeconfig
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters_kubeconfig
  - lke
  - linode    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Linode resources using SQL
custom_edit_url: null
image: /img/providers/linode/stackql-linode-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>clusters_kubeconfig</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>linode.lke.clusters_kubeconfig</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `getLKEClusterKubeconfig` | `SELECT` | `clusterId` | Get the Kubeconfig file for a Cluster. Please note that it often takes 2-5 minutes before<br />the Kubeconfig file is ready after first [creating a new cluster](/docs/api/linode-kubernetes-engine-lke/#kubernetes-cluster-create).<br /> |
| `deleteLKEClusterKubeconfig` | `DELETE` | `clusterId` | Delete and regenerate the Kubeconfig file for a Cluster.<br /> |
| `_getLKEClusterKubeconfig` | `EXEC` | `clusterId` | Get the Kubeconfig file for a Cluster. Please note that it often takes 2-5 minutes before<br />the Kubeconfig file is ready after first [creating a new cluster](/docs/api/linode-kubernetes-engine-lke/#kubernetes-cluster-create).<br /> |
