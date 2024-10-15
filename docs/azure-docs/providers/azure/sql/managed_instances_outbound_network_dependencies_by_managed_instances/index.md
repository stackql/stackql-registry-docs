---
title: managed_instances_outbound_network_dependencies_by_managed_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_instances_outbound_network_dependencies_by_managed_instances
  - sql
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

Creates, updates, deletes, gets or lists a <code>managed_instances_outbound_network_dependencies_by_managed_instances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>managed_instances_outbound_network_dependencies_by_managed_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.managed_instances_outbound_network_dependencies_by_managed_instances" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="category" /> | `string` | The type of service accessed by the managed instance service, e.g., Azure Storage, Azure Active Directory, etc. |
| <CopyableCode code="endpoints" /> | `array` | The endpoints that the managed instance service communicates with in order to function correctly. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="managedInstanceName, resourceGroupName, subscriptionId" /> | Gets the collection of outbound network dependencies for the given managed instance. |

## `SELECT` examples

Gets the collection of outbound network dependencies for the given managed instance.


```sql
SELECT
category,
endpoints
FROM azure.sql.managed_instances_outbound_network_dependencies_by_managed_instances
WHERE managedInstanceName = '{{ managedInstanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```