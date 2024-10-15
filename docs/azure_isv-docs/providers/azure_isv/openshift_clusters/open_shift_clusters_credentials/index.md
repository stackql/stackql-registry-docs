---
title: open_shift_clusters_credentials
hide_title: false
hide_table_of_contents: false
keywords:
  - open_shift_clusters_credentials
  - openshift_clusters
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

Creates, updates, deletes, gets or lists a <code>open_shift_clusters_credentials</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>open_shift_clusters_credentials</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.openshift_clusters.open_shift_clusters_credentials" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="kubeadminPassword" /> | `string` | The password for the kubeadmin user. |
| <CopyableCode code="kubeadminUsername" /> | `string` | The username for the kubeadmin user. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | The operation returns the credentials. |

## `SELECT` examples

The operation returns the credentials.


```sql
SELECT
kubeadminPassword,
kubeadminUsername
FROM azure_isv.openshift_clusters.open_shift_clusters_credentials
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```