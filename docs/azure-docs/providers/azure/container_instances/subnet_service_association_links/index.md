---
title: subnet_service_association_links
hide_title: false
hide_table_of_contents: false
keywords:
  - subnet_service_association_links
  - container_instances
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

Creates, updates, deletes, gets or lists a <code>subnet_service_association_links</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>subnet_service_association_links</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_instances.subnet_service_association_links" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, subnetName, subscriptionId, virtualNetworkName" /> | Delete container group virtual network association links. The operation does not delete other resources provided by the user. |

## `DELETE` example

Deletes the specified <code>subnet_service_association_links</code> resource.

```sql
/*+ delete */
DELETE FROM azure.container_instances.subnet_service_association_links
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subnetName = '{{ subnetName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND virtualNetworkName = '{{ virtualNetworkName }}';
```
