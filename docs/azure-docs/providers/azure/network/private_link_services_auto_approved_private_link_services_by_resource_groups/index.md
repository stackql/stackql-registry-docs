---
title: private_link_services_auto_approved_private_link_services_by_resource_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - private_link_services_auto_approved_private_link_services_by_resource_groups
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

Creates, updates, deletes, gets or lists a <code>private_link_services_auto_approved_private_link_services_by_resource_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>private_link_services_auto_approved_private_link_services_by_resource_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.private_link_services_auto_approved_private_link_services_by_resource_groups" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="privateLinkService" /> | `string` | The id of the private link service resource. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="location, resourceGroupName, subscriptionId" /> | Returns all of the private link service ids that can be linked to a Private Endpoint with auto approved in this subscription in this region. |

## `SELECT` examples

Returns all of the private link service ids that can be linked to a Private Endpoint with auto approved in this subscription in this region.


```sql
SELECT
privateLinkService
FROM azure.network.private_link_services_auto_approved_private_link_services_by_resource_groups
WHERE location = '{{ location }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```