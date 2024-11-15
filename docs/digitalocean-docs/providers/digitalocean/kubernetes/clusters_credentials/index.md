---
title: clusters_credentials
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters_credentials
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

Creates, updates, deletes, gets or lists a <code>clusters_credentials</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>clusters_credentials</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.kubernetes.clusters_credentials" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="certificate_authority_data" /> | `string` | A base64 encoding of bytes representing the certificate authority data for accessing the cluster. |
| <CopyableCode code="client_certificate_data" /> | `string` | A base64 encoding of bytes representing the x509 client certificate data for access the cluster. This is only returned for clusters without support for token-based authentication. Newly created Kubernetes clusters do not return credentials using certificate-based authentication. For additional information, [see here](https://docs.digitalocean.com/products/kubernetes/how-to/connect-to-cluster/#authenticate). |
| <CopyableCode code="client_key_data" /> | `string` | A base64 encoding of bytes representing the x509 client key data for access the cluster. This is only returned for clusters without support for token-based authentication. Newly created Kubernetes clusters do not return credentials using certificate-based authentication. For additional information, [see here](https://docs.digitalocean.com/products/kubernetes/how-to/connect-to-cluster/#authenticate). |
| <CopyableCode code="expires_at" /> | `string` | A time value given in ISO8601 combined date and time format that represents when the access token expires. |
| <CopyableCode code="server" /> | `string` | The URL used to access the cluster API server. |
| <CopyableCode code="token" /> | `string` | An access token used to authenticate with the cluster. This is only returned for clusters with support for token-based authentication. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="kubernetes_get_credentials" /> | `SELECT` | <CopyableCode code="cluster_id" /> | This endpoint returns a JSON object . It can be used to programmatically construct Kubernetes clients which cannot parse kubeconfig files. The resulting JSON object contains token-based authentication for clusters supporting it, and certificate-based authentication otherwise. For a list of supported versions and more information, see "[How to Connect to a DigitalOcean Kubernetes Cluster](https://docs.digitalocean.com/products/kubernetes/how-to/connect-to-cluster/)". To retrieve credentials for accessing a Kubernetes cluster, send a GET request to `/v2/kubernetes/clusters/$K8S_CLUSTER_ID/credentials`. Clusters supporting token-based authentication may define an expiration by passing a duration in seconds as a query parameter to `/v2/kubernetes/clusters/$K8S_CLUSTER_ID/credentials?expiry_seconds=$DURATION_IN_SECONDS`. If not set or 0, then the token will have a 7 day expiry. The query parameter has no impact in certificate-based authentication. |

## `SELECT` examples

This endpoint returns a JSON object . It can be used to programmatically construct Kubernetes clients which cannot parse kubeconfig files. The resulting JSON object contains token-based authentication for clusters supporting it, and certificate-based authentication otherwise. For a list of supported versions and more information, see "[How to Connect to a DigitalOcean Kubernetes Cluster](https://docs.digitalocean.com/products/kubernetes/how-to/connect-to-cluster/)". To retrieve credentials for accessing a Kubernetes cluster, send a GET request to `/v2/kubernetes/clusters/$K8S_CLUSTER_ID/credentials`. Clusters supporting token-based authentication may define an expiration by passing a duration in seconds as a query parameter to `/v2/kubernetes/clusters/$K8S_CLUSTER_ID/credentials?expiry_seconds=$DURATION_IN_SECONDS`. If not set or 0, then the token will have a 7 day expiry. The query parameter has no impact in certificate-based authentication.


```sql
SELECT
certificate_authority_data,
client_certificate_data,
client_key_data,
expires_at,
server,
token
FROM digitalocean.kubernetes.clusters_credentials
WHERE cluster_id = '{{ cluster_id }}';
```