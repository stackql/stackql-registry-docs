---
title: connected_cluster_cluster_user_credential
hide_title: false
hide_table_of_contents: false
keywords:
  - connected_cluster_cluster_user_credential
  - hybrid_kubernetes
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connected_cluster_cluster_user_credential</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.hybrid_kubernetes.connected_cluster_cluster_user_credential</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `hybridConnectionConfig` | `object` | Contains the REP (rendezvous endpoint) and “Sender” access token. |
| `kubeconfigs` | `array` | Base64-encoded Kubernetes configuration file. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `clusterName, resourceGroupName, subscriptionId, data__authenticationMethod, data__clientProxy` |
