---
title: bastion_shareable_links
hide_title: false
hide_table_of_contents: false
keywords:
  - bastion_shareable_links
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

Creates, updates, deletes, gets or lists a <code>bastion_shareable_links</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>bastion_shareable_links</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.bastion_shareable_links" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="bsl" /> | `string` | The unique Bastion Shareable Link to the virtual machine. |
| <CopyableCode code="createdAt" /> | `string` | The time when the link was created. |
| <CopyableCode code="message" /> | `string` | Optional field indicating the warning or error message related to the vm in case of partial failure. |
| <CopyableCode code="vm" /> | `object` | Describes a Virtual Machine. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="bastionHostName, resourceGroupName, subscriptionId" /> | Return the Bastion Shareable Links for all the VMs specified in the request. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="bastionHostName, resourceGroupName, subscriptionId" /> | Deletes the Bastion Shareable Links for all the VMs specified in the request. |
| <CopyableCode code="put" /> | `EXEC` | <CopyableCode code="bastionHostName, resourceGroupName, subscriptionId" /> | Creates a Bastion Shareable Links for all the VMs specified in the request. |

## `SELECT` examples

Return the Bastion Shareable Links for all the VMs specified in the request.


```sql
SELECT
bsl,
createdAt,
message,
vm
FROM azure.network.bastion_shareable_links
WHERE bastionHostName = '{{ bastionHostName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `DELETE` example

Deletes the specified <code>bastion_shareable_links</code> resource.

```sql
/*+ delete */
DELETE FROM azure.network.bastion_shareable_links
WHERE bastionHostName = '{{ bastionHostName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
