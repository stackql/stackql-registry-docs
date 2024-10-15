---
title: service_association_links
hide_title: false
hide_table_of_contents: false
keywords:
  - service_association_links
  - network
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

Creates, updates, deletes, gets or lists a <code>service_association_links</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service_association_links</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.service_association_links" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Name of the resource that is unique within a resource group. This name can be used to access the resource. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="properties" /> | `object` | Properties of ServiceAssociationLink. |
| <CopyableCode code="type" /> | `string` | Resource type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subnetName, subscriptionId, virtualNetworkName" /> | Gets a list of service association links for a subnet. |

## `SELECT` examples

Gets a list of service association links for a subnet.


```sql
SELECT
id,
name,
etag,
properties,
type
FROM azure.network.service_association_links
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subnetName = '{{ subnetName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND virtualNetworkName = '{{ virtualNetworkName }}';
```