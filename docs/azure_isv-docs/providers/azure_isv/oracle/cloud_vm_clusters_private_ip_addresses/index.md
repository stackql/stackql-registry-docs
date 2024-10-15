---
title: cloud_vm_clusters_private_ip_addresses
hide_title: false
hide_table_of_contents: false
keywords:
  - cloud_vm_clusters_private_ip_addresses
  - oracle
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

Creates, updates, deletes, gets or lists a <code>cloud_vm_clusters_private_ip_addresses</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cloud_vm_clusters_private_ip_addresses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.oracle.cloud_vm_clusters_private_ip_addresses" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="cloudvmclustername, resourceGroupName, subscriptionId, data__subnetId, data__vnicId" /> | List Private IP Addresses by the provided filter |

## `SELECT` examples

List Private IP Addresses by the provided filter


```sql
SELECT

FROM azure_isv.oracle.cloud_vm_clusters_private_ip_addresses
WHERE cloudvmclustername = '{{ cloudvmclustername }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND data__subnetId = '{{ data__subnetId }}'
AND data__vnicId = '{{ data__vnicId }}';
```