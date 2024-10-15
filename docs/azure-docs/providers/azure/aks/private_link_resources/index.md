---
title: private_link_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - private_link_resources
  - aks
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

Creates, updates, deletes, gets or lists a <code>private_link_resources</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>private_link_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.aks.private_link_resources" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The ID of the private link resource. |
| <CopyableCode code="name" /> | `string` | The name of the private link resource. |
| <CopyableCode code="groupId" /> | `string` | The group ID of the resource. |
| <CopyableCode code="privateLinkServiceID" /> | `string` | The private link service ID of the resource, this field is exposed only to NRP internally. |
| <CopyableCode code="requiredMembers" /> | `array` | The RequiredMembers of the resource |
| <CopyableCode code="type" /> | `string` | The resource type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | To learn more about private clusters, see: https://docs.microsoft.com/azure/aks/private-clusters |

## `SELECT` examples

To learn more about private clusters, see: https://docs.microsoft.com/azure/aks/private-clusters


```sql
SELECT
id,
name,
groupId,
privateLinkServiceID,
requiredMembers,
type
FROM azure.aks.private_link_resources
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```