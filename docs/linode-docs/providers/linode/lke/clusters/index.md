---
title: clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.lke.clusters" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `integer` | This Kubernetes cluster's unique ID. |
| <CopyableCode code="control_plane" /> | `object` | Defines settings for the Kubernetes Control Plane. Allows for the enabling of High Availability (HA) for Control Plane Components. Enabling High Avaialability for LKE is an **irreversible** change.<br /> |
| <CopyableCode code="created" /> | `string` | When this Kubernetes cluster was created. |
| <CopyableCode code="k8s_version" /> | `string` | The desired Kubernetes version for this Kubernetes cluster in the format of &lt;major&gt;.&lt;minor&gt;, and the latest supported patch version will be deployed.<br /> |
| <CopyableCode code="label" /> | `string` | This Kubernetes cluster's unique label for display purposes only.<br />Labels have the following constraints:<br /><br />  * UTF-8 characters will be returned by the API using escape<br />    sequences of their Unicode code points. For example, the<br />    Japanese character *か* is 3 bytes in UTF-8 (`0xE382AB`). Its<br />    Unicode code point is 2 bytes (`0x30AB`). APIv4 supports this<br />    character and the API will return it as the escape sequence<br />    using six 1 byte characters which represent 2 bytes of Unicode<br />    code point (`"\u30ab"`).<br />  * 4 byte UTF-8 characters are not supported.<br />  * If the label is entirely composed of UTF-8 characters, the API<br />    response will return the code points using up to 193 1 byte<br />    characters.<br /> |
| <CopyableCode code="region" /> | `string` | This Kubernetes cluster's location. |
| <CopyableCode code="tags" /> | `array` | An array of tags applied to the Kubernetes cluster. Tags are for organizational purposes only.<br /> |
| <CopyableCode code="updated" /> | `string` | When this Kubernetes cluster was updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getLKECluster" /> | `SELECT` | <CopyableCode code="clusterId" /> | Get a specific Cluster by ID.<br /> |
| <CopyableCode code="getLKEClusters" /> | `SELECT` |  | Lists current Kubernetes clusters available on your account.<br /> |
| <CopyableCode code="createLKECluster" /> | `INSERT` | <CopyableCode code="data__k8s_version, data__label, data__node_pools, data__region" /> | Creates a Kubernetes cluster. The Kubernetes cluster will be created<br />asynchronously. You can use the events system to determine when the<br />Kubernetes cluster is ready to use. Please note that it often takes 2-5 minutes before the<br />[Kubernetes API server endpoint](/docs/api/linode-kubernetes-engine-lke/#kubernetes-api-endpoints-list) and<br />the [Kubeconfig file](/docs/api/linode-kubernetes-engine-lke/#kubeconfig-view) for the new cluster<br />are ready.<br /> |
| <CopyableCode code="deleteLKECluster" /> | `DELETE` | <CopyableCode code="clusterId" /> | Deletes a Cluster you have permission to `read_write`.<br /><br />**Deleting a Cluster is a destructive action and cannot be undone.**<br /><br />Deleting a Cluster:<br />  - Deletes all Linodes in all pools within this Kubernetes cluster<br />  - Deletes all supporting Kubernetes services for this Kubernetes<br />    cluster (API server, etcd, etc)<br />  - Deletes all NodeBalancers created by this Kubernetes cluster<br />  - Does not delete any of the volumes created by this Kubernetes<br />    cluster<br /> |
| <CopyableCode code="_getLKECluster" /> | `EXEC` | <CopyableCode code="clusterId" /> | Get a specific Cluster by ID.<br /> |
| <CopyableCode code="_getLKEClusters" /> | `EXEC` |  | Lists current Kubernetes clusters available on your account.<br /> |
| <CopyableCode code="postLKECServiceTokenDelete" /> | `EXEC` | <CopyableCode code="clusterId" /> | Delete and regenerate the service account token for a Cluster.<br /><br />**Note**: When regenerating a service account token, the Cluster's control plane components and Linode CSI drivers are also restarted and configured with the new token. High Availability Clusters should not experience any disruption, while standard Clusters may experience brief control plane downtime while components are restarted.<br /> |
| <CopyableCode code="postLKEClusterRecycle" /> | `EXEC` | <CopyableCode code="clusterId" /> | Recycles all nodes in all pools of a designated Kubernetes Cluster. All Linodes within the Cluster will be deleted<br />and replaced with new Linodes on a rolling basis, which may take several minutes. Replacement Nodes are<br />installed with the latest available [patch version](https://github.com/kubernetes/community/blob/master/contributors/design-proposals/release/versioning.md#kubernetes-release-versioning) for the Cluster's current Kubernetes minor release.<br /><br />**Any local storage on deleted Linodes (such as "hostPath" and "emptyDir" volumes, or "local" PersistentVolumes) will be erased.**<br /> |
| <CopyableCode code="postLKEClusterRegenerate" /> | `EXEC` | <CopyableCode code="clusterId" /> | Regenerate the Kubeconfig file and/or the service account token for a Cluster.<br /><br />This is a helper command that allows performing both the [Kubeconfig Delete](#kubeconfig-delete) and the [Service Token Delete](#service-token-delete) actions with a single request.<br /><br />When using this command, at least one of `kubeconfig` or `servicetoken` is required.<br /><br />**Note**: When regenerating a service account token, the Cluster's control plane components and Linode CSI drivers are also restarted and configured with the new token. High Availability Clusters should not experience any disruption, while standard Clusters may experience brief control plane downtime while components are restarted.<br /> |
| <CopyableCode code="putLKECluster" /> | `EXEC` | <CopyableCode code="clusterId" /> | Updates a Kubernetes cluster.<br /> |
